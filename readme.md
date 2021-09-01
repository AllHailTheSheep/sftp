# SFTP
SFTP is a minimalistic client designed for SFTP (although it has other use cases, see below)
## Installation
To clone the repo, run
```bash
git clone https://github.com/AllHailTheSheep/SFTP
```
This will create a new folder in your current directory with the source code.
Then make a new virtual environment and activate it
```bash
cd SFTP
python3 -m venv ./venv/
source venv/bin/activate
```
Then you will be able to run the client as shown below.
Note: you may have to grant run permissions to listener.py by running
```bash
sudo chmod +x listener.py
```
## Usage
When run, listener.py will ask
```Input path to folder to listen in: ```