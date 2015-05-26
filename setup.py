import os

from setuptools import setup, find_packages

import sessionprofile


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


readme = read_file('README.rst')
requirements = []
test_requirements = [
    'factory-boy',#==2.5.2',
    'coverage'#==3.7.1'
]

setup(
    name='django-sessionprofile',
    version=sessionprofile.get_version(),
    license='MIT',

    # Packaging
    packages=find_packages(exclude=('tests', 'tests.*', 'examples')),
    install_requires=requirements,
    include_package_data=True,
    extras_require={
        'test': test_requirements,
    },
    tests_require=test_requirements,
    test_suite='runtests.runtests',

    # PyPI metadata
    description='Dump the entire database to xlsx workbook with a sheet per model',
    long_description='\n\n'.join([readme]),
    author='Maykin Media, Sergei Maertens',
    author_email='sergei@maykinmedia.nl',
    platforms=['any'],
    url='https://github.com/maykinmedia/django-sessionprofile',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ]
)
