from setuptools import find_packages
from setuptools import setup


setup(
    name="my-other-package",
    packages=find_packages(),
    version='1.0.1',
    description="Test",
    install_requires=["my-package @ git+https://github.com/neradha/my-package.git"],
    author="",
    license="",
)
