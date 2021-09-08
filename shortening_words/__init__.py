from .shortening import Shortening_Words as sw
from ._version import get_versions

def shortit(word, length):
    return sw(words=word,max_len=length).phrase

__version__ = get_versions()['version']
del get_versions

from . import _version
__version__ = _version.get_versions()['version']
