from setuptools import setup

setup(
    name='nameserver',
    version = '0.0.1',
    author = 'Saionara',
    description = '',
    license= 'GNU',
    install_requires ='flask',
    entry_points = {
        'console_scripts':[
            'nameserver = main:main'
        ]
    }
)

