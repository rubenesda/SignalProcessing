# 
# Computes the discrete Fourier transform (DFT) of the given complex vector.
# 'input' is a sequence of numbers (integer, float, or complex).
# Returns a list of complex numbers as output, having the same length.
#

import numpy as np
import matplotlib.pyplot as plt
import cmath
import time

def compute_dft_complex(input):
	n = len(input)
	output = []
	for k in range(n):  # For each output element
		s = complex(0)
		for t in range(n):  # For each input element
			angle = 2j * cmath.pi * t * k / n
			s += input[t] * cmath.exp(-angle)
		output.append(s)
	return output


# 
# (Alternate implementation using only real numbers.)
# Computes the discrete Fourier transform (DFT) of the given complex vector.
# 'inreal' and 'inimag' are each a sequence of n floating-point numbers.
# Returns a tuple of two lists of floats - outreal and outimag, each of length n.
# 
import math
def compute_dft_real_pair(inreal, inimag):
	assert len(inreal) == len(inimag)
	n = len(inreal)
	outreal = []
	outimag = []
	for k in range(n):  # For each output element
		sumreal = 0.0
		sumimag = 0.0
		for t in range(n):  # For each input element
			angle = 2 * math.pi * t * k / n
			sumreal +=  inreal[t] * math.cos(angle) + inimag[t] * math.sin(angle)
			sumimag += -inreal[t] * math.sin(angle) + inimag[t] * math.cos(angle)
		outreal.append(sumreal)
		outimag.append(sumimag)
	return (outreal, outimag)

# https://www.nayuki.io/page/how-to-implement-the-discrete-fourier-transform
# https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
start = time.time() #Measure time of computing
yf = compute_dft_complex(y)
end = time.time()
elapsed = end - start
print(elapsed)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()