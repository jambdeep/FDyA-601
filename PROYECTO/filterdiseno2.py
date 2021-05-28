# -*- coding: utf-8 -*-
"""
Created on Wed May 26 18:47:00 2021

@author: JAB
"""

import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


# Requerimientos del filtro
order = 6
fs = 30.0       # frecuencia de muestreo, Hz
cutoff = 3.667  # frecuencia de corte deseada del filtro, Hz


# Obtención de coeficientes
b, a = butter_lowpass(cutoff, fs, order)

# Gráfica de respuesta en frecuencia.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Respuesta en Frecuencia del Filtro Pasabajos")
plt.xlabel('Frecuencia [Hz]')
plt.grid()


# Demostración del filtro
T = 5.0         # segundos
n = int(T * fs) # total de muestras
t = np.linspace(0, T, n, endpoint=False)
# Datos con ruido, se quiere recuperar la señal de 1.2Hz
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filtrado de datos 
y = butter_lowpass_filter(data, cutoff, fs, order)

plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='señal con ruido')
plt.plot(t, y, 'g-', linewidth=2, label='datos filtrados')
plt.xlabel('Tiempo [seg]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()