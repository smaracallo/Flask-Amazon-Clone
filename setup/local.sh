#!/usr/bin/env bash

rm run/core/__init__.py

rm run/core/controllers/*.py

python3 setup/meta/program_init.py

python3 setup/meta/program_controllers.py