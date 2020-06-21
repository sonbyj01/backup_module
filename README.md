# Backup Module
## Description
The objective of this project is to (1) work on my python skill, (2) get some 
interesting project completed, and (3) implement it on my servers and desktop 
because I have not found a fruitful feature application yet...

The project will be built modular-ly (i.e. I can enable/disable syncing between 
Google Storage, AWS, personal back up storage).
 

## Project Structure
backup.py - 'main' python file

**Classes** \
src/SimpleCopy.py - SimpleCopy class \
src/SourceFiles.py - SourceFiles class

## Issues
- [X] nothing works
- [X] back up folder is created but directories are not copied over
until the second time the script runs in SimpleCopy class
- [X] check if there's already a 'records.txt' that exists in **SourceFiles.py**
- [ ] create hash to check integrity of content inside 'records.txt' ? 

## Future Development
- [ ] docker?
- [ ] nice web ui?
- [X] python gui
- [ ] integration with cloud storage service provider
- [ ] compression (zip)