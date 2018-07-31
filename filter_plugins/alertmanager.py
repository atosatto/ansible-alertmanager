"""Prometheus Jinja2 filters"""
import re


AM_SYSTEM =  {
    'Linux': 'linux',
    'Darwin': 'darwin',
    'FreeBSD': 'freebsd',
    'NetBSD': 'netbsd',
    'OpenBSD': 'openbsd'
}

AM_ARCHITECTURE = {
    'x86_64': 'amd64',
    'i386': '386',
    'armv6l': 'armv6',
    'armv7l': 'armv7'
}


def alertmanager_release_build(hostvars, promrelease):

    architecture = hostvars['ansible_architecture']
    system = hostvars['ansible_system']
    version = re.sub('^v(.*)$', '\\1', promrelease)

    return 'alertmanager-' + version + '.' + AM_SYSTEM[system] + '-' + AM_ARCHITECTURE[architecture]


class FilterModule(object):


    def filters(self):
        return {
            'alertmanager_release_build': alertmanager_release_build
        }
