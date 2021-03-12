# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:22:32 2021
@author: JAB
"""

import numpy as np
import matplotlib.pyplot as plt


t =np.arange(0,1,0.001)
frec_1 = 50 # Frecuencia en Hz
frec_2 = 120 # Frecuencia en Hz
signal_limpia = np.sin(2*np.pi*frec_1*t) + np.sin(2*np.pi*frec_2*t) # Señal
signal_ruido = signal_limpia + 2.5*np.random.randn(len(t))


fig=plt.figure()
plt.plot(t,signal_limpia,color='k',LineWidth=2,label='Limpia')
plt.xlim(t[0],t[-1])
plt.legend()
fig=plt.figure()
plt.plot(t,signal_ruido,color='r',LineWidth=1.5,label='Ruidosa')
plt.xlim(t[0],t[-1])
plt.legend()

fig=plt.figure()
plt.plot(t,signal_ruido,color='r',LineWidth=1.5,label='Ruidosa')
plt.plot(t,signal_limpia,color='k',LineWidth=2,label='Limpia')
plt.xlim(t[0],t[-1])
plt.legend()


N = len(t)
TDFfast = np.fft.fft(signal_ruido,N)                     
PSD = (np.abs(TDFfast)*np.abs(TDFfast))/N
frecuencias = np.arange(N)           
Mitad = np.arange(1,np.floor(N/2),dtype='int') 

indices = PSD > 100       
PSD_mod = PSD * indices  
TDFfast_mod = indices * TDFfast     
signal_filtrada = np.fft.ifft(TDFfast_mod) 

fig=plt.figure()
plt.plot(t,signal_limpia,color='k',LineWidth=1.5,label='Limpia')
plt.xlim(t[0],t[-1])
plt.legend()
fig=plt.figure()
plt.plot(t,signal_filtrada,color='b',LineWidth=2,label='Filtrada')
plt.xlim(t[0],t[-1])
plt.legend()


fig=plt.figure()
plt.plot(t,signal_limpia,color='k',LineWidth=1.5,label='Limpia')
plt.plot(t,signal_filtrada,color='b',LineWidth=2,label='Filtrada')
plt.xlim(t[0],t[-1])
plt.legend()

fig=plt.figure()
plt.plot(frecuencias[Mitad],PSD[Mitad],color='r',LineWidth=2,label='Ruidosa')
plt.plot(frecuencias[Mitad],PSD_mod[Mitad],color='b',LineWidth=1.5,label='Limpia')
plt.xlim(frecuencias[Mitad[0]],frecuencias[Mitad[-1]])
plt.legend()
