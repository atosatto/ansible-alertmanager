import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_alertmanager_config(host):

    d = host.file('/etc/alertmanager/')
    assert d.exists
    assert d.user == 'alertmanager'
    assert d.group == 'alertmanager'
    assert oct(d.mode) == '0755'

    f = host.file('/etc/alertmanager/alertmanager.yml')
    assert f.exists
    assert f.user == 'alertmanager'
    assert f.group == 'alertmanager'
    assert oct(f.mode) == '0640'

    host.run("/usr/local/bin/amtool check-config /etc/alertmanager/alertmanager.yml").rc == 0


def test_alertmanager_tsdb(host):

    d = host.file('/var/lib/alertmanager/')
    assert d.exists
    assert d.user == 'alertmanager'
    assert d.group == 'alertmanager'
    assert oct(d.mode) == '0755'


def test_alertmanager_service(host):

    s = host.service('alertmanager')
    assert s.is_running
    assert s.is_enabled


def test_alertmanager_webserver(host):

    host.socket("tcp://127.0.0.1:9093").is_listening
