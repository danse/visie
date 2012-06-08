from setuptools import setup, find_packages

setup(
    name='vishnje',
    include_package_data=True,
    packages=find_packages(),
    install_requires='CherryPy',
    scripts=[
        'scripts/tornado',
        'scripts/bounded-tornado',
        ],
    entry_points = {
        'console_scripts':[
            'vis-parallel = vishnje:parallel',
            'vis-splom = vishnje:splom',
            'vis-crimea_stacked_area = vishnje:crimea_stacked_area',
            'vis-zoom = vishnje:zoom',
            'vis-marimekko = vishnje:marimekko',
            'vis-bar = vishnje:bar',
            ],
    }
    )
