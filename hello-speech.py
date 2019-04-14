from google_speech import Speech

while True:
    print("Text:")
    text = input()
    speech = Speech(text, 'en')
    speech.play() # Remember to turn on speakers