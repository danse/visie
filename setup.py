from setuptools import setup, find_packages

setup(
    name='vishnje',
    include_package_data=True,
    packages=find_packages(),
    install_requires='CherryPy',
    entry_points = {
        'console_scripts':[
            'vishnje = vishnje.server:present',
            'vis-tornado = vishnje.tornado:run',
            'vis-line = vishnje.line:run',
            'vis-parallel = vishnje.wrapper:parallel',
            'vis-splom = vishnje.wrapper:splom',
            'vis-crimea_stacked_area = vishnje.wrapper:crimea_stacked_area',
            'vis-zoom = vishnje.wrapper:zoom',
            'vis-marimekko = vishnje.wrapper:marimekko',
            ],
    }
    )
