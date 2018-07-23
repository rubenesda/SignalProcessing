import sounddevice as sd
import numpy as np
import time

M = 15
global x, y
x = np.zeros((M, 1))
y = 0

def myFiltrar (data):
    global x,y
    x[0] = data
    y = y + x[0] * 1
    y = y * (1 / float(M))
    return np.transpose(y)

def sumar ():
    global x,y
    for k in range(1, M):
        y = y + x[k] * 1
    y = y * (1 / float(M))

    for k in range(M - 1, -1, -1):
        x[k] = x[k - 1]

fs = 44100
duration = 5  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float32')
print "Recording Audio"
sd.wait()
print "Audio recording complete, play audio"
sd.play(myrecording, fs)
sd.wait()
print "Played audio complete"
np.savetxt('data.csv', (myrecording), delimiter=',')

# noisy Gaussian
mu, sigma = 0, 0.1  # mean and standard deviation
s = np.random.normal(mu, sigma, len(myrecording))
s = np.array(([s,]))
s = s.transpose()

# apply Noisy Gaussian
myrecording = myrecording + s

print "Play audio with noise"
sd.play(myrecording, fs)
sd.wait()
print "Played with noise audio complete"
np.savetxt('data2.csv', (myrecording), delimiter=',')

#Applying Filter moving average
Y = np.zeros(np.size(myrecording), dtype='float32')

start = time.time() #Measure time of computing
for j in range(0, np.size(myrecording, 0)):
    Y[j] = myFiltrar(myrecording[j])
    sumar()

end = time.time()
elapsed = end - start
print(elapsed)

print "Play Audio without Noise"
sd.play(Y, fs)
sd.wait()
print "Play without Noise Audio Complete"
