import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

fileName = "prueba.wav"
spf = wave.open(fileName, "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "int16")
startFonema = 15400
endFonema = 16000
fonema = signal[startFonema:endFonema] #segon de 0.77 a 0.8
tempsFonema = range(startFonema, endFonema)
senyalFonema = np.column_stack((fonema, tempsFonema))


# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

plt.figure(1)
plt.title(fileName)
plt.xlabel("Mostres de: "+str(startFonema)+" a "+str(endFonema)+" de: "+str(startFonema/20000)+" a "+str(endFonema/20000)+ "s")
plt.ylabel("Senyal")
plt.plot(fonema)
plt.show()