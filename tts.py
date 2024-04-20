import requests
import simpleaudio

text = input()

key="insert key here"

r = requests.get(f"https://api.voicerss.org/?key={key}&v=John&src={text}&hl=en-us")
print(r.content)
# Extract audio data (assuming data starts after "data" string)
audio_data = r.content[26:]

# Assuming PCM audio format
num_channels = 1
bytes_per_sample = 1
sample_rate = 8000

# playing audio
try:
  play_obj = simpleaudio.play_buffer(audio_data, num_channels, bytes_per_sample, sample_rate)
  play_obj.wait_done()
except Exception as e:
  print(f"Error playing audio: {e}")


