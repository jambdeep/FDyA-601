# -*- coding: utf-8 -*-
"""
Created on Wed May 19 18:40:03 2021

@author: JAB
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# información de muestreo
Fs = ??? # frecuencia de muestreo
T = 1/Fs # periodo de muestreo
t = ??? # segundos de muestreo a visualizar
N = Fs*t # muestras totales

# información de la señal de entrada
freq = ??? # frecuencia de la señal en Hz
omega = 2*np.pi*freq # frecuencia angular
t_vec = np.arange(N)*T # vector con valores en tiempo discreto para graficar
x = np.sin(omega*t_vec) # señal de entrada

plt.stem(t_vec,x)
plt.title('Señal de entrada x[n]')
plt.xlabel("Valores discretos de tiempo")
plt.ylabel("Amplitud")

# ================== FILTRO DIGITAL =====================================
# Coeficientes  
a = [ ??? ]
b = [ ??? ]

# Ingreso y evaluación de la señal al filtro
y = signal.lfilter(b, a, x)

# Visualización de la entrada y salida al filtro 
fig, axs = plt.subplots(2, sharex=True)
axs[0].stem(x, linefmt='b', markerfmt='.k', use_line_collection=True)
axs[1].stem(y, linefmt='b', markerfmt='.k', use_line_collection=True)
axs[0].grid(color='grey', linestyle='--', linewidth=0.5)
axs[0].set(ylabel="x[n]")
axs[0].set_title('Entrada al filtro digital, x[n]')
axs[1].grid(color='grey', linestyle='--', linewidth=0.5)
axs[1].set(ylabel="y[n]")
axs[1].set_title('Salida del filtro digital, y[n]')
plt.xlabel("n")
plt.tight_layout(pad=2, w_pad=0, h_pad=0)




