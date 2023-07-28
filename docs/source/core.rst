***************************
Core Problem Package Format
***************************

This section explains the core part of the problem package format,
enough to define many interesting problems.
For illustration, we use a very simple example problem that is fully specified in
the directory
`increment <https://github.com/thorehusfeldt/problem_package_format_copy/tree/main/problems/increment>`_.

Problem Statement
=================

The problem statement of the problem is provided in the directory
``problem_statement/``.

This directory must contain one file per (natural) language, for at least one
language, named ``problem.<language>.<filetype>``.
It contains the description of the problem aimed at the solver, 
including input and output specifications, but not sample input and output.
Language must be given as the shortest ISO 639 code.
If needed, a hyphen and an ISO 3166-1 alpha-2 code may be appended to ISO 639 code. 
Optionally, the language code can be left out.
The default is then English (``en``).
Filetype can be either ``tex`` for LaTeX, ``md`` for Markdown, or ``pdf`` for PDF.

.. literalinclude :: ../../problems/increment/problem_statement/problem.en.tex
    :caption: problem_statement/problem.en.tex

.. hint ::
    Many kinds of transformations on the problem
    statements, such as conversion to HTML or styling to fit in a single
    document containing many problems will not be possible for PDF problem
    statements, so using PDF should be avoided if at all possible.

Auxiliary files needed by the problem statement files must all be in ``problem_statement/``.
The statement source ``problem.<language>.<filetype>``
should reference auxiliary files as if the working directory is
``problem_statement/``. 
Image file formats supported are ``.png``, ``.jpg``, ``.jpeg``, and ``.pdf``.

A LaTeX file may include the problem name using the LaTeX command
``\problemname`` in case LaTeX formatting of the title is wanted.
Otherwise, the problem name specified in ``problem.yaml`` will be used.

The problem statements must only contain the actual problem statement, no sample data.


Test Data
=========

The test data are provided in subdirectories of ``data/``. 
Sample data resides in ``data/sample/`` and secret data resides in ``data/secret/``.

A :term:`test case` has a unique :term:`base name` such as ``data/secret/043-no-edges`` and is determined by its input file, such as ``data/secret/043-no-edges.in``.
Most test cases have a default answer file with the extension ``.ans``.
Several other files with the same base name and other extensions than ``.in`` may exist;

Input ``.in``:

    *Required*. Explain me.

    .. literalinclude:: ../../problems/increment/data/sample/1.in
        :caption: data/sample/1.in

Default answer ``.ans``:

    Must exist for problems that use the default output validator.
    See :ref:`Custom Output Validation`.

    .. literalinclude:: ../../problems/increment/data/sample/1.ans
        :caption: data/sample/1.ans

Hint ``.hint``:

    The hint file is a text file with filename extension\ ``.hint`` giving a
    hint for solving an input file. The hint file is meant to be given as
    feedback, i.e. to somebody that fails to solve the problem.

Description ``.desc``:    

    The description file is a text file with filename extension ``.desc`` describing the purpose of an input file. 
    The description file is meant to be privileged information that explains the purpose of the related
    test file, e.g., what cases it’s supposed to test.
    
Illustration:    

    The Illustration is an image file with filename extension ``.png``, ``.jpg``, ``.jpeg``, or ``.svg``. 
    The illustration is meant to be privileged information illustrating the related test file.

.. container:: not-icpc

   The test data for the problem can be organized into a tree-like
   structure. Each node of this tree is represented by a directory and
   referred to as a test data group. Each test data group may consist of
   zero or more test cases (i.e., input-answer files) and zero or more
   subgroups of test data (i.e., subdirectories).

At the top level, the test data is divided into exactly two groups:
``sample`` and ``secret``. These two groups may be further split into
subgroups as desired.

Test files and groups will be used in lexicographical order on file base name. 
If a specific order is desired a numbered prefix such as ``00``, ``01``, ``02``, ``03``, and so on, can be used.


Invalid Input Files
-------------------

In the ``data/`` directory, there may be an ``invalid_inputs/``
directory containing input files that must be rejected by at least one
input validator. 
These are meant to only test the input validators, and are not used for judging.
The rejected input files can be organized into a tree-like structure similar to the test data. 
There may be ``testdata.yaml`` files within this structure, but they may only contain
the key ``input_validator_flags``.

.. literalinclude:: ../../problems/increment/data/invalid_inputs/too_large.in
    :caption: data/invalid_inputs/too_large.in

