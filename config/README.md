# Configuration

Following is the recommended configuration for a development environment.

## Virtual Environment

```bash
cd ~/snlcopyright

# python3 -m pip install --upgrade pip setuptools wheel
/usr/local/bin/python3.7 -m pip install --upgrade pip setuptools wheel

# python3 -m venv autotwin_env  # create a virtual environment
# VS Code docs reference:
# https://code.visualstudio.com/docs/python/environments#_create-a-virtual-environment
/usr/local/bin/python3.7 -m venv .venv  # create a virtual environment

# activate the venv with one of the following:
source .venv/bin/activate # for bash shell
source .venv/bin/activate.csh # for c shell
source .venv/bin/activate.fish # for fish shell
source .venv/bin/Activate.fish # for powershell

python --version  # Python 3.7.9

pip list

Package    Version
---------- -------
pip        20.1.1
setuptools 47.1.0
WARNING: You are using pip version 20.1.1; however, version 22.3.1 is available.
You should consider upgrading via the 'python3.7 -m pip install --upgrade pip' command.
(.venv) ~/snlcopyright>

python -m pip install --upgrade pip
```

## Install `snlcopyright` as a developer

Reference: https://packaging.python.org/en/latest/tutorials/packaging-projects/

```bash
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── your_package_name_here/
│       ├── __init__.py
│       └── example.py
└── tests/
```

Create a `pyproject.toml`, e.g., example `.toml` reference: https://peps.python.org/pep-0621/#example and general setuptools documentation: https://setuptools.pypa.io/en/latest/index.html

Installing from a local source tree, reference:

* https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-a-local-src-tree, and
* development mode: https://setuptools.pypa.io/en/latest/userguide/development_mode.html

```bash
# create an editable install (aka development mode)
(.venv) ~/snlcopyright>
python -m pip install -e .[dev]  # note: `-e .` = `--editable .`
```

At the time of this writing, the current version of `snlcopyright` is shown below.  Your version may be newer.  Post-install package status:

```bash
(.venv) ~/snlcopyright>
pip list
Package            Version Editable project location
------------------ ------- -------------------------
attrs              22.2.0
black              22.10.0
click              8.1.3
coverage           7.1.0
exceptiongroup     1.1.0
flake8             5.0.4
importlib-metadata 4.2.0
iniconfig          2.0.0
mccabe             0.7.0
mypy-extensions    0.4.3
packaging          23.0
pathspec           0.11.0
pip                23.0
platformdirs       2.6.2
pluggy             1.0.0
pycodestyle        2.9.1
pyflakes           2.5.0
pytest             7.2.1
pytest-cov         4.0.0
PyYAML             6.0
setuptools         47.1.0
snlcopyright       0.0.6   /Users/cbh/snlcopyright
tomli              2.0.1
typed-ast          1.5.4
typing_extensions  4.4.0
zipp               3.12.0
```

Deactivate/Reactivate method:  To deactivate any current `venv`:

```bash
deactivate
```

Deactivate/Reactivate method:  To activate the `.venv` virtual environment:

```bash
# activate the venv with one of the following:
source .venv/bin/activate # for bash shell
source .venv/bin/activate.csh # for c shell
source .venv/bin/activate.fish # for fish shell
source .venv/bin/Activate.fish # for powershell
```

Run from the REPL:

```bash
(.venv) python
Python 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08)
[Clang 6.0 (clang-600.0.67)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from snlcopyright import command_line as cl
>>> cl.copyright_version()
snlcopyright version:
'0.0.6'
>>> quit()
```

Run from the command line:

```bash
(.venv) commands
------------
snlcopyright
------------
This is the command line interface help for Sandia National Laboratories snlcopyright Python module.
Available commands:
commands           (this command)
copyright          Appends contents `copyright.txt` contents to .py files in the cwd, recursively.
copyright-info     Describes the installation details.
copyright-show     Echos the `copyright.txt` contents to the terminal.
copyright-version  Prints the semantic verison of the current installation.
```

Run the tests with `pytest`:

