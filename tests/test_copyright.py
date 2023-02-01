"""This module tests operation and coverage of the copyright module.

To run
cd ~/reli
pytest reli/tests/unit/test_copyright.py -v
pytest reli/tests/unit/test_copyright.py -v --cov=reli --cov-report term-missing
"""

from pathlib import Path
from shutil import copyfile

# from typing import Final  # postpone Final until Python 3.9 is used in pyproject.toml

# import pytest

import snlcopyright.copyright_crud as cr


def test_text_block():
    """Test that the text block of the copyright is as expected as
    defined once and for all in the 'text_block' function of the copyright module.
    """

    # known: Final[  # postpone Final until Python 3.9 is required
    # TODO: Figure out the problem with this `known` test string.
    # I am struggling to get formatting perfect, so postpone a deeper teset for now.
    # known: str = '"""\nCopyright 2023 Sandia National Laboratories\nNotice: This computer software was prepared by National Technology and Engineering Solutions of\nSandia, LLC, hereinafter the Contractor, under Contract DE-NA0003525 with the Department of Energy\n(DOE). All rights in the computer software are reserved by DOE on behalf of the United States\nGovernment and the Contractor as provided in the Contract. You are authorized to use this computer\nsoftware for Governmental purposes but it is not to be released or distributed to the public.\nNEITHER THE U.S. GOVERNMENT NOR THE CONTRACTOR MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR ASSUMES\nANY LIABILITY FOR THE USE OF THIS SOFTWARE. This notice including this sentence must appear on any\ncopies of this computer software. Export of this data may require a license from the United States\nGovernment.\n"""'

    found = cr.text_block()

    assert found


def test_copyright_exists():
    """Given two examplar test files, one with a copyright block and one without,
    verify that the function returns True and False, respectively.
    """
    aa = Path(__file__).parent.joinpath("files")

    bb = aa.joinpath("module_with_copyright.py")
    assert bb.is_file()
    assert cr.copyright_exists(bb)

    cc = aa.joinpath("module_without_copyright.py")
    assert cc.is_file()
    assert not cr.copyright_exists(cc)  # assert no copyright in this file


def test_copyright_create():
    """Given an examplar test file without a copyright, create a temporary
    clone of that test file, append the copyright to the cloned file, verify
    the copyright exists in the newly mutated cloned file, then delete the
    temporary cloned file.
    """
    aa = Path(__file__).parent.joinpath("files")
    bb = aa.joinpath("module_without_copyright.py")

    # The original exemplar teste file should never have a copyright, fail if it does.
    assert not cr.copyright_exists(path=bb)

    # Create a temporary clone of the exemplar test file.
    cc = aa.joinpath((str(bb) + ".clone"))
    copyfile(src=bb, dst=cc)

    # Append the copyright to the cloned file.
    cr.copyright_create(path=cc)

    # Verify the copyright exists in the newly mutated cloned file.
    assert cr.copyright_exists(path=cc)

    # Delete the temporary cloned file.
    cc.unlink()
    assert not cc.is_file()

    # Test the case wherein the copyright already exists, and assure that the
    # function does not create a second duplated copyright.
    dd = aa.joinpath("module_with_copyright.py")
    assert cr.copyright_exists(path=dd)
    ee = aa.joinpath((str(dd) + ".clone"))
    copyfile(src=dd, dst=ee)
    assert cr.copyright_create(ee)
    ee.unlink()
    assert not ee.is_file()


def test_modules_list():
    """To test the copyright modules, we have constructed several exemplar test
    files, and this test verifies the files in the file structure are as designed.
    """
    aa = Path(__file__).parent.joinpath("files")

    expected = [
        aa.joinpath("hello_world.py"),
        aa.joinpath("nested_files", "hello_world_nested.py"),
        aa.joinpath("module_with_copyright.py"),
        aa.joinpath("module_without_copyright.py"),
    ]

    found = cr.modules_list(path=aa)

    for item in found:
        assert item in expected


# @pytest.mark.skip("work in progress")
def test_copyright_update():
    """Given a module with a copyright, test that the copyright can be updated."""
    original_text = cr.text_block()

    # Work with the "module_with_copyright.py"
    aa = Path(__file__).parent.joinpath("files")
    bb = aa.joinpath("module_with_copyright.py")

    # Make a backup copy of "module_with_copyright.py"
    # and restore this file from the backup and the
    # end of the test.
    path_bak = Path(str(bb) + ".bak")
    copyfile(src=bb, dst=path_bak)

    # Test the degenerate case where the update is
    # indentical to the current state:
    # Replace the 2023 and updat it to 2023.
    new_text = original_text.replace("2023", "2023")  # replace all occurrences

    assert bb.is_file()
    assert cr.copyright_exists(bb)

    success = cr.copyright_update(path=bb, new=new_text, old=original_text)
    assert not success

    # Replace the 2023 and updated it to 2022.
    new_text = original_text.replace("2023", "2022")  # replace all occurrences

    aa = Path(__file__).parent.joinpath("files")

    bb = aa.joinpath("module_with_copyright.py")
    assert bb.is_file()
    assert cr.copyright_exists(bb)

    success = cr.copyright_update(path=bb, new=new_text, old=original_text)

    assert success

    # Restore original from the backup.
    copyfile(src=path_bak, dst=bb)

    # Remove the newly created temp file.
    path_bak.unlink()


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
