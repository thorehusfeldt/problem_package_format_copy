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

The package consists of a single directory whose name is the :term:`package name`.
The package name consists of alphanumerical characters, such as `increment`.
A minimal problem has the following structure:

::

    <package_name>
    ├── problem_statement/
    │   └── problem.en.tex
    ├── data/
    │   ├── sample/
    │   └── secret/
    ├── submission/
    │   └── accepted/
    ├── problem.yaml
    └── input_validators/

The meaning of the subdirectories is as follows:

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
archive of such a directory with the ``<package_name>.kpp`` or ``<package_name>.zip``.

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
    :language: tex
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

Input, ``.in``:
    *Required*. Explain me.

    .. literalinclude:: ../../problems/increment/data/sample/1.in
        :caption: data/sample/1.in

Default answer, ``.ans``:
    Must exist for problems that use the default output validator.
    See :ref:`Custom Output Validation`.

    .. literalinclude:: ../../problems/increment/data/sample/1.ans
        :caption: data/sample/1.ans

Hint, ``.hint``:
    The hint file is a text file with filename extension\ ``.hint`` giving a
    hint for solving an input file. The hint file is meant to be given as
    feedback, i.e. to somebody that fails to solve the problem.

Description, ``.desc``:    
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

All input validators provided will be run on every test case using
the arguments specified for the test data group they are part of;
see :ref:`Test Data Settings`.
Validation fails if any validator fails.

When invoked the input validator will get the input file on stdin.

The input validator must be possible to use as follows on the command line:

.. code-block:: bash

    ./validator [arguments] < inputfile


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

Basic Output Validation
-----------------------

To validate a submission, an output validator checks the ouput of the submission on the secret test data.
By default, this process just compares the ``.ans``-file of every test case with the submission's output on the corresponding ``.in``-file.
The default output validator is lenient with respect to whitespace, and character case, so
``34 alice`` is the same as `` 34     AlicE``, but different from ``34.0 alice``, ``034 alice`` and ``34 alicee``.
For more details, or if you need different behaviour from the default output validator, see :ref:`Default Output Validation`.
For problems with more than one correct answer, you need to write your own validator; see :ref:`Custom Output Validation`.

Judgement
---------

For pass-fail problems, the verdict of a submission is the first
non-accepted verdict, where test cases are run in lexicographical order
of their full file paths (note that ``sample`` comes before ``secret``
in this order).


Default Timing
--------------

By default, the time limit for a problem is inferred by the judge based on the the example submissions.
If :math:`a_1,\ldots, a_k` are the running times (in seconds) for the example submissions in
``submissions/accepted``, then the time limit :math:`t` is given by

.. math :: t = \bigl\lceil 2\cdot\max (a_1,\ldots,a_k)  \bigr\rceil\,.

Moreover, the running time :math:`e` for every submission in ``submissions/time_limit_exceeded`` must satisfy 

.. math :: e \geq \tfrac32 t  \,.

To modify these settings, see :ref:`Problem Timing`.
*****************************************************
Problem Settings, Output Validation Flags, and Timing
*****************************************************

Default Output Validation
=========================

The default output validator tokenizes the submission output and compares it token by token with the default answer.
It supports the following flags, which control how tokens are compared.

``case_sensitive``:
    String comparisons should be case-sensitive. By defaul they are not.
``space_change_sensitive``:
    Changes in the amount of whitespace should
    be rejected (the default is that any sequence of one or
    more whitespace characters are equivalent).
``float_relative_tolerance`` ε:
    Floating-point tokens should be accepted
    if they are within relative error ≤ ε (see below for details).                                             
``float_absolute_tolerance`` ε:
    indicates that floating-point tokens should be accepted
    if they are within absolute error ≤ ε (see below for    
    details).                                                 
``float_tolerance`` ε:
    short-hand for applying ε as both relative and absolute tolerance.

When both a relative and an absolute tolerance are supplied, a token is accepted if it is within either of the two
tolerances. 
When a floating-point tolerance has been set, any valid formatting of floating point numbers is accepted for floating point tokens.
For instance, if a token in the answer file says ``0.0314``, a token of ``3.14000000e-2`` in the output file would be accepted.
If no floating point tolerance has been set, floating point tokens are treated just like any other token and have to match exactly.

