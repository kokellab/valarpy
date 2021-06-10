# Changelog for valarpy

Adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [4.x.0] - unreleased

## [3.x.0] - unreleased

### Fixed:
- Bumped some dev deps and improved build

## [3.0.0] - 2021-02-06

### Added:

- Functions `atomic` and `rolling_back`

### Changed:

- `autorollback` is set to `True`
- INSERT, UPDATE, and DELETE queries fail unless `enable_write` is called
- The path search lists `.sauronlab` instead of `.chemfish`

### Fixed:

- Improved build
- Docs

## [2.2.0] - 2020-08-26

### Fixed:

- `submission_statuses` was incompatible with the actual database

## [2.1.0] - 2020-08-25

### Fixed:

- Incompatibility with real database
- Improved connection code
- Inflexible dependency version ranges
- Poor code separation: moved general code from `model.py` to `metamodel.py`

### Removed:

- `DagsToCreate` and `GeneticConstructs`, which were invalid

### Added:

- `new_model` and `opened` context managers
- Test that checks each model class
- Support for `.chemfish/connection.json`
- Better main method, useful for testing with the active db

## [2.0.0] - 2020-08-14

### Changed:

- Build infrastructure and code organization.
