""" Testing """
# flake8: noqa
import sys
import os
try:
    import shortening_words as sw
except Exception as e:
    sys.path.append(os.path.abspath('.'))
    sys.path.append('/'.join([os.path.abspath('.'), 'shortening_word']))
    import shortening_words as sw


def test_short_one_word():
    """Green to G"""
    resp = sw.shortit("Green", 1)
    assert resp == "G."
