import numpy as np
import matplotlib.pyplot as plt

n = 500
f_sin = 25.0  # Hz

f = np.arange(0.0, f_sin, f_sin / n)
t = 2 * np.pi * f

y = 1 * np.sin(t)

plt.plot(t, y)
plt.show()

sp = np.fft.fft(y)
freq = np.fft.fftfreq(t.shape[-1]) * n
freq = freq[:n/2]
amp = abs(sp.imag)[:n/2] / (n/2)

plt.plot(freq, amp)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude")
plt.show()
