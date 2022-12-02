import scipy
import streamlit as st

st.markdown("# Select your first sample")
uploaded_file = st.file_uploader("Pick a wave file!", type='wav', key="sample1")

if uploaded_file is not None:
    # We generate byte data from the uploaded sample 1 to store locally
    bytes_data = uploaded_file.getvalue()

    if os.path.exists('cache/sample1.wav'):
        pass
    else:
        with open('cache/sample1.wav', mode='bx') as f:
            f.write(bytes_data)

    # Read the .wav file
    sample_rate, data = wavfile.read('cache/sample1.wav')

    st.markdown('## Check out the sample!')
    audio_file = open("cache/sample1.wav", 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

    # Spectrogram of First sample, First channel
    sample_freq_fs_fc, segment_time_fs_fc, spec_data_fs_fc = scipy.signal.spectrogram(data[:, 0], sample_rate)

    # Spectrogram of First sample, Second channel
    sample_freq_fs_sc, segment_time_fs_sc, spec_data_fs_sc = scipy.signal.spectrogram(data[:, 1], sample_rate)

