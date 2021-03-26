# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:43:03 2021

@author: JAB
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


ECGreal = pd.read_csv('601examen04.csv')

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