import os
import re
from github import Github

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

gh = Github(os.getenv('GITHUB_API_TOKEN', None))
am_last_release = re.sub('^v(.*)$', '\\1', gh.get_repo('prometheus/alertmanager').get_latest_release().tag_name)
am_last_artifact = "alertmanager-" + am_last_release + ".linux-amd64"


def test_alertmanager_binaries(host):

    amd = host.file('/usr/local/bin/alertmanager')
    assert amd.exists
    assert amd.is_symlink
    assert amd.linked_to == '/opt/' + am_last_artifact + '/alertmanager'

    amt = host.file('/usr/local/bin/amtool')
    assert amt.exists
    assert amt.is_symlink
    assert amt.linked_to == '/opt/' + am_last_artifact + '/amtool'


def test_alertmanager_release(host):

    cmd = host.run('/usr/local/bin/alertmanager --version')

    assert 'version ' + am_last_release in (cmd.stdout + cmd.stderr)
