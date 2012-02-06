from setuptools import setup, find_packages

from countries import get_version


setup(
    name = 'incuna-countries',
    packages = find_packages(),
    include_package_data=True,
    version = get_version(),
    description = 'Countries model and fixtures.',
    author = 'Incuna Ltd',
    author_email = 'dev@incuna.com',
    url = 'http://incuna.com/',
)

