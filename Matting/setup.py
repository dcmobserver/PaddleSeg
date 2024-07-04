# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import find_packages, setup

with open("requirements.txt") as file:
    REQUIRED_PACKAGES = file.read()

setup(
    name="paddle_matting",
    version="1.0",
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(include="ppmatting"),
)
