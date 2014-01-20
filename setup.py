import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Digitacion",
    version="0.1.0",
    url='',
    license='GPL V. 3',
    description="Digitacion de planillas",
    long_description=read('README.md'),

    author='Herald Olivares',
    author_email='heraldmatias.oz@gmail.com',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=['setuptools', 'django'],

    classifiers=[
        'Development Status :: Production',
        'Framework :: Django',
        'Intended Audience :: Public',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Statics',
        'Topic :: Internet :: WWW/HTTP',
    ],

    include_package_data=True,
    zip_safe=False,
)
