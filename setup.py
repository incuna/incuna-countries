from setuptools import setup, find_packages


version = '1.0.3'


setup(
    name = 'incuna-countries',
    packages = find_packages(),
    include_package_data=True,
    version=version,
    description = 'Countries model and fixtures.',
    author = 'Incuna Ltd',
    author_email = 'dev@incuna.com',
    url = 'http://incuna.com/',
)

