import sys
from setuptools import setup

entry_points = {
    'console_scripts': [
        # knossos related
        'cyclegan = cyclegan_tensorflow.main:main',
    ]
}
install_requires = []
setup(
    name='cyclegan_tensorflow',
    author='xhujoy',
    packages=['cyclegan_tensorflow'],
    entry_points=entry_points,
    include_package_data=True,
    version='1.0',
    description='',
    keywords=[],
    install_requires=install_requires,
)