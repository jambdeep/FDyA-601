import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000, endpoint=True)
f = 20.0 # Frecuencia en Hz
A = 100.0 # Amplitud
s = A * np.sin(2*np.pi*f*t) # Señal

# graficar
plt.plot(t,s)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# TF rápida
fig=plt.figure()
Y = np.fft.fft(s)
plt.plot(Y)

# ¿Hay algo mal?

N = len(Y)/2+1
N = int(N)
Y[N-4:N+3]

# Valores complejos
fig=plt.figure()
plt.plot(np.abs(Y))

# Existe simetría
fig=plt.figure()
plt.plot(np.abs(Y[:N]))

#Los valores no corresponden

dt = t[1] - t[0] # Diferencia en tiempo entre muestras originales
fa = 1.0/dt # Obtener frecuencia (muestreo)
print('dt=%.5fs (Tiempo entre muestras)' % dt)
print('fa=%.2fHz (Frecuencia de muestreo)' % fa)

# Necesitamos crear un vector de eje x, que comienza en 0
# y termine en N (muestras) y se llene con los valores (longitud de la mitad de la señal FFT)
# y llega hasta la frecuencia máxima, que se puede reconstruir. 
# Esta frecuencia es la mitad de la frecuencia de muestreo máxima 
# y se denomina `Frecuencia de Nyquist` 

X = np.linspace(0, fa/2, N, endpoint=True)
X[:4]
fig=plt.figure()
plt.plot(X, np.abs(Y[:N]))
plt.xlabel('Frequencia (Hz)')

# Ahora para la corrección de la escala de amplitud
# debemos obtener 2/N

fig=plt.figure()
plt.plot(X, 2.0*np.abs(Y[:N])/N)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

# ¿Es correcta la figura?


fig=plt.figure()
plt.plot(t,s)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# La TF está hecha para realizarse en señales periodicas, así:
fig=plt.figure()    
plt.plot(t, s, label='Señal 1')
plt.plot(t+t[-1], s, label='Señal 1 otra vez')
plt.xlim(t[-1]-1, t[-1]+1)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

# Para compensar el efecto no deseado se realiza un sistema de ventanas 
# Hay muchas funciones de ventana, como Hamming, Hanning, Blackman, .. ...


hann = np.hanning(len(s))
hamm = np.hamming(len(s))
black= np.blackman(len(s))
fig=plt.figure()  
plt.figure(figsize=(8,3))
plt.subplot(131)
plt.plot(hann)
plt.title('Hanning')
plt.subplot(132)
plt.plot(hamm)
plt.title('Hamming')
plt.subplot(133)
plt.plot(black)
plt.title('Blackman')
plt.tight_layout()


fig=plt.figure() 
plt.plot(t,hann*s)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal con función de ventana Hanning aplicada')

# Aplicar la FFT a esta señal con ventana 

Yhann = np.fft.fft(hann*s)
fig=plt.figure() 
plt.figure(figsize=(7,3))
plt.subplot(121)
plt.plot(t,s)
plt.title('Señal en el dominio del tiempo')
plt.ylim(np.min(s)*3, np.max(s)*3)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.subplot(122)
plt.plot(X, 2.0*np.abs(Yhann[:N])/N)
plt.title('Señal en el dominio de la Frecuencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')

plt.annotate("FFT",
            xy=(0.0, 0.1), xycoords='axes fraction',
            xytext=(-0.8, 0.2), textcoords='axes fraction',
            size=30, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            connectionstyle="arc3,rad=0.2"))
plt.tight_layout()

plt.savefig('FFT.png',bbox_inches='tight', dpi=150, transparent=True)

