# Speechful
Sample Google Text to Speech in Python

This sample assumes you have python 3 installed.

Before you can run the on e.g. MacOS you need to install sox, one approach is

Get Homebrew, an installer app, instructions here http://macappstore.org/sox/

Open Teminal, and run
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
```
Then run the sox installer
```
brew install sox
```
Clone the sample project in Terminal
```
git clone https://github.com/TheDanishDynamo/speechful/
```
Change to the new folder
```
cd speechful
```
Install the google speech module
```
pip3 install google_speech
```
Run the script in Terminal
```
python3 hello-speech.py
```
Type some text in text book English and turn the speaker on to listen to a female with a google assistant accent



