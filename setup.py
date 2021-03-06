from setuptools import setup
import todotxtio

setup(
    name='todotxtio',
    version=todotxtio.__version__,
    description='A simple Python module to parse, manipulate and write Todo.txt data',
    long_description='Everything you need to know is located `here <https://epocdotfr.github.io/todotxtio/>`_.',
    url='https://github.com/EpocDotFr/todotxtio',
    author='Maxime "Epoc" G.',
    author_email='contact.nospam@epoc.nospam.fr',
    license='DBAD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    keywords='todotxt todo.txt file parse parser read reader',
    py_modules=['todotxtio'],
    download_url='https://github.com/EpocDotFr/todotxtio/archive/todotxtio-{version}.tar.gz'.format(version=todotxtio.__version__)
)
