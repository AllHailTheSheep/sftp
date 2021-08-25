import pysftp

def sftp_put(host, username, password, local_path, remote_path):
    ''' A function to PUT a file into a remote system over SFTP.
    Users must have already configured and connected SSH on both ends.
    @type host: str
    @param host: the IP or hostname
    @type username: str
    @param username: the username on the host to login as
    @type password: str
    @param password: the password of the username to login with. it is suggested
    to store this in an untracked file, as to not expose any passwords in plaintext onscreen.
    @type local_path: str
    @param local_path: path to the file to push
    @type remote_path: str
    @param remote_path: the remote path to push to on the remore machine'''
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host, username=username, password=password) as sftp:
        sftp.put(local_path, remote_path)
        sftp.close()

def sftp_get(host, username, password, remote_path, local_path):
    ''' A function to GET a file from a remote system over SFTP.
    Users must have already configured and connected SSH on both ends.
    @type host: str
    @param host: the IP or hostname
    @type username: str
    @param username: the username on the host to login as
    @type password: str
    @param password: the password of the username to login with. it is suggested
    to store this in an untracked file, as to not expose any passwords in plaintext onscreen.
    @type remote_path: str
    @param remote_path: the remote path to pull from
    @type local_path: str
    @param local_path: path to copy the file to on local machine'''
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host, username=username, password=password) as sftp:
        sftp.get(remote_path, local_path)
        sftp.close()
