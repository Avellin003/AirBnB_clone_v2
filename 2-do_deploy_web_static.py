#!/usr/bin/python3
"""
distributes the archive to web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.89.109.87', '100.25.190.21']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ex = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ex))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ex))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ex))
        run('rm -rf {}{}/web_static'.format(path, no_ex))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ex))
        return True
    except:
        return False
