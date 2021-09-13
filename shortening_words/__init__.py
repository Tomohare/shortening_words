from .shortening import Shortening_Words as sw
from ._version import get_versions
from . import _version


def shortit(word, length, lang):
    return sw(words=word, max_len=length, lang=lang).phrase


__version__ = get_versions()['version']
del get_versions

__version__ = _version.get_versions()['version']
