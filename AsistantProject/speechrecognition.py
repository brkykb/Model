import pyaudio

p = pyaudio.PyAudio()
print(p.get_default_input_device_info())
