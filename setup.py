from distutils.core import setup

setup(
    name='hipster',
    url='https://github.com/a2design-company/hipster',
    version='0.1',
    packages = ['hipster'],
    install_requires = ('urllib3'),
    author='Andrew Fatkulin',
    author_email='a.lampcat@gmail.com',
    license='MIT',
    description = "Simple Python library for the HipChat API",
    long_description=open('README.md').read()
)