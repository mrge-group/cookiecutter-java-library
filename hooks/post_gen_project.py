#!/usr/bin/env python

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':
    if '{{ cookiecutter.open_source }}' != 'y':
        remove_file('LICENSE')