The output validator flags are set in ``data/testdata.yaml``:

.. code-block:: yaml
    :caption: data/problem.yaml

    output_validator_flags: case_sensitive space_change_sensitive

.. code-block:: yaml
    :caption: data/problem.yaml

    output_validator_flags: float_tolerance 10e-5

Problem Settings
================

Metadata about the problem (e.g., source, license, limits) are provided
in a YAML file named ``problem.yaml`` placed in the root directory of the package.

.. code-block:: yaml
    :caption: problem.yaml

    name: Hello Moon
    problem_format_version: 2023-07
    author: Robin McAuthorson
    license: cc by-sa

.. code-block:: yaml
    :caption: problem.yaml

    name: Hello Moon
    problem_format_version: 2023-07
    author: Robin McAuthorson
    source: Lunar Collegiate Programming Contest NCPC 2023
    source_url: lunar.icpc.io
    license: cc by-sa
    rights_owner: Miscatonic University
    type: pass-fail
    validation:
        interactive: true

The keys are defined as below. Keys are optional unless explicitly
stated. Any unknown keys should be treated as an error.

.. object:: name


    **Type:** string or map

    When `name` is a map, it maps language codes to strings.

    .. code-block:: yaml
	:caption: problem.yaml

        name: Hello World!

    .. code-block:: yaml
	:caption: problem.yaml

        name: 
	  en: Hello World!
	  fr: Bonjour Le Monde!
	  de: Hallo Welt

    *Required*

.. object:: version

    **Type:** string

    If using this version of the Format must be  the string ``2023-07-draft``.
    Will be on the form     ``<yyyy>-<mm>`` for a stable version,
    ``<yyyy>-<mm>-draft`` or ``draft`` for a draft        version, or
    ``legacy`` for the version before the     addition of
    problem_format_version. Documentation for version ``<version>`` is
    available at                 https://www.kattis.com
    /problem-package-format/spec/problem_package_format/. 

.. object:: type

    **Type:** string

    **Default:** ``"pass-fail"``

    In ICPC, must be `"pass-fail"`
    In general, can be `"pass-fail"` or `"scoring"`

.. object:: author

    **Type:** string

    Who should get author credits. This would typically   be the people that
    came up with the idea, wrote the   problem specification and created the
    test data. This is sometimes omitted when authors choose to instead   only
    give source credit, but both may be specified.   

.. object:: source

    **Type:** string

    Who should get source credit. This would typically be
    the name (and year) of the event where the problem 
    was first used or created for.      

.. object:: source_url

    **Type:** string

    Link to page for source event. 
    
    *Forbidden* if source is not specified.

.. object:: rights_owner

    **Type:** string

    Owner of the copyright of the problem. If not present, author is owner. If
    author is not present either, source is owner. 
    
    *Required* if license is something other than ``unknown`` or ``public domain``.
    
    *Forbidden* if license is ``public domain``. 

.. object:: license

    **Type:** string

    **Default:** ``"unknown"``

    License under which the problem may be used. 
    The possible values are:

    ``unknown``:
        The default value. In practice means that the problem can not be used.
    ``public domain``:
        There are no known copyrights on the problem, anywhere in the world. See http://creativecommons.org/about/pdm 
    ``cc0``:
        CC0, “no rights reserved”. See http://creativecommons.org/about/cc0 
    ``cc by``:
       CC attribution. See http://creativecommons.org/licenses/by/4.0
    ``cc by-sa``:
        CC attribution, share alike; see http://creativecommons.org/licenses/by-sa/4.0
    ``educational``:
        May be freely used for educational purposes.
    ``permission``:
        Used with permission. The author must be contacted for every additional use.                

.. object:: uuid

    **Type**: string

    UUID identifying the problem

