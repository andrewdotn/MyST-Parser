from pathlib import Path

import pytest

from markdown_it.utils import read_fixture_file
from myst_parser.main import to_docutils

FIXTURE_PATH = Path(__file__).parent.joinpath("fixtures")


@pytest.mark.parametrize(
    "line,title,input,expected", read_fixture_file(FIXTURE_PATH.joinpath("basic.md"))
)
def test_basic(line, title, input, expected):
    document = to_docutils(input)
    print(document.pformat())
    assert "\n".join(
        [l.rstrip() for l in document.pformat().splitlines()]
    ) == "\n".join([l.rstrip() for l in expected.splitlines()])


@pytest.mark.parametrize(
    "line,title,input,expected",
    read_fixture_file(FIXTURE_PATH.joinpath("role_options.md")),
)
def test_role_options(line, title, input, expected):
    document = to_docutils(input)
    print(document.pformat())
    assert "\n".join(
        [l.rstrip() for l in document.pformat().splitlines()]
    ) == "\n".join([l.rstrip() for l in expected.splitlines()])


@pytest.mark.parametrize(
    "line,title,input,expected",
    read_fixture_file(FIXTURE_PATH.joinpath("docutil_roles.md")),
)
def test_docutils_roles(line, title, input, expected):
    document = to_docutils(input)
    print(document.pformat())
    assert "\n".join(
        [l.rstrip() for l in document.pformat().splitlines()]
    ) == "\n".join([l.rstrip() for l in expected.splitlines()])


@pytest.mark.parametrize(
    "line,title,input,expected",
    read_fixture_file(FIXTURE_PATH.joinpath("docutil_directives.md")),
)
def test_docutils_directives(line, title, input, expected):
    # TODO fix skipped directives
    # TODO test domain directives
    if title.startswith("SKIP"):
        pytest.skip(title)
    document = to_docutils(input)
    print(document.pformat())
    assert "\n".join(
        [l.rstrip() for l in document.pformat().splitlines()]
    ) == "\n".join([l.rstrip() for l in expected.splitlines()])


@pytest.mark.parametrize(
    "line,title,input,expected",
    read_fixture_file(FIXTURE_PATH.joinpath("sphinx_directives.md")),
)
def test_sphinx_directives(line, title, input, expected):
    # TODO fix skipped directives
    # TODO test domain directives
    if title.startswith("SKIP"):
        pytest.skip(title)
    document = to_docutils(input, in_sphinx_env=True)
    print(document.pformat())
    assert "\n".join(
        [l.rstrip() for l in document.pformat().splitlines()]
    ) == "\n".join([l.rstrip() for l in expected.splitlines()])


@pytest.mark.parametrize(
    "line,title,input,expected",
    read_fixture_file(FIXTURE_PATH.joinpath("sphinx_roles.md")),
)
def test_sphinx_roles(line, title, input, expected):
    if title.startswith("SKIP"):
        pytest.skip(title)
    document = to_docutils(input, in_sphinx_env=True)
    print(document.pformat())
    assert "\n".join(
        [l.rstrip() for l in document.pformat().splitlines()]
    ) == "\n".join([l.rstrip() for l in expected.splitlines()])
