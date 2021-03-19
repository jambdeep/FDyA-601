# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:23:37 2021

@author: JAB
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ECGreal = pd.read_csv('ekg.csv')

#Obtener la frecuencia de muestreo
print('La frecuencia de muestreo es: ')
samplingFreq = 1/(ECGreal['Time (s)'][1]-ECGreal['Time (s)'][0])
print(samplingFreq)


# Gráfica de la Señal en el dominio del tiempo
plt.plot(ECGreal['Time (s)'],ECGreal['Channel 1 (V)'])

# Dominio de la frecuencia
ekgData = ECGreal['Channel 1 (V)'].values
fftData = np.abs(np.fft.fft(ekgData))
fftLen = int(len(fftData)/2)
freqs = np.linspace(0,samplingFreq/2, fftLen )

# Gráfica de la Señal en el dominio de la frecuencia
plt.figure()
plt.plot( freqs, fftData[0:fftLen] )

# Acercamiento al rango de 0 a 200Hz
plt.figure()
plt.plot( freqs[0:400], fftData[0:400] )

# FILTRADO DIGITAL
# Uso de un filtro IIR para eliminar los 50Hz
from scipy import signal
sos = signal.iirfilter(17, [49, 51], rs=60, btype='bandstop',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos, 2000, fs=2000)

# Gráfica de la respuesta del filtro IIR
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Respuesta del filtro Chebyshev Tipo II (filtro notch)')
ax.set_xlabel('Frecuencia [Hz]')
ax.set_ylabel('Amplitud [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()

## Filtrado del ruido de 50Hz
ekgFiltered = signal.sosfilt(sos, ekgData)

# Gráfica de la Señal filtrada en el dominio del tiempo
plt.plot(ECGreal['Time (s)'],ekgFiltered)

# Dominio de la frecuencia
fftData = np.abs( np.fft.fft(ekgFiltered) )
fftLen = int(len(fftData) / 2)
freqs = np.linspace(0,samplingFreq/2, fftLen )

# Gráfica de la Señal filtrada en el dominio de la frecuencia
plt.figure()
plt.plot( freqs, fftData[0:fftLen] )
plt.figure()
# Acercamiento al rango de 0 a 200Hz (señal filtrada)
plt.plot( freqs[0:400], fftData[0:400] )

# Gráfica de la respuesta de un segundo filtro IIR
sos2 = signal.iirfilter(17, [0.5, 200], rs=60, btype='bandpass',
                        analog=False, ftype='cheby2', fs=4000,
                        output='sos')
w, h = signal.sosfreqz(sos2, 2000, fs=2000)

# Gráfica de la respuesta del segundo filtro IIR
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.semilogx(w, 20 * np.log10(np.maximum(abs(h), 1e-5)))
ax.set_title('Respuesta del filtro Chebyshev Tipo II (elimina altas frecuencias)')
ax.set_xlabel('Frecuencia [Hz]')
ax.set_ylabel('Amplitud [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()

## Filtrado con los dos filtros (ruido de 50Hz y altas frecuencias)
ekgFiltered2 = signal.sosfilt(sos2, ekgFiltered)

# Gráfica de la Señal original en el dominio del tiempo
plt.plot(ECGreal['Time (s)'],ECGreal['Channel 1 (V)'],label='Sin Filtrar')
# Gráfica de la Señal filtrada (un filtro) en el dominio del tiempo
plt.plot(ECGreal['Time (s)'],ekgFiltered, label='Filtrada 1')
# Gráfica de la Señal filtrada (dos filtros) en el dominio del tiempo
plt.plot(ECGreal['Time (s)'],ekgFiltered2, label='Filtrada 2')

# Promediador
def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'same') / w

# Gráfica de la Señal filtrada (dos filtros) mas promediador en el dominio del tiempo
plt.plot(ECGreal['Time (s)'],moving_average(ekgFiltered2, 100),label='Filtrada 3')
plt.legend()
