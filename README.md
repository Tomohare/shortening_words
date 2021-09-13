# Shortening Words

![Main build status](https://github.com/Tomohare/shortening_words/actions/workflows/shortening-actions.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/Tomohare/shortening_words/branch/main/graph/badge.svg?token=DH6O6E8XFL)](https://codecov.io/gh/Tomohare/shortening_words)

Shortening words using 'pyphen' for word hyphenation

# How to use

## Installation

### Using release package

Can be found on the [releases](https://github.com/Tomohare/shortening_words/releases) page.

```bash
$ pip install https://github.com/Tomohare/shortening_words/releases/download/<tag>/shortening-words-<version>-py3-none-any.whl

```

### Using git repository

Make sure that you have the `pyphen` package installed (try `pip install pythen`).

```bash
$ pip install git+https://github.com/Tomohare/shortening_words.git

```

## Example code

```python
import shortening_words as sw

print(sw.shortit("National Census",11, lang="en"))

```

# Limitations

This module does not guarantee the desired length.