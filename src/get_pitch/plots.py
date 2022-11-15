import librosa
import matplotlib.pyplot as plt
import IPython.display as ipd
import pav_analysis as ev
import soundfile as sf

def plot_zcr(name, audio, sample_rate):
    
    signal, fm = sf.read("prueba.wav")

    info = [i.strip().split() for i in open ("prueba.wav").readLines()]
    zcr = float(3)


    plt.figure(figsize=(8, 1))
    plt.plot(audio)
    plt.gca().set_title(name1)

    plt.show()