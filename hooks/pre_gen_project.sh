#!/bin/bash
set +xe

if [[ -z $(which pre-commit) ]]; then
    echo "installing pre-commit ......"
    pip3 install pre-commit
else
    echo "pre-commit installed"
fi
