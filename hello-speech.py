from google_speech import Speech

while True:
    text = input()
    speech = Speech(text, 'en')
    speech.play() # Remember to turn on speakers