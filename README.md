# Speechful
Sample Google Text to Speech in Python

Before you can run the on e.g. MacOS you need to install sox, one approach is

Get Homebrew an installer app, instructions here http://macappstore.org/sox/

Open Teminal, and run
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
```
then run the sox installer
```
brew install sox
```
clone the sample project in Terminal
```
git clone https://github.com/TheDanishDynamo/speechful/
```
change to the new folder
```
cd speechful
```
install the google speech module
```
pip3 install google_speech
```
Note: You might need to adjust the pip command to match the version of python, via virtual environment or juse pip if you are using python 2.7 (have not tried if this work in 2.7)

Run the script in Terminal
```
python3 hello-speech.py
```
Type some text in text book English and turn the speaker on to list to it