.. object:: limits

    **Type**: map

    A map defining various limits on the behaviour of an accepted submission,
    Three keys, all optional, determine the time limit.
    See :ref:`Problem Timing`.

    ``time_multipliers``
        is itself a map defining the values ``ac_to_time_limit`` and ``time_limit_to_tle``.
    ``time_resolution``
        a number; default ``1.0``.
    ``time_limit``
        a number, in seconds, that determines the upper bound on the running time of a solution.

    The remaining keys of `limits`, also all optional, take integer values.
    Their default values are  system-dependent.

    ====================== ======== ======================
    Key                    Unit     Typical System Default
    ====================== ======== ======================
    ``memory``             MiB      2048
    ``output``             MiB      8
    ``code``               kiB      128
    ``compilation time``   seconds  60
    ``compilation memory`` MiB      2048
    ``compilation time``   seconds  60
    ``validation memory``  MiB      2048
    ``validation output``  MiB      8
    ====================== ======== ======================

    System defaults can vary, but you *should* assume that it’s reasonable. Only specify
    these limits when the problem needs a specific limit, but *do* specify limits
    even if the “typical system default” is what is needed.

    .. code-block:: yaml
	:caption: problem.yaml
	
	name: Nasty problem
	# Submissions may use at most 1kB of code and must terminate in half a second
        limits:
	  time_limit: 0.5
	  code: 1

.. object:: validation

    **Type**: string or map

    **Default**: ``"default"``

    Describes the behaviour of the output validator.
    If a string, must be either ``"default"`` or ``"custom"``.
    If a map, contains any of three boolean keys:

    scoring:
        Only valid for problems with `type: scoring`.
	Indicates that the output validator produces a score.
    interactive:
	specifies that the validator is run interactively with a submission. 
    multipass:
	 indicates that the submission should run multiple 
	 times with inputs generated by the validator, and    

    .. code-block:: yaml
        :caption: problem.yaml
    

        name: Guess
        validation:
            interactive: true

    .. code-block:: yaml
        :caption: problem.yaml
    
        name: Problem With Interactive Scoring Validator
	type: scoring
        validation:
            scoring: true
            interactive: true

.. object:: keywords

    **Type**: list of strings

    List of keywords.                

.. object:: languages

    **Type**: the string ``"all"`` or a list of strings

    *Not ICPC*

    List of programming languages or the string ``all``. 

    If a list is given, the problem may only be solved using those
    programming languages.

    .. code-block:: yaml

        languages: [java, apl, pascal]

Here is a formal specification of the `problem.yaml` schema:

.. literalinclude:: ../../support/problem.cue
    :caption: CUE schema for problem.yaml

Problem Timing
--------------

The time limit of a problem is a value between the running times of the accepted example submissions
and those that are rejected for begin too slow, with robust safety margins.
More precisely, let :math:`a` denote the maximum running time of the submissions in
in ``submissions/accepted`` and let :math:`e` denote the minimum running time of the submissions in ``submissions/time_limit_exceeded``.
If no such submissions exists, set :math:`e =\infty`.
Then for a resolution :math:`r` and margins :math:`m_1` and :math:`m_2` the time limit :math:`t` is the smallest integer multiple of :math:`r` such that

.. math :: m_1 a \leq t  
	
and 

.. math:: m_2 t  \leq e\,.

In other words

.. math :: t = \min_{i\in \mathbf N} \{\, ir \colon m_1 a \leq ir  \leq e/m_2\}\,.

These decisions can me influenced by the specifying values for ``time_multipliers`` (:math:`m_1` and :math:`m_2`) and ``time_resolution`` (:math:`r`) in ``limits`` of ``problem.yaml``.
They can be overriden altogether by specifying an explicit ``time_limit`` (:math:`t`).

.. code-block:: yaml
    :caption: problem.yaml

    name: Hello Mars!
    limits:
      time_multipliers:
        ac_to_time_limit: 1
        time_limit_to_tle: 1.2
      time_resolution:
        .5

.. object:: time_multipliers

    **Type:** map with the following keys and defaults:

    ================= ======== =======
    Key               Type     Default
    ================= ======== =======
    ac_to_time_limit  number   2.0
    time_limit_to_tle number   1.5
    ================= ======== =======

    The time multipliers specify safety margins relative to the example submissions.

.. object:: time_resolution

    **Type:**  number

    **Default** 1.0

    *Forbidden* if `time_limit` is specified.
    (In particular, `time_limit` is not required to be a multiple of the resolution).

.. object:: time_limit

    **Type:**  number

    **Default** Computed, see below


Let ``T_ac`` denote the running time of the slowest accepted example submission.
Let ``T_tle`` denote the running time fastest time_limit_exceeded example submission, 
or infinity if the problem does not provide at least one time_limit_exceeded submission.

