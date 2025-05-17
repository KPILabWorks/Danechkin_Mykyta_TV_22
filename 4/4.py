import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.fft import fft, fftfreq

fs = 1000
t = np.arange(0, 1, 1/fs)
signal = (np.sin(2*np.pi*5*t) + 
          0.5*np.sin(2*np.pi*50*t) + 
          0.2*np.random.randn(len(t)))
N = len(signal)
yf = fft(signal)
xf = fftfreq(N, 1/fs)

plt.figure(figsize=(14, 4))
plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.title("Аналіз фур'є")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплітуда")
plt.grid()
plt.show()

widths = np.arange(1, 100)
cwtmatr, freqs = pywt.cwt(signal, widths, 'morl', sampling_period=1/fs)

plt.figure(figsize=(14, 6))
plt.imshow(np.abs(cwtmatr), extent=[0, 1, freqs[-1], freqs[0]], cmap='jet', aspect='auto')
plt.title('Вейвлет')
plt.xlabel('Час (сек)')
plt.ylabel('Частота (Гц)')
plt.colorbar(label='Амплітуда')
plt.show()
