import matplotlib.pyplot as plt
import numpy as np
import h5py

# 画频谱图
f = h5py.File('F:/PyQT5学习/01.hdf5', 'r')
a = f['X'][:]
b = f['Y'][:]
c = f['Z'][:]
point_num = 1024
x = np.linspace(0, 5, point_num)
y1 = a[0][:, 0][:point_num]
y2 = a[0][:, 1][:point_num]
fs = 2000;
y = y1 + y2 * 1j
NFFT = 256  # the length of the windowing segments
dt = 0.0005
Fs = int(1.0 / dt)  # the sampling frequency

fig, ax=plt.subplots()
# Pxx, freqs, bins, im = plt.specgram(x, NFFT=NFFT, Fs=Fs,noverlap=200)
Pxx, freqs, bins, im = plt.specgram(x, NFFT=NFFT, Fs=Fs,mode='psd')
position=fig.add_axes([0.15, 0.05, 0.7, 0.03])#位置[左,下,右,上]
plt.colorbar(im,cax=position,orientation='horizontal')#方向
plt.show()
