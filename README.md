Restic
=========

[![Build Status](https://travis-ci.org/trawiasty/ansible-role-restic.svg?branch=master)](https://travis-ci.org/trawiasty/ansible-role-restic)

Simple ansible role for provisioning restic.

Requirements
------------

- S3-compatible object storage

Role Variables
--------------

See `defaults/main.yml`.

Dependencies
------------

-

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-restic, x: 42 }

License
-------

BSD

Author Information
------------------

[Paweł Tatarczuk](https://trawiasty.github.io)