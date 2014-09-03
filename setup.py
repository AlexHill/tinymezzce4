import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='TinyMezzCE4',
    version='0.1',
    description='TinyMCE4 integration for Mezzanine',
    license='BSD',
    long_description=read('README.rst'),
    url='https://github.com/alexhill/tinymezzce4',
    author='Alex Hill',
    author_email='alex@hill.net.au',

    packages=find_packages(),
    install_requires=['django>=1.4'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
    ],
)

