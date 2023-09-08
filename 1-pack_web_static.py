#!/usr/bin/python3
"""the content of the web static folder to be archieved by this func"""
from fabric.api import local
import time


def do_pack():
    """from webstatic folder tgz archieve to be generated"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