The value of ``time_limit`` must satisfy ``T_ac * ac_to_time_limit <=
time_limit`` and ``time_limit * time_limit_to_tle <= T_tle``. 
If no ``time_limit`` is provided, the default value is the smallest integer multiple
of ``time_resolution`` that satisfies these inequalities. 
It is an error if no such multiple exists.

.. note ::

    Since time multipliers are more future-proof than absolute time limits, 
    avoid specifying ``time_limit`` whenever practical.

.. note ::
    Contest systems should make a best effort to respect the problem time
    limit, and should warn when importing a problem whose time limit is
    specified with precision greater than can be resolved by system timers.





****************
Scoring Problems
****************

In scoring problems, accepted submissions are given a numerical :term:`score`, often an integer.
The goal of the submission is to maximize the score.


Test Data Settings
------------------

In each test data group, a file ``testdata.yaml`` may be placed to
specify how the result of the test data group should be computed.
If a test data group has no ``testdata.yaml`` file, the ``testdata.yaml`` in the closest ancestor group that has one will be used.
If there is no ``testdata.yaml`` file in the root ``data`` group, one is implicitly added with the default values.

The following keys can be given in ``testdata.yaml``:

.. object:: output_validator_flags
    
    **Type**: string

    **Default**: ``""``

.. object:: input_validator_flags
    
    **Type**: string or map

    **Default**: ``""``

    Arguments passed to each input validator for this test data group. If a
    string then those are the flags that will be passed to each input
    validator for this test data group. If a map then each key is the name
    of the input validator and the value is the flags to pass to that input
    validator for this test data group. Validators not present in the
    map are run without flags.

    .. code-block:: yaml
    
        input_validator_flags: --max_n 500 connected

    .. code-block:: yaml
    
        input_validator_flags:
          topology: connected
          bounds: --max_n 50
     
.. object:: grading
    
    **Type**: map

    Description of how the results of the group test cases 
    and subgroups should be aggregated.                    
    See :ref:`Grading`.


The formal specification for `testdata.yaml` is this:

.. literalinclude :: ../../support/testdata.cue
    :caption: CUE schema for testdata.yaml

Grading
-------

For scoring problems, the behaviour is configured by the following flags under ``grading`` in ``testdata.yaml``:

.. object:: score

    **Type:** number

    **Default:** 0 in `data/sample`, else 1.

    The score assigned to an accepted input file in the 
    group. If a scoring output validator is used, this 
    score is *multiplied* by the score from the 
    validator.                           

.. object:: max_score

    **Type:** number

    The maximum score allowed for this test group. It is an error to exceed this.

    **Default:** The sum/mininum of ``score`` and the subresults’ ``max_score`` values, dependinding on if ``score_aggregation`` is ``"sum"``/``"min"``.

.. object:: score_aggregation

    **Type**: ``"sum"`` or ``"min"``

    **Default:** ``"sum"`` in ``data`` and ``data/secret``, else ``"min"``.

    The score for this test group is the sum of the subresult scores. 

.. object:: verdict_aggregation

    **Type**: `"first_error"` or `"accept_if_any_accepted"`

    **Default:** ``"accept_if_any_accepted"`` in ``data`` and ``data/secret``, else ``"first_error"``.

    If ``first_error``, the verdict is that of the first non-accepted subresult. 
    Only test cases in the group up to the first non-accepted case are judged. 

    If ``accept_if_any_accepted``, the verdict is accepted if any subresult is accepted,   
    otherwise that of the first non-accepted subresult.     
    All test cases in the group are judged.

The defaults are chosen so that that problems with scoring subtasks can be organised as follows:

.. code-block:: text

    data
      +-sample
      +-secret
        +-subtask1
        +-subtask2
        +-subtask3

With the default output validator it is then sufficient to specify the subtask points as an integer value of `score` in the three `subtask` directories.

.. versionadded:: 2.
    `score` is a multiplier for scoring output validators. In particular, if an output validator assigns the
    default score 1 to an accepted solution, the resulting value is exacly `score`,
    consistent with the previous behaviour for non-scoring validators.


    Sensible defaults for scoring problems.
************************
Custom Output Validation
************************