.. literalinclude:: ../../problems/increment/data/invalid_inputs/not_int.in
    :caption: data/invalid_inputs/not_int.in

.. literalinclude:: ../../problems/increment/data/invalid_inputs/too_many_tokens.in
    :caption: data/invalid_inputs/too_many_tokens.in


Example Submissions
===================

Correct and incorrect solutions to the problem are provided in
subdirectories of ``submissions/``. 

Submissions must read input data from standard input, and write output
to standard output.

An incomplete list possible of subdirectories is:

``accepted``:

    Accepted as a correct solution.
    
    At least one program in ``accepted`` is required.

    .. literalinclude:: ../../problems/increment/submissions/accepted/th.py
        :language: python
        :caption: submissions/accepted/th.py

``wrong_answer``:

    Wrong answer for some test
    case, but is not too slow and
    does not crash for any test case 

    .. literalinclude:: ../../problems/increment/submissions/wrong_answer/decrements.py
        :language: python
        :caption: submissions/wrong_answer/decrements.py

``time_limit_exceeded``:

  Too slow for some test case.  
  May also give wrong answer but may not crash for any test case.

``run_time_error``:

    Crashes for some test file.

    .. literalinclude:: ../../problems/increment/submissions/run_time_error/conversion.py
        :language: python
        :caption: submissions/run_time_error/conversion.py

Input Validation
================

Input validators, for verifying the correctness of the input files, are
provided in ``input_validators/``. 
Input validators can be specified as
VIVA-files (with extension ``.viva``), 
Checktestdata-files (with extension ``.ctd``), 
or as a program.

All input validators provided will be run on every input file.
Validation fails if any validator fails.

    .. literalinclude:: ../../problems/increment/input_validators/validate.ctd
        :language: yaml
        :caption: increment/problem.yaml


Input Validator Invocation
--------------------------

An input validator program must be an application (executable or
interpreted) capable of being invoked with a command line call.

All input validators provided will be run on every test data file using
the arguments specified for the test data group they are part of;
see :ref:`input_validator_flags`.
Validation fails if any validator fails.


When invoked the input validator will get the input file on stdin.

The input validator must be possible to use as follows on the command line:

``./validator [arguments] < inputfile``


The input validator may output debug information on stdout and stderr.
This information may be displayed to the user upon invocation of the
validator.

The input validator must exit with code 42 on successful validation. Any
other exit code means that the input file could not be confirmed as
valid.

The validator MUST NOT read any files outside those defined in the Invocation section. 
Its result MUST depend only on these files and the arguments.

    .. code-block:: python3
        :caption: alternative input_validators/validate.py
    
        import sys
        import re
    
        line = sys.stdin.readline()           # read line from standard input
        re.match("(0|-?[1-9][0-9]+)\n", line) # check against regex
    	assert -32768 <= int(line) < 32766    # check bounds
        assert sys.readline == ""             # check no more ouput 
        sys.exit(42)                          # got this far? accept!


Problem Settings
================

Problem settings are specified in  `problem.yaml` and must at least include the problem's name.
It is good practice to also include the author and license.

.. literalinclude:: ../../problems/increment/problem.yaml
    :language: yaml
    :caption: increment/problem.yaml

For the full specification, see :ref:`Problem Settings`.

How Judging is Done
===================

In pass-fail problems, submissions are basically judged as
either accepted or rejected (though the “rejected” judgement is more
fine-grained and divided into results such as “Wrong Answer”, “Time
Limit Exceeded”, etc).

Default Output Validation
-------------------------

To validate a submission, an output validator checks the ouput of the submission on the secret test data.
By default, this process just compares the ``.ans``-file of every test case with the submission's output on the corresponding ``.in``-file.
The default output validator is lenient with respect to whitespace, and character case, so
``34 alice`` is the same as `` 34     AlicE``, but different from ``34.0 alice``, ``034 alice`` and ``34 alicee``.
For more details, or if you need different behaviour from the default output validator, see :ref:`Modfifying the Default Output Validator`.
For problems with more than one correct answer, you need to write your own validator; see :ref:`Custom Output Validation`.

Judgement
---------

For pass-fail problems, the verdict of a submission is the first
non-accepted verdict, where test cases are run in lexicographical order
of their full file paths (note that ``sample`` comes before ``secret``
in this order).


Timing
------

By default, the time limit for a problem is inferred by the judge based on the the example submissions.
For instance, the time limit may be twice the slowest running time among the submissions in ``submissions/accepted``, rounded up to the nearest integer number of seconds.

To modify these settings, see :ref:`Problem Timing`.
