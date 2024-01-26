# main.py
import time
import librosa
import soundfile as sf
from denoising_module import removeNoise
from visualization_module import plot_spectrogram, plot_statistics_and_filter

def main():
    signal_audio, sample_rate = librosa.load(r"D:\UNIVERSITY STUFF\6th Semester\Digital Signal Processing\STFT Based Audio Denoising\speech.wav")
    noise_audio, _ = librosa.load(r"D:\UNIVERSITY STUFF\6th Semester\Digital Signal Processing\STFT Based Audio Denoising\noisesig.wav")

    recovered = removeNoise(
        signal_audio, noise_audio, 2, 4, 2048, 2048, 512, 2, 0.95, verbose=False, visual=True
    )

    sf.write("denoisedsignal.wav", recovered, sample_rate)

if __name__ == "__main__":
    main()
