#!/bin/bash

set -xe

git init

pre-commit install

git add .

git commit -m "feat(all): project setup"

git remote add origin git@{{ cookiecutter.code_hosting }}.com:{{ cookiecutter.code_hosting_username }}/{{ cookiecutter.project_name }}.git

git checkout -b develop

echo "    cd {{ cookiecutter.project_name }}"
