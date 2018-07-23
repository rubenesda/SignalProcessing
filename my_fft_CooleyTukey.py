#Algoritm FFT of Cooley-Tukey

import cmath
import time
import matplotlib.pyplot as plt
import numpy as np

def omega(p, q):
    return cmath.exp((2.0 * cmath.pi * 1j * q) / p)

def fft(signal):
    n = len(signal)
    if n == 1:
        return signal
    else:
        Feven = fft([signal[i] for i in xrange(0, n, 2)])
        Fodd = fft([signal[i] for i in xrange(1, n, 2)])

        combined = [0] * n
        for m in xrange(n / 2):
            combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
            combined[m + n / 2] = Feven[m] - omega(n, -m) * Fodd[m]

        return combined

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
start = time.time() #Measure time of computing
yf = fft(y)
end = time.time()
elapsed = end - start
print(elapsed)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()

# Reference
# https://jeremykun.com/2012/07/18/the-fast-fourier-transform/
