import numpy as np
from numpy.random import rand, randn
from numpy import sqrt
import matplotlib.pyplot as plt
from scipy import special
import math as m

N = 100000 #sample
def Q_func(x):
	erf = special.erfc(x / np.sqrt(2)) / 2
	return erf

SNR = np.array(range(0,12,2))
itr = len(SNR)
ber = [None] * itr #bit error

for n in range(0, itr):
    noise_var = 10**(SNR[n]*(-1)/10)
    snr_log = 10**(SNR[n]/10)
    s = 2*(rand(N)>=0.5)-1
    awgn = 1/sqrt(2*snr_log)*randn(N)
    r = s + awgn
    r_d = 2*(r>=0)-1
    errors = (s!=r_d).sum()
    ber[n] = 1.0 * errors / N
    print('SNR : ', SNR[n])
    print('BER_BPSK : ', ber[n])

EbN0db = np.linspace(0,10,6)
EbN0db = EbN0db.astype(np.int)
EbNo = []
Pe_theory = []

for n in range(len(EbN0db)):
   EbNo.append(m.pow(10,(EbN0db[n]/10)))
   Pe_theory.append(Q_func(np.sqrt(2 * EbNo[n])))

plt.figure()
plt.title('BER performance of BPSK ')
plt.semilogy(EbN0db,Pe_theory,marker='o')
plt.semilogy(EbN0db,ber,marker='o',color='r')
plt.xlabel('Eb/No [dB]')
plt.ylabel('Probability of bit error')

plt.show()




