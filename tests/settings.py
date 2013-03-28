DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
SECRET_KEY = 'secret'
INSTALLED_APPS = (
    'django_nose',
)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = (
    'stopwatch',
    '--verbosity=2',
    '--nologcapture',
    '--with-doctest',
    '--with-coverage',
    '--cover-package=stopwatch',
    '--cover-erase',
)