Custum Output Validation
------------------------

A validator program must be an application (executable or interpreted)
capable of being invoked with a command line call. The details of this
invocation are described below. The validator program has two ways of
reporting back the results of validating:

1. The validator must give a judgement (see `Reporting a
   judgement <#reporting-a-judgement>`__).
2. The validator may give additional feedback, e.g., an explanation of
   the judgement to humans (see `Reporting Additional
   Feedback <#reporting-additional-feedback>`__).

A custom output validator is used if the problem requires more
complicated output validation than what is provided by the default diff
variant described below. It must be provided as the directory
``output_validator/``, and may contain ``build`` and ``run`` scripts. It
must adhere to the Output validator specification described below.


Output Validator Invocation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When invoked the output validator will be passed at least three command
line parameters and the output stream to validate on stdin.

The validator should be possible to use as follows on the command line:

.. code-block:: sh

   ./validator input judge_answer feedback_dir [additional_arguments] < team_output [ > team_input ]

The meaning of the parameters listed above are:

input: 
    a string specifying the name of the input data file which was
    used to test the program whose results are being validated.

judge_answer: 
    a string specifying the name of an arbitrary “answer
    file” which acts as input to the validator program. The answer file
    may, but is not necessarily required to, contain the “correct answer”
    for the problem. For example, it might contain the output which was
    produced by a judge’s solution for the problem when run with input
    file as input. Alternatively, the “answer file” might contain
    information, in arbitrary format, which instructs the validator in
    some way about how to accomplish its task. The meaning of the
    contents of the answer file is not defined by this format.

feedback_dir: 
    a string which specifies the name of a “feedback
    directory” in which the validator can produce “feedback files” in
    order to report additional information on the validation of the
    output file. The feedbackdir must end with a path separator
    (typically ‘/’ or ‘\\’ depending on operating system), so that simply
    appending a filename to feedbackdir gives the path to a file in the
    feedback directory.

additional_arguments: 
    in case the problem specifies additional
    validator_flags, these are passed as additional arguments to the
    validator on the command line.

team_output: 
    the output produced by the program being validated is
    given on the validator’s standard input pipe.

team_input: 
    when running the validator in interactive mode everything
    written on the validator’s standard output pipe is given to the
    program being validated. Please note that when running interactive
    the program will only receive the output produced by the validator
    and will not have direct access to the input file.

The two files pointed to by input and judge_answer must exist (though
they are allowed to be empty) and the validator program must be allowed
to open them for reading. The directory pointed to by feedback_dir must
also exist.

Reporting a judgement
~~~~~~~~~~~~~~~~~~~~~

An output validator is required to report its judgement by exiting with
specific exit codes:

-  If the output is a correct output for the input file (i.e., the
   submission that produced the output is to be Accepted), the validator
   exits with exit code 42.
-  If the output is incorrect (i.e., the submission that produced the
   output is to be judged as Wrong Answer), the validator exits with
   exit code 43.

Any other exit code (including 0!) indicates that the validator did not
operate properly, and the judging system invoking the validator must
take measures to report this to contest personnel. The purpose of these
somewhat exotic exit codes is to avoid conflict with other exit codes
that results when the validator crashes. For instance, if the validator
is written in Java, any unhandled exception results in the program
crashing with an exit code of 1, making it unsuitable to assign a
judgement meaning to this exit code.

Reporting Additional Feedback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of the feedback directory is to allow the validator program
to report more information to the judging system than just the
accept/reject verdict. Using the feedback directory is optional for a
validator program, so if one just wants to write a bare-bones minimal
validator, it can be ignored.

The validator is free to create different files in the feedback
directory, in order to provide different kinds of information to the
judging system, in a simple but organized way. For instance, there may
be a “judgemessage.txt” file, the contents of which gives a message that
is presented to a judge reviewing the current submission (typically used
to help the judge verify why the submission was judged as incorrect, by
specifying exactly what was wrong with its output). Other examples of
files that may be useful in some contexts (though not in the ICPC) are a
score.txt file, giving the submission a score based on other factors
than correctness, or a teammessage.txt file, giving a message to the
team that submitted the solution, providing additional feedback on the
submission.

