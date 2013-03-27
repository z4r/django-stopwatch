from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
DEFAULT_KEYBUILDER = 'stopwatch.keybuilders.RestApiKeyBuilder'
DEFAULT_BACKENDS = ('stopwatch.backends.StatsDStopWatchBackend', )


def get_keybuilder():
    keybuilder_path = getattr(settings, 'STOPWATCH_KEYBUILDER', DEFAULT_KEYBUILDER)
    try:
        kb_module, kb_classname = keybuilder_path.rsplit('.', 1)
    except ValueError:
        raise ImproperlyConfigured('%s isn\'t a stopwatch keybuilder module' % keybuilder_path)
    try:
        mod = import_module(kb_module)
    except ImportError as e:
        raise ImproperlyConfigured('Error importing stopwatch keybuilder %s: "%s"' % (kb_module, e))
    try:
        kb_class = getattr(mod, kb_classname)
    except AttributeError:
        raise ImproperlyConfigured('stopwatch keybuilder: module "%s" does not define a "%s" class' % (kb_module, kb_classname))
    return kb_class()


def get_backends():
    backends = []
    for backend_path in getattr(settings, 'STOPWATCH_BACKENDS', DEFAULT_BACKENDS):
        try:
            b_module, b_classname = backend_path.rsplit('.', 1)
        except ValueError:
            raise ImproperlyConfigured('%s isn\'t a stopwatch backend module' % backend_path)
        try:
            mod = import_module(b_module)
        except ImportError as e:
            raise ImproperlyConfigured('Error importing stopwatch backend %s: "%s"' % (b_module, e))
        try:
            b_class = getattr(mod, b_classname)
        except AttributeError:
            raise ImproperlyConfigured('stopwatch backend: module "%s" does not define a "%s" class' % (b_module, b_classname))
        backends.append(b_class())
    return backends
