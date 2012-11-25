from setuptools import setup, find_packages

setup(
    name='vishnje',
    scripts=[
        'scripts/demo.py',
        ],
    include_package_data=True,
    packages=find_packages(),
    install_requires=(
        'python>=3.0',
        'CherryPy==3.2.2',
        ))
