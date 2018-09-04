import pandas
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
import librosa
import os
import pydub

#name of the two instruments
instr1_name = "flute"
instr2_name = "viola"

#folder initialization
instr1_main_folder = './' + instr1_name + "/"
instr2_main_folder = './' + instr2_name + "/"
instr1_wav_folder = './' + instr1_name + "_wav/"
instr2_wav_folder = './' + instr2_name + "_wav/"

#get the lists of mp3 files
instr1_files = os.listdir(instr1_main_folder)
instr2_files = os.listdir(instr2_main_folder)

#filter the lists of files
instr1 = [k for k in instr1_files if 'very-long' in k]
instr1 += [k for k in instr1_files if '_long_' in k]
instr2 = [k for k in instr2_files if 'pizz-normal' in k]

instr1_len = len(instr1)
instr2_len = len(instr2)
instr1_lst = [None] * instr1_len
instr2_lst = [None] * instr2_len

#clear the old wav files if exists
instr1_wav_list = os.listdir(instr1_wav_folder)
instr2_wav_list = os.listdir(instr2_wav_folder)

for i in range(0,len(instr1_wav_list)):
    os.remove(instr1_wav_folder + instr1_wav_list[i])

for i in range(0,len(instr2_wav_list)):
    os.remove(instr2_wav_folder + instr2_wav_list[i])

print("Samples of " + instr1_name + ":", instr1_len)
print("Samples of " + instr2_name + ":", instr2_len)

#convert from mp3 to wav all the filtered files from instrument 1 and instrument 2 and save
for i in range(0,instr1_len):
    sound = pydub.AudioSegment.from_mp3(instr1_main_folder + instr1[i])
    sound.export(instr1_wav_folder + instr1[i][:-4] + ".wav",format ="wav")

for i in range(0,instr2_len):
    sound = pydub.AudioSegment.from_mp3(instr2_main_folder+ instr2[i])
    sound.export(instr2_wav_folder + instr2[i][:-4] + ".wav",format ="wav")

