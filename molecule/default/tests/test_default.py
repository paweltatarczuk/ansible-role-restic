import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('instance')


def test_services(host):
    assert host.service('backup.timer').is_running is True


def test_backup(host):
    result = host.ansible('command', '/usr/local/bin/backup', check=False)
    assert result['rc'] == 0
