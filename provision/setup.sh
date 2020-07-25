#!/usr/bin/env bash

set +x
ansible-playbook -i inventory/server.ini provision.yml;