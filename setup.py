from setuptools import setup, find_packages

setup(
    name='adr-viewer',

    url='https://github.com/mrwilson/adr-viewer',
    version='0.1.0',
    description='A visualisation tool for Architecture Design Records',

    author='Alex Wilson',
    author_email='a.wilson@alumni.warwick.ac.uk',
    license='MIT',

    packages=find_packages(),
    include_package_data=True,
    install_requires=(
        'mistune',
        'bs4',
    ),
    package_data={
        'adr_viewer': ['templates/index.html'],
    },
    entry_points={
        'console_scripts': ['adr-viewer=adr_viewer:main']
    },
)