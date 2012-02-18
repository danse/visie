from setuptools import setup, find_packages

setup(
    name='vishnje',
    include_package_data=True,
    packages=find_packages(),
    entry_points = {
        'console_scripts':[
            'vishnje = vishnje.server:present',
            'vis-tornado = vishnje.tornado:run',
            'vis-line = vishnje.line:run',
            ],
    }
    )
