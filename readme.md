# SFTP

SFTP is a minimalistic client in Python 3 designed for SFTP (although it has other use cases, see below)
## Installation

To clone the repo, run

```bash
git clone https://github.com/AllHailTheSheep/SFTP
```

This will create a new folder in your current directory with the source code.
Then make a new virtual environment and activate it:

```bash
cd SFTP
python3 -m venv ./venv/
source venv/bin/activate
pip3 install -r 'requirements.txt'
```
Then you will be able to run the client as shown below.

Note: you may have to grant run permissions to listener.py by running

```bash
sudo chmod +x listener.py
```
## Listener

When run, listener.py will ask for a path to the folder to watch. From this point forward, any images placed in that directory or any of its subdirectories will be brought up onscreen in your native photo viewing application. This has been tested on Windows 10 and Ubuntu and *should* work on any Mac OS or other Linux distros. This, obviously, has nothing to do with SFTP and is also super handy for any other program that generates images.

## Python Functions

### sftp.py
IMPORTANT: YOU MUST HAVE ESTABLISHED PREVIOUS SSH CONNECTIONS BOTH WAYS FOR THESE TO WORK
sftp.py contains two functions: `sftp_put()` and `sftp_get()`.
The parameters for `sftp_put()` are as follows:
    host: the IP or hostname of the computer to pull a file from.
    username: the username on the host to login as.
    password: the password of the username to login with. it is suggested to store this in an untracked file, as to not expose any passwords in plaintext onscreen.
    local_path: path of the file to push on the local machine.
    remote_path: the remote path to pull from.
The parameters for `sftp_get()` are as follows:
    host: the IP or hostname of the computer to pull a file from.
    username: the username on the host to login as.
    password: the password of the username to login with. it is suggested to store this in an untracked file, as to not expose any passwords in plaintext onscreen.
    remote_path: the remote path to pull from.
    local_path: path to copy the file to on local machine.

### uttils.py
uttils.py only contains one function, `getImagesInFolder()`. It has one parameter, `dir`, which is the folder for which to scan. It searches subdirectories as well, and returns a list containing every path that ends in `.jpg`, `.jpeg`, or `.png`.

# Copyright
Released under the MIT license. See `LICENSE.txt` for full terms.

