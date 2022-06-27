import numpy as np
import cmath
import matplotlib.pyplot as plt


class fourierTransform:
    def __init__(self, amplitude, time):
        self.amplitude = amplitude
        self.time = time
        self.cAmplitudes = np.array([])

        Fs = 1 / (self.time[1] - self.time[0])
        N = len(self.time)
        fStep = Fs / N
        self.frequency = np.linspace(0, (N/2-1)*fStep, N)
        self.calculateAmplitudes()

    def calculateIntegration(self, f=0,):
        output = self.amplitude[0] * cmath.exp(complex(0, -2 * cmath.pi * f * self.time[0])) + \
                 self.amplitude[-1] * cmath.exp(complex(0, -2 * cmath.pi * f * self.time[-1]))
        step = self.time[1] - self.time[0]
        index = np.arange(0, len(self.amplitude), 1)
        for i in index:
            output += 2 * self.amplitude[i] * cmath.exp(complex(0, -2 * cmath.pi * f * self.time[i]))
        output = 0.5 * output * step

        return output

    def calculateAmplitudes(self):
        for item in self.frequency:
            self.cAmplitudes = np.append(self.cAmplitudes, abs(self.calculateIntegration(item).real))

    def drawChar(self):
        fiq, ax = plt.subplots()
        ax.plot(self.frequency, self.cAmplitudes)
        ax.grid()
        ax.set_xlabel('Frequency[Hz]')
        ax.set_ylabel('Amplitude')
        plt.show()


t = np.arange(0, 10 + 0.01, 0.01)
x = [20*cmath.sin(2*cmath.pi*30 * i) - 8*cmath.cos(2*cmath.pi*12 * i) for i in t]


test = fourierTransform(x, t)
test.drawChar()

