# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:26:01 2021

@author: JAB
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from scipy import signal

ECG = loadmat("D:/BioDATA/a01m.mat")

x = (ECG["val"]-0)/200
x = np.transpose(x)

# Determinar la escala de tiempo
fs = 100
ts = 1/fs
tn = np.linspace(0, len(x), len(x))*ts
plt.plot(tn,x)
plt.show 

# ================== FILTRO DIGITAL =====================================
# Coeficientes  
a = [1]
b = [-0.027778203,-0.018773992,-0.006689165,0.006805006,0.019766978,0.030273069,0.036711232,0.038034443,0.033933038,0.024897289,0.012158356,-0.002485263,-0.016930496,-0.029082063,-0.037166594,0.96,-0.037166594,-0.029082063,-0.016930496,-0.002485263,0.012158356,0.024897289,0.033933038,0.038034443,0.036711232,0.030273069,0.019766978,0.006805006,-0.006689165,-0.018773992,-0.027778203]

# Ingreso y evaluación de la señal al filtro
y = signal.lfilter(b, a, x)

# Visualización de la entrada y salida al filtro 
fig, axs = plt.subplots(2, sharex=True)
axs[0].stem(x[:200], linefmt='b', markerfmt='.k', use_line_collection=True)
axs[1].stem(y[:200], linefmt='b', markerfmt='.k', use_line_collection=True)
axs[0].grid(color='grey', linestyle='--', linewidth=0.5)
axs[0].set(ylabel="x[n]")
axs[0].set_title('Entrada al filtro digital, x[n]')
axs[1].grid(color='grey', linestyle='--', linewidth=0.5)
axs[1].set(ylabel="y[n]")
axs[1].set_title('Salida del filtro digital, y[n]')
plt.xlabel("n")
plt.tight_layout(pad=2, w_pad=0, h_pad=0)




