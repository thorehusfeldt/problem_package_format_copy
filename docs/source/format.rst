**********************
Problem Package Format
**********************

This is the ``2023-07-draft`` version of the Kattis problem package
format.

Overview
========

This document describes the format of a *Kattis problem package*, used
for distributing and sharing problems for algorithmic programming
contests as well as educational use.

Directory structure
--------------------

The package consists of a single directory whose name is the problem's unique :term:`problem ID`, such as ``hello``.
Its subdirectories and some of the files have fixed names.
There may be more directories, and in particular more subdirectories.
A minimal problem has the following structure:

::

    <problem_id>
    ├── problem_statement/
    │   └── problem.en.tex
    ├── data/
    │   ├── sample/
    │   └── secret/
    ├── submission/
    │   └── accepted/
    ├── problem.yaml
    └── input_validators/

Their meaning is

``problem_statement``:
    The problem statement, typically given as a TeX file. 
    See :ref:`Problem Statement`.
``data``:
    A directory holding the testdata that team submissions will be run on. It must have two subdirectories;
    `sample` holds the sample inputs and answers shown to the team,
    `secret` holds the secret input. See :ref:`Test Data`.
``submissions``:
    Example submissions that solve (or fail to solve) the problem.
    See :ref:`Example Submissions`.
``problem.yaml``:
    A configuration file describing problem settings (such as time limits) and metadata (such as authorship). See :ref:`Problem Settings`.
``input_validators``:
    Programs that validate the test data, i.e., the input files in `data`.
    For a problem to be valid, all input file in `data` must be accepted by the input validators.
    See :ref:`Input Validation`.

With this setup, the :term:`judge` runs a  :term:`team submission` against the test data in `data` and verifies that it is both correct and fast enough, and produces a judgement. See :ref:`How Judging is Done`.

File Name Requirements
----------------------

The problem ID of the directory must consist solely of lower case letters a-z and digits 0-9. 
Alternatively, the problem package can be a ZIP compressed
archive of such a directory with the ``<problem_id>.kpp`` or ``<problem_id>.zip``.

All file names for files included in the package must match the
following regexp:

``[a-zA-Z0-9][a-zA-Z0-9_.-]*[a-zA-Z0-9]``

That is, file names must be of length at least 2, consist solely of lower or upper
case letters a-z, A-Z, digits 0-9, period, dash, or underscore, but must
not begin or end with period, dash or underscore.

All text files for a problem must be UTF-8 encoded and not have a byte
order mark.

All floating point numbers must be given as the external character
sequences defined by IEEE 754-2008 and may use up to double precision.


