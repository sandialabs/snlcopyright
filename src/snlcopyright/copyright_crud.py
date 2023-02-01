"""This module provides Sandia National Laboratories copyright assertion functionality."""

from pathlib import Path
from shutil import copyfile
from typing import List


"""
Plan:  Support most CRUD (create, read, update, delete) operations.

* Create: when an existing .py file lacks the copyright, add the copyright.
* Read: does the .py file already have the copyright (and is it correct).
* Update: perhaps the copyright year or the wording needs updating.
* Delete: Unlikely we need this action, since all .py files need copyright.

Support recursion, so that all .py files in nested subdirectories are handled too.
"""


def text_block() -> str:  # This is a an entry point in pyproject.toml
    """The copyright.txt file is the one and only place for definition of
    the Sandia National Laboratories copyright test block.
    Updates to the test block should be directly to the copyright.txt file.

    The copyright assertion block exists as a stand-alone text file
    named `copyright.txt` and located in the same path as this module.

    When used from the command line via an entry point, this function will
    read the contents of the copyright.txt file and echo it to the terminal
    """

    # Default to error, unless a successful file read overwrites contents.
    contents = "Error: The `copyright.txt` file could not be read."

    ff = Path(__file__).parent.joinpath("copyright.txt")
    with open(str(ff), mode="r") as fin:
        contents = fin.read()  # overwrite if successful

    return contents


def modules_list(path: Path) -> List[Path]:
    """Finds all Python files in the given path and in all subdirectories."""

    # Reference: https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
    # Patterns are the same as for fnmatch, with the addition of "**" which
    # means "this directory and all subdirectories, recursively". In other words,
    # it enables recursive globbing.
    return list(path.glob("**/*.py"))


def copyright_exists(path: Path) -> bool:
    """Given a single python file as a Path, returns True if the copyright
    block is contained in the Python file, returns False otherwise.
    """
    copyright_exists = False

    with open(path, mode="r") as fin:
        contents = fin.read()
        if text_block() in contents:
            copyright_exists = True  # overwrite

    return copyright_exists


def copyright_create(path: Path, text_block=text_block()) -> bool:
    """Given a Path to a .py file, appends the copyright `text_block` to the end
    of the file.  Returns True if the append operation was successful or if the
    copyright already exists (avoid duplicate copyright blocks); False otherwise.
    """
    created = False  # default first state, copyright not created yet

    print(f"Processing path: {path}")

    if copyright_exists(path=path):
        return True

    path_temp = Path(str(path) + ".temp")

    with open(path, mode="r") as fin:
        contents = fin.read()
        contents_new = contents + "\n\n" + text_block + "\n"
        with open(path_temp, mode="w") as fout:
            fout.write(contents_new)

        # overwrite old original file with new temp file
        copyfile(src=path_temp, dst=path)

        # remove the new temp file
        path_temp.unlink()

        created = True  # overwrite

    return created


def copyright_update(path: Path, *, new: str, old=text_block()) -> bool:
    """Given a Path to a .py file, replaces the old copyright text block with
    the `new` copyright text block.  Returns True if the append operation was
    successful; False otherwise.

    For example, we may want to update the year, or year span, or contract
    number, etc.  The entire old string is removed from the module, and the
    entire new string is inserted in its place.
    """
    if old == new:
        # Do not update if the new string is identical to old string.
        # Return False to indicate no update occurred.
        return False

    path_temp = Path(str(path) + ".temp")

    with open(path, mode="r") as fin:
        contents = fin.read()
        contents_new = contents.replace(old, new)

        with open(path_temp, mode="w") as fout:
            fout.write(contents_new)

        # overwrite old original file with new temp file
        copyfile(src=path_temp, dst=path)

        # remove the new temp file
        path_temp.unlink()

        return True  # update occurred


def copyright() -> bool:  # This is a an entry point in pyproject.toml
    success = False
    root_path = Path.cwd()
    print(f"Processing path: {root_path}")
    print("Marking all `*.py` files with the text block contained in `copyright.txt`.")

    py_files = modules_list(root_path)

    for item in py_files:
        copyright_create(item)

    success = True  # overwrite

    return success


"""
Copyright 2021 Sandia National Laboratories

Notice: This computer software was prepared by National Technology and Engineering Solutions of
Sandia, LLC, hereinafter the Contractor, under Contract DE-NA0003525 with the Department of Energy
(DOE). All rights in the computer software are reserved by DOE on behalf of the United States
Government and the Contractor as provided in the Contract. You are authorized to use this computer
software for Governmental purposes but it is not to be released or distributed to the public.
NEITHER THE U.S. GOVERNMENT NOR THE CONTRACTOR MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR ASSUMES
ANY LIABILITY FOR THE USE OF THIS SOFTWARE. This notice including this sentence must appear on any
copies of this computer software. Export of this data may require a license from the United States
Government.
"""