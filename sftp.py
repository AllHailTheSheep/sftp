import pysftp

def sftp_put(host, username, password, local_path, remote_path):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host, username=username, password=password) as sftp:
        sftp.put(local_path, remote_path)
        sftp.close()

def sftp_get(host, username, password, remote_path, local_path):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host, username=username, password=password) as sftp:
        sftp.get(remote_path, local_path)
        sftp.close()