A judging system that implements this format must support the
judgemessage.txt file described above (I.e., content of the
“judgemessage.txt” file, if produced by the validator, must be provided
by the judging system to a human judge examining the submission). Having
the judging system support other files is optional.

Note that a validator may choose to ignore the feedback directory
entirely. In particular, the judging system must not assume that the
validator program creates any files there at all.

.. container:: not-icpc

   .. rubric:: Multi-pass validation
      :name: multi-pass-validation

   A multi-pass validator can be used for problems that should run the
   submission multiple times sequentially, using a new input generated
   by output validator during the previous invocation of the submission.

   To signal that the submission should be run again, the output
   validator must exit with code 42 and output the new input in the file
   ``nextpass.in`` in the feedback directory. Judging stops if no
   ``nextpass.in`` was created, or the output validator exited with any
   other code.

   It is a judge error to create the ``nextpass.in`` file and exit with
   any other code than 42.

Examples
^^^^^^^^

An example of a judgemessage.txt file:

.. code:: text

   Team failed at test case 14.
   Team output: "31", Judge answer: "30".
   Team failed at test case 18.
   Team output: "hovercraft", Judge answer: "7".
   Summary: 2 test cases failed.

An example of a teammessage.txt file:

.. code:: text

   Almost all test cases failed, are you even trying to solve the problem?

Validator standard output and standard error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A validator program is allowed to write any kind of debug information to
its standard error pipe. This information may be displayed to the user
upon invocation of the validator.

Setting Default Output Validator Flags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In each test data group, a file ``testdata.yaml`` may be placed to
specify how the result of the test data group should be computed. If
a test data group has no ``testdata.yaml`` file, the
``testdata.yaml`` in the closest ancestor group that has one will be
used. If there is no ``testdata.yaml`` file in the root ``data``
group, one is implicitly added with the default values.

The following keys can be given in ``testdata.yaml``

.. object:: output_validator_flags
    
    **Type**: string

    **Default**: ``""``

.. object:: input_validator_flags

Samples for Interactive Problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For interactive problems, any sample test cases must provide an
interaction protocol with the extension ``.interaction`` for each sample
demonstrating the communication between the submission and the output
validator, meant to be displayed in the problem statement. An
interaction protocol consists of a series of lines starting with ``>``
and ``<``. Lines starting with ``>`` signify an output from the
submission to the output validator, while ``<`` signify an input from
the output validator to the submission.

A sample test case may have just an ``.interaction`` file without a
corresponding ``.in`` and ``.ans`` file. However, if either of a ``.in``
or a ``.ans`` file is present the other one must also be present. Unlike
``.in`` and ``.ans`` files for non-interactive problem, interactive
``.in`` and ``.ans`` files must not be displayed to teams: not in the
problem statement, nor as part of sample input download. If you want to
provide files related to interactive problems (such as testing tools or
input files) you can use `attachments <#attachments>`__.

*****************
Other Directories
*****************

This section describes less frequently used directories.

Attachments
===========

Public, i.e., non-secret, files can be made available in addition to the
problem statement and sample test data are provided in the directory
``attachments/``.

Included Code
=============

Code that should be included with all submissions are provided in one
directory per supported language, called ``include/<language>/``.

The files are be copied from a language directory based on the
language of the submission, to the submission files before compiling,
overwriting files from the submission in the case of name collision.
Language must be given as one of the language codes in the language
table in the overview section. If any of the included files are
supposed to be the main file (i.e. a driver), that file must have the
language dependent name as given in the table referred above.

 
********
Appendix
********

Programs
========


There are a number of different kinds of programs that may be provided
in the problem package: submissions, input validators, and output
validators. All programs are always represented by a single file or
directory. In other words, if a program consists of several files, these
must be provided in a single directory. The name of the program, for the
purpose of referring to it within the package is the base name of the
file or the name of the directory. There can’t be two programs of the
same kind with the same name.

Validators, but not submissions, in the form of a directory may include
two POSIX-compliant scripts ``build`` and ``run``. If at least one of these
two files is included:

1. First, if the ``build`` script is present, it will be run. The
   working directory will be (a copy of) the program directory. The
   ``run`` file must exist after ``build`` is done.
2. Then, the ``run`` file (which now exists) must be executable, and
   will be invoked in the same way as a single file program.

