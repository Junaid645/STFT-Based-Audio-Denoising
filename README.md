# STFT-Based-Audio-Denoising
First, we did preprocessing. We loaded the noisy signal and 
the noise reference signal. We performed any necessary 
preprocessing steps such as resampling or normalization.
We then applied the STFT to both the noisy signal and the 
noise reference signal using parameters such as the window 
size, hop length, and FFT bin size. The STFT magnitudes
were converted to a logarithmic scale using the amplitude to-decibel conversion. Then the mean and standard 
deviation of the noise STFT magnitudes across frequency 
bins was computed to estimate the noise characteristics. 

Our next task was to calculate the threshold for noise 
removal based on the mean and standard deviation of the 
noise STFT magnitudes. It was then adjusted by 
multiplying it with a user-defined standard deviation factor.
magnitudes with the noise threshold and finally convolving
the mask with the smoothing filter using FFT convolution to 
reduce artifacts and enhance the denoising effect. The mask 
was then scaled by multiplying it with a user-defined 
proportion decrease factor which defines the extent of noise 
2
removal. A value of 1 implies complete suppression of the 
noisy components whereas a value of 0 means otherwise.
To reconstruct the signal, we multiplied the masked 
STFT magnitudes by the original phase information to retain 
the phase coherence of the signal, and then converted the 
masked STFT back to the time domain using the inverse 
STFT.