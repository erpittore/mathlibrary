from setuptools import setup, find_packages

classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
]

setup(
        name = 'Die erste kalkulator',
        version= '0.0.1',
        description = 'Library',
        Long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
        url='',
        author= 'Romeo Manzanares',
        author_email= 'alexandermanzanares6@gmail.com',
        License= 'MIT',
        classifiers=classifiers,
        keywords='calculator',
        packages= find_packages(),
        install_requires= ['']
)



















