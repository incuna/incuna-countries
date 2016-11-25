from setuptools import find_packages, setup


version = '1.1.1'


setup(
    name='incuna-countries',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Countries model and fixtures.',
    author='Incuna Ltd',
    author_email='dev@incuna.com',
    url='http://incuna.com/',
)
