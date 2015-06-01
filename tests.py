from scipy.io import wavfile

fps, bowl_sound = wavfile.read('voices/enathu_peyar.wav')
tones = range(-25,25)
transposed = [picthshift(bowl_sound,n) for n in tones]