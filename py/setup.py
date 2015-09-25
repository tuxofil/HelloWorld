import setuptools


setuptools.setup(
    name = 'HelloWorld',
    version = '0.1.0',
    description = 'HelloWorld Python Library',
    author = 'Asylum Inc.',
    packages = setuptools.find_packages('.'),
    provides = ['HelloWorld'],
    requires = [],
    include_package_data = True,
    zip_safe = True,
    license = 'Public Domain',
    platforms = 'Platform Independent',
    classifiers = ['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Natural Language :: English',
                   'Topic :: Software Development'])
