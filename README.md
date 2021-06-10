# 🌴 Valarpy

[![Version status](https://img.shields.io/pypi/status/valarpy?label=status)](https://pypi.org/project/valarpy)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python version compatibility](https://img.shields.io/pypi/pyversions/valarpy?label=Python)](https://pypi.org/project/valarpy)
[![Version on GitHub](https://img.shields.io/github/v/release/dmyersturnbull/valarpy?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/valarpy/releases)
[![Version on PyPi](https://img.shields.io/pypi/v/valarpy?label=PyPi)](https://pypi.org/project/valarpy)
[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/valarpy/Build%20&%20test?label=Tests)](https://github.com/dmyersturnbull/valarpy/actions)
[![Documentation status](https://readthedocs.org/projects/valarpy/badge)](https://valarpy.readthedocs.io/en/stable/)
[![Coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/valarpy/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/valarpy?branch=main)
[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/d09d2fe2feec87da1816/maintainability)](https://codeclimate.com/github/dmyersturnbull/valarpy/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/valarpy/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/valarpy/?branch=main)
[![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-Tyrannosaurus-0000ff.svg)](https://github.com/dmyersturnbull/tyrannosaurus)

Python code to talk to [Valar 🌲](https://github.com/dmyersturnbull/valar-schema).
There is more documentation available in the Valar readme.
[See the docs 📚](https://valarpy.readthedocs.io/en/stable/).

### 🔨 Usage

```python
import valarpy

with valarpy.for_write() as model:
  print(list(model.Refs.select()))
```

An example connection config file:

```json
{
  "port": 3306,
  "user": "kaletest",
  "password": "kale123",
  "database": "valartest",
  "host": "127.0.0.1"
}
```

### 🍁 Contributing

[New issues](https://github.com/dmyersturnbull/valarpy/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/valarpy/blob/master/CONTRIBUTING.md).
Generated with [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).