```bash
(.venv) pytest -v
==================================================================================================================== test session starts =====================================================================================================================
platform darwin -- Python 3.7.9, pytest-7.2.1, pluggy-1.0.0 -- /Users/cbh/copyright/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/cbh/copyright
plugins: cov-4.0.0
collected 8 items                                                                                           

tests/test_command_line.py::test_commands PASSED                          [ 12%]
tests/test_command_line.py::test_scinfo PASSED                            [ 25%]
tests/test_command_line.py::test_version PASSED                           [ 37%]
tests/test_copyright.py::test_text_block PASSED                           [ 50%]
tests/test_copyright.py::test_copyright_exists PASSED                     [ 62%]
tests/test_copyright.py::test_copyright_create PASSED                     [ 75%]
tests/test_copyright.py::test_modules_list PASSED                         [ 87%]
tests/test_copyright.py::test_copyright_update PASSED                     [100%]

------------================ 8 passed in 0.08s =================================
```

And `pytest-cov` (coverage) with line numbers missing coverage:

```bash
(.venv) pytest --cov=copyright --cov-report term-missing
=============== test session starts ============================================
platform darwin -- Python 3.7.9, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/cbh/copyright
plugins: cov-4.0.0
collected 8 items                                                                                           

tests/test_command_line.py ...                                            [ 37%]
tests/test_copyright.py .....                                             [100%]

---------- coverage: platform darwin, python 3.7.9-final-0 -----------
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
src/snlcopyright/__init__.py             0      0   100%
src/snlcopyright/command_line.py        31      0   100%
src/snlcopyright/copyright_crud.py      44      0   100%
---------------------------------------------------------------
TOTAL                                75      0   100%


================ 8 passed in 0.13s =============================================
```

Success!  The `venv` virtual environment `.venv` has been created, 
and the `snlcopyright` module is now installed and tested.

## Typical Development Cycle

```bash
# develop code
# uninstall the now-outdated developer installation
pip uninstall snlcopyright
# reinstall the module with the newly developed code
pip install -e .[dev]
```

## Modify VS Code if desired

Reference: Enable IntelliSense for custom package locations, https://code.visualstudio.com/docs/python/editing#_enable-intellisense-for-custom-package-locations

Before:

```bash
    "python.autoComplete.extraPaths": [
        "~/python_modules"
    ],
```

After:

```bash
    "python.autoComplete.extraPaths": [
        "~/python_modules",
        "/Applications/Cubit-16.08/Cubit.app/Contents/MacOS"
    ],
    "python.envFile": "${workspaceFolder}/.venv",
```

## Continuous Integration (CI)

Any push to the `main` branch that contains at least one file with a `.py` extension will trigger CI.  The CI tests against the Black code formatter, against `flake8`, and assesses code coverage. 

## First Deployment (manual)

### Git Tag

* Git Tag [reference](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
* View the existing tag (if any):

```bash
$ git tag
v1.0
v2.0

# Create a git tag with the `-a` flag:
$ git tag -a v1.4 -m "my version 1.4"

# Read the tag
$ git show v1.4

# Push the tag
$ git push origin v1.4
```


> *Note:  Naming collisions for module names can occur.  If the module name one has selected is too common or too general, then likely the name is already taken; a new and unique name much be created.  Search [PyPI](https://pypi.org/) to determine if the module name is available.*

### Build

```bash
# Use the latest version of PyPA's build module
$ python -m pip install --upgrade build

# Run from the same directory where pyproject.toml is located
$ python -m build

# Output
# dist/
# ├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
# └── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
```

### Deploy

> *Note: You may need to disconnect from the SNL VPN for this step.*

```bash
# Install twine
$ python -m pip install --upgrade twine

# Run Twine to upload all of the archives under dist/
$ python -m twine upload --repository testpypi dist/*

# Output
# Uploading distributions to https://test.pypi.org/legacy/
# Enter your username: __token__
# Uploading example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
# 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
# Uploading example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
# 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?

# For deployment (non-test)
$ python -m twine upload dist/*
```

## Continuous Deployment (CD)

The `.github/workflows/release.yml` automates the build of a release when a `git push` is specified with a version flag, such as `v1.0`, `v20.15.10`, etc.

## References

* https://github.com/cycjimmy/semantic-release-action
* https://github.com/anirudh2/setup-jl
* https://github.com/marketplace/actions/action-for-semantic-release
* https://github.com/semantic-release/semantic-release
* https://github.com/python-semantic-release/python-semantic-release
* https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/github-actions.html
* https://packaging.python.org/en/latest/tutorials/packaging-projects/
