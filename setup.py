import setuptools

with open('README.md') as f:
    _long_description = f.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='oelint_data',
    version='1.0.3',
    author='Konrad Weihmann',
    author_email='kweihmann@outlook.com',
    description='Data for oelint-adv',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/priv-kweihmann/oelint-data',
    packages=setuptools.find_packages(exclude=('tests',)),
    package_data={
        'oelint_data': ['*.json', '*/*.json'],
    },
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Quality Assurance',
    ],
    python_requires='>=3.9',
)
