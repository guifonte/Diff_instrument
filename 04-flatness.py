
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display

x1, fs = librosa.load('./cello_A5.wav', sr=44100)
x2, fs =  librosa.load('./flute_A5.wav', sr=44100)
#x3, fs = librosa.load('./samples/03.wav', sr=44100)
#x4, fs = librosa.load('./samples/04.wav', sr=44100)


# n_fft = amostras para calcular a DFT (>= que win_length)
# hop_length = amostras entre o começo de duas janelas
# win_length = amostras em cada janela
# window = formato da janela no tempo
d1 = librosa.stft(x1, n_fft=2048, hop_length=128, win_length=1024, window='hann')

flat1 = librosa.feature.spectral_bandwidth(S=np.abs(d1), n_fft=2048,\
        hop_length=512)

d2 = librosa.stft(x2, n_fft=2048, hop_length=128, win_length=1024, window='hann')
flat2 = librosa.feature.spectral_bandwidth(S=np.abs(d2), n_fft=2048,\
        hop_length=512)



# y_axis='linear' ou 'log'
plt.figure()
plt.semilogy(flat1.T, label='Spectral flatness')
plt.semilogy(flat2.T, label='Spectral flatness')
plt.legend(['x1', 'x2'])
plt.show()

