# Backup Module
## Description
The objective of this project is to (1) work on my python skill, (2) get some 
interesting project completed, and (3) implement it on my servers and desktop 
because I have not found a fruitful feature application yet...

The project will be built modular-ly (i.e. I can enable/disable syncing between 
Google Storage, AWS, personal back up storage).
 
## Requirements
I'll create a requirements.txt file eventually but most are installed. If you want
to use the GUI though, you'll need PySimpleGUI. 

Like I always say, I recommend you creating a virtual environment before you 
install packages from pip.

```bash
$ pip install pysimplegui
```

## Running Program
This is written in Python3... so get with the program and stop using python2. 
```bash
$ python GUI.py
```

## Project Structure
GUI.py - GUI form to run program

**Classes** \
src/SimpleCopy.py - SimpleCopy class \
src/SourceFiles.py - SourceFiles class

## Issues
- [X] nothing works
- [X] back up folder is created but directories are not copied over
until the second time the script runs in SimpleCopy class
- [X] check if there's already a 'records.txt' that exists in **SourceFiles.py**
- [ ] ~~create hash to check integrity of content inside 'records.txt' ?~~
- [ ] thing crashes when you exit out the pop out window
- [ ] cancel button for pop out window also crashes program

## Tasks at hand
- [X] compression .zip
- [ ] compression .tar.gz

## Future Development
- [ ] docker?
- [ ] nice web ui?
- [X] python gui
- [ ] integration with cloud storage service provider
