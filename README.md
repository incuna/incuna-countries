# Incuna Countries v1.0.3

Add countries support to your application

## Installation

Install Countries with your favourite package manager:

    pip install incuna-countries

Add `countries` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        # other apps
        'countries',
    )

You can now ForeignKey the ```Country``` object from your models.

### Fixtures

Load the default list of contries into your database with loaddata:
   
    python manage.py loaddata default_countries