Programs without ``build`` and ``run`` scripts are built and run
according to what language is used. Language is determined by looking at
the file endings. If a single language from the table below can’t be
determined, building fails.


For languages where there could be several entry points, the default
entry point in the table below will be used.

+----------+-----------+--------------------+--------------------------+
| Code     | Language  | Default entry      | File endings             |
|          |           | point              |                          |
+==========+===========+====================+==========================+
| c        | C         |                    | .c                       |
+----------+-----------+--------------------+--------------------------+
| cpp      | C++       |                    | .cc, .cpp, .cxx, .c++,   |
|          |           |                    | .C                       |
+----------+-----------+--------------------+--------------------------+
| csharp   | C#        |                    | .cs                      |
+----------+-----------+--------------------+--------------------------+
| go       | Go        |                    | .go                      |
+----------+-----------+--------------------+--------------------------+
| haskell  | Haskell   |                    | .hs                      |
+----------+-----------+--------------------+--------------------------+
| java     | Java      | Main               | .java                    |
+----------+-----------+--------------------+--------------------------+
| ja       | J         | main.js            | .js                      |
| vascript | avaScript |                    |                          |
+----------+-----------+--------------------+--------------------------+
| kotlin   | Kotlin    | MainKt             | .kt                      |
+----------+-----------+--------------------+--------------------------+
| lisp     | Common    | main.{lisp,cl}     | .lisp, .cl               |
|          | Lisp      |                    |                          |
+----------+-----------+--------------------+--------------------------+
| ob       | Ob        |                    | .m                       |
| jectivec | jective-C |                    |                          |
+----------+-----------+--------------------+--------------------------+
| ocaml    | OCaml     |                    | .ml                      |
+----------+-----------+--------------------+--------------------------+
| pascal   | Pascal    |                    | .pas                     |
+----------+-----------+--------------------+--------------------------+
| php      | PHP       | main.php           | .php                     |
+----------+-----------+--------------------+--------------------------+
| prolog   | Prolog    |                    | .pl                      |
+----------+-----------+--------------------+--------------------------+
| python2  | Python 2  | main.py2           | .py2                     |
+----------+-----------+--------------------+--------------------------+
| python3  | Python 3  | main.py            | .py                      |
+----------+-----------+--------------------+--------------------------+
| ruby     | Ruby      |                    | .rb                      |
+----------+-----------+--------------------+--------------------------+
| rust     | Rust      |                    | .rs                      |
+----------+-----------+--------------------+--------------------------+
| scala    | Scala     |                    | .scala                   |
+----------+-----------+--------------------+--------------------------+

.. versionadded:: 2.0

   ``.py`` files now default to Python 3, and using shebangs are no longer supported; 
   Python 2 has to be explicitly indicated by the ``.py2`` extension.


Glossary
========

.. glossary::

    verdict
        one of the strings 'AC', 'WA', 'TLE', 'RTE', or 'JE'
    
    score
        a number

    grade
        a verdict and a score
    
    judgement
        in a pass-fail problem, same as :term:`verdict`. In a scoring problems, same as :term:`grade`.
    
    gradeable
        A testcase or a testroup, i.e., something that can have a grade.
    
    test data
    
        A simple directed acyclic graph whose leaves are test cases.
        The test data without the leaves form a rooted tree.
    
    test case

	An instance to the problem.
        The predecessors of a testcase are testgroups, but not the root.
    
    test group

        An non-leaf node in the test data. The test groups form a rooted
        tree. The root has one or two children, which are called ``sample``
        and ``secret``. The names of all other test groups, if they exist,
        describe their position in the testdata tree, such as ``secret/group1``
        or ``secret/connected/cycles``.

    solver

        Person or group of persons trying to solve the problem. Synonym: team

    submission

        A program submitted by a solver to the judge, 
	or an example submission, which is part of the problem package.

    task

        Synonym for problem 

    judge
    
        Synonym for contest system or judging environment

    package name

        A string of alphanumerical characters used for the problem's root directory.
	For instance, the package name of a problem whose English name is *Hello World!* can be ``helloworld``.
	The package name must match ``[a-z0-9]+``.

    problem name

        The name of a problem in a natural language, such as *Hello World!*.
	All problems need at least one name;
       	most problems have an English name.
