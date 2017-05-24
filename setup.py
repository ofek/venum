from setuptools import find_packages, setup

with open('venum/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break

setup(
    name='venum',
    version=version,
    description='Verifiably better, validated Enum',
    long_description=open('README.rst', 'r').read(),
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    maintainer='Ofek Lev',
    maintainer_email='ofekmeister@gmail.com',
    url='https://github.com/ofek/venum',
    download_url='https://github.com/ofek/venum',
    license='MIT',

    keywords=(
        'enum',
        'immutable',
        'functional',
        'data structures',
    ),

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),

    tests_require=['pytest'],

    packages=find_packages(),
)
