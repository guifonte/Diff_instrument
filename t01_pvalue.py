import pandas
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import librosa
import os

flute = os.listdir('./flute_wav/')
viola = os.listdir('./viola_wav/')
flute_len = len(flute)
viola_len = len(viola)
flute_lst = [None] * flute_len
flute_stft = [None] * flute_len
flute_mean = [None] * flute_len
flute_stdv = [None] * flute_len
flute_flat = [None] * flute_len
viola_lst = [None] * viola_len
viola_stft = [None] * viola_len
viola_mean = [None] * viola_len
viola_stdv = [None] * viola_len
viola_flat = [None] * viola_len

print("Samples of flute:", flute_len)
print("Samples of viola", viola_len)

for i in range(0,flute_len):
    flute_lst[i], fs = librosa.load('./flute_wav/' + flute[i], sr=44100)
    flute_stft[i] = librosa.stft(flute_lst[i], n_fft=2048, hop_length=128, win_length=1024, window='hann')
    flute_flat[i] = librosa.feature.spectral_flatness(S=np.abs(flute_stft[i]), n_fft=2048,hop_length=512)
    flute_mean[i], flute_stdv[i] = np.mean(flute_flat[i]), np.std(flute_flat[i])

for i in range(0,viola_len):
    viola_lst[i], fs = librosa.load('./viola_wav/' + viola[i], sr=44100)
    viola_stft[i] = librosa.stft(viola_lst[i], n_fft=2048, hop_length=128, win_length=1024, window='hann')
    viola_flat[i] = librosa.feature.spectral_flatness(S=np.abs(viola_stft[i]), n_fft=2048,hop_length=512)
    viola_mean[i], viola_stdv[i] = np.mean(viola_flat[i]), np.std(viola_flat[i])

#d0 = librosa.stft(x1, n_fft=2048, hop_length=128, win_length=1024, window='hann')
#centX = librosa.feature.spectral_centroid(S=np.abs(d0), n_fft=2048,\
#                hop_length=512)
#mcx0, scx0 = np.mean(centX), np.std(centX)

#d0 = librosa.stft(x2, n_fft=2048, hop_length=128, win_length=1024, window='hann')
#centX = librosa.feature.spectral_centroid(S=np.abs(d0), n_fft=2048,\
#                hop_length=512)
#mcx1, scx1 = np.mean(centX), np.std(centX)

#d0 = librosa.stft(y1, n_fft=2048, hop_length=128, win_length=1024, window='hann')
#centX = librosa.feature.spectral_centroid(S=np.abs(d0), n_fft=2048,\
#                hop_length=512)
#mcx2, scx2 = np.mean(centX), np.std(centX)

#d0 = librosa.stft(y2, n_fft=2048, hop_length=128, win_length=1024, window='hann')
#centX = librosa.feature.spectral_centroid(S=np.abs(d0), n_fft=2048,\
#                hop_length=512)
#mcx3, scx3 = np.mean(centX), np.std(centX)


means_viola = np.mean ( np.array(viola_mean))
stds_viola =  np.std ( np.array(viola_stdv))
means_flute = np.mean ( np.array(flute_mean))
stds_flute =  np.std ( np.array(flute_stdv))

#means_crash = np.mean ( np.array( [scx0, scx1] ))
#stds_crash =  np.std ( np.array( [scx0, scx1] ))
#means_horn = np.mean ( np.array( [scx2, scx3] ))
#stds_horn =  np.std ( np.array( [scx2, scx3] ))


t, p = st.ttest_ind_from_stats(means_viola, stds_viola, viola_len,\
                               means_flute, stds_flute, flute_len)
print(means_viola, means_flute)
print(stds_viola, stds_flute)
print("P-value", p)