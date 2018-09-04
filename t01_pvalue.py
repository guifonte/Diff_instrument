import pandas
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import librosa
import os

instr1_name = "flute"
instr2_name = "viola"

instr1_wav_folder = './' + instr1_name + "_wav/"
instr2_wav_folder = './' + instr2_name + "_wav/"

instr1 = os.listdir(instr1_wav_folder)
instr2 = os.listdir(instr2_wav_folder)
instr1_len = len(instr1)
instr2_len = len(instr2)
instr1_lst = [None] * instr1_len
instr1_stft = [None] * instr1_len
instr1_mean = [None] * instr1_len
instr1_stdv = [None] * instr1_len
instr1_flat = [None] * instr1_len
instr2_lst = [None] * instr2_len
instr2_stft = [None] * instr2_len
instr2_mean = [None] * instr2_len
instr2_stdv = [None] * instr2_len
instr2_flat = [None] * instr2_len

print("Samples of " + instr1_name + ":", instr1_len)
print("Samples of " + instr2_name + ":", instr2_len)

for i in range(0,instr1_len):
    instr1_lst[i], fs = librosa.load(instr1_wav_folder + instr1[i], sr=44100)
    instr1_stft[i] = librosa.stft(instr1_lst[i], n_fft=2048, hop_length=128, win_length=1024, window='hann')
    instr1_flat[i] = librosa.feature.spectral_flatness(S=np.abs(instr1_stft[i]), n_fft=2048,hop_length=512)
    instr1_mean[i], instr1_stdv[i] = np.mean(instr1_flat[i]), np.std(instr1_flat[i])

for i in range(0,instr2_len):
    instr2_lst[i], fs = librosa.load(instr2_wav_folder + instr2[i], sr=44100)
    instr2_stft[i] = librosa.stft(instr2_lst[i], n_fft=2048, hop_length=128, win_length=1024, window='hann')
    instr2_flat[i] = librosa.feature.spectral_flatness(S=np.abs(instr2_stft[i]), n_fft=2048,hop_length=512)
    instr2_mean[i], instr2_stdv[i] = np.mean(instr2_flat[i]), np.std(instr2_flat[i])

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


means_instr2 = np.mean ( np.array(instr2_mean))
stds_instr2 =  np.std ( np.array(instr2_stdv))
means_instr1 = np.mean ( np.array(instr1_mean))
stds_instr1 =  np.std ( np.array(instr1_stdv))

#means_crash = np.mean ( np.array( [scx0, scx1] ))
#stds_crash =  np.std ( np.array( [scx0, scx1] ))
#means_horn = np.mean ( np.array( [scx2, scx3] ))
#stds_horn =  np.std ( np.array( [scx2, scx3] ))


t, p = st.ttest_ind_from_stats(means_instr2, stds_instr2, instr2_len,\
                               means_instr1, stds_instr1, instr1_len)
print(means_instr2, means_instr1)
print(stds_instr2, stds_instr1)
print("P-value", p)