
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import pydub

sound = pydub.AudioSegment.from_mp3("./flute/flute_A5_05_forte_normal.mp3")
sound.export("./flute_A5.wav",format ="wav")
sound = pydub.AudioSegment.from_mp3("./cello/cello_A5_05_forte_arco-normal.mp3")
sound.export("./cello_A5.wav",format ="wav")

x1, fs = librosa.load('./cello_A5.wav', sr=44100)
x2, fs =  librosa.load('./flute_A5.wav', sr=44100)
#x3, fs = librosa.load('./samples/03.wav', sr=44100)
#x4, fs = librosa.load('./samples/04.wav', sr=44100)


# n_fft = amostras para calcular a DFT (>= que win_length)
# hop_length = amostras entre o começo de duas janelas
# win_length = amostras em cada janela
# window = formato da janela no tempo
d1 = librosa.stft(x1, n_fft=2048, hop_length=128, win_length=1024, window='hann')
D1 = librosa.amplitude_to_db(np.abs(d1), ref=np.max)


d2 = librosa.stft(x2, n_fft=2048, hop_length=128, win_length=1024, window='hann')
D2 = librosa.amplitude_to_db(np.abs(d2), ref=np.max)


# y_axis='linear' ou 'log'
plt.figure()
plt.subplot(2, 1, 1)
librosa.display.specshow(D1, sr=fs, y_axis='log', x_axis='time')
plt.subplot(2, 1, 2)
librosa.display.specshow(D2, sr=fs, y_axis='log', x_axis='time')

plt.show()

