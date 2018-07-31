Ansible Role: Alertmanager
==========================

[![Build Status](https://travis-ci.org/atosatto/ansible-alertmanager.svg?branch=master)](https://travis-ci.org/atosatto/ansible-alertmanager)
[![Galaxy](https://img.shields.io/badge/galaxy-atosatto.alertmanager-blue.svg?style=flat-square)](https://galaxy.ansible.com/atosatto/alertmanager)

Install and configure Prometheus Alertmanager.

Requirements
------------

An Ansible 2.2 or higher installation.<br />
This role makes use of the Ansible `json_filter` that requires `jmespath` to be installed on the Ansible machine.
See the `requirements.txt` file for further details on the specific version of `jmespath` required by the role.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    alertmanager_release_tag: "latest"

The Prometheus release to be installed.
By default, the latest release published at https://github.com/prometheus/alertmanager/releases.

    alertmanager_user: "alertmanager"
    alertmanager_group: "alertmanager"

Prometheus system user and group.

    alertmanager_install_path: "/opt"

Directory containing the downloaded Alertmanager release artifacts.

    alertmanager_bin_path: "/usr/local/bin"

Directory to which the Alertmanager binaries will be symlinked.

    alertmanager_config_path: "/etc/alertmanager"
    alertmanager_config_file: "alertmanager.yml"

Alertmanager configuration file and directory

    alertmanager_config: {}

YAML dictionary holding the Alertmanager configuration.
The complete Alertmanager configuration reference can be found at
https://prometheus.io/docs/alerting/configuration/.<br/>
**NOTE**: the provided Alertmanager configuration will be merged with the default one defined in `vars/main.yml`.

    alertmanager_templates_path: "{{ alertmanager_config_path }}/templates"
    alertmanager_templates: {}

Alertmanager templates directory and definitions.

    alertmanager_config:
      templates:
        - "{{ alertmanager_templates_path }}/*.tmpl"
    alertmanager_templates:
      "example": "{{ define "slack.myorg.text" }}https://internal.myorg.net/wiki/alerts/{{ .GroupLabels.app }}/{{ .GroupLabels.alertname }}{{ end}}"

The example above, shows how to create the `example.tmpl` in the `alertmanager_templates_path` directory and how to configure Alertmanager to load it.

    alertmanager_listen_address: "127.0.0.1:9093"

The Alertmanager WebServer listen ip address and port.<br/>
**NOTE**: the Alertmanager metrics will be available at `{{ alertmanager_listen_address }}/metrics`.

    alertmanager_storage_path: "/var/lib/alertmanager"
    alertmanager_storage_retention: "120h"

Directory used to store Alertmanager's notification states and silences.
By default, the old data will be deleted after 120 hours.

    alertmanager_log_level: "info"

Alertmanager deamon log verbosity level.

    alertmanager_additional_cli_args: ""

Additional command-line arguments to be added to the Alertmanager service unit.
For the complete refence of the available CLI arguments please refer to the output
of the `alertmanager --help` command.

Dependencies
------------

None.

Example Playbooks
-----------------

    $ cat playbook.yml
    - name: "Install and configure Prometheus Alertmanager"
      hosts: all
      roles:
        - { role: atosatto.alertmanager }

Testing
-------

Tests are automated with [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ pip install tox

To test all the scenarios run

    $ tox

To run a custom molecule command

    $ tox -e py27-ansible23 -- molecule test -s alertmanager-latest

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
