#!/bin/python
import os
import shutil

from contextlib import contextmanager


@contextmanager
def switch_directory(path):
    previous_path = os.getcwd()

    os.chdir(path)
    yield
    os.chdir(previous_path)


def get_parent_directory(path):
    return os.path.split(path)


def get_directory_name(path):
    return os.path.split(path)[-1]


def create_nested_folders(package_name, target):

    # make sure to get back to the original cwd
    with switch_directory(os.getcwd() + '/src'):
        parts = package_name.split('.')

        for ix, part in enumerate(parts):
            if (ix + 1) == len(parts):
                shutil.move(target, part)
            else:
                os.mkdir(part)
                os.chdir(part)


# create nested package folders (src/my.package becomes src/my/package)
package_name = get_directory_name(os.getcwd())

if '.' in package_name:
    create_nested_folders(
        package_name=package_name,
        target=os.path.join(os.getcwd() + '/src', package_name)
    )
