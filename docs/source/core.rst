.. container:: not-icpc

   .. rubric:: Problem Types
      :name: problem-types

   There are two types of problems: pass-fail problems and scoring
   problems. In pass-fail problems, submissions are basically judged as
   either accepted or rejected (though the “rejected” judgement is more
   fine-grained and divided into results such as “Wrong Answer”, “Time
   Limit Exceeded”, etc). In scoring problems, a submission that is
   accepted is additionally given a score, which is a numeric value (and
   the goal is to maximize this value).

Problem Metadata
----------------

Metadata about the problem (e.g., source, license, limits) are provided
in a UTF-8 encoded YAML file named ``problem.yaml`` placed in the root
directory of the package.

A typical example is this:

.. code-block:: yaml

    name: Hello Moon
    problem_format_version: 2023-07
    author: Robin McAuthorson
    type: pass-fail
    license: cc by-sa

.. code-block:: yaml

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

        name: Hello World!

    .. code-block:: yaml

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
    multi:
	 indicates that the submission should run multiple 
	 times with inputs generated by the validator, and    

    .. code-block:: yaml
    
        name: Guess
        validation:
            interactive: true

    .. code-block:: yaml
    
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



Problem Timing
--------------

By default, the time limit for a problem is inferred by the judging system based on the the example submissions.

These decisions can me influenced by the specifying values for `time_multipliers` and `time_resolution` in `limits` of `problem.yaml` or overriden altogether by specifying an explicit `time_limit`.

.. code-block:: yaml

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

    The time multipliers specify safety margins relative to the example submissions, see below.

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


Problem Statements
------------------

The problem statement of the problem is provided in the directory
``problem_statement/``.

This directory must contain one file per language, for at least one
language, named ``problem.``\ <language>\ ``.``\ <filetype>, that
contains the problem text itself, including input and output
specifications, but not sample input and output. Language must be given
as the shortest ISO 639 code. If needed a hyphen and a ISO 3166-1
alpha-2 code may be appended to ISO 639 code. Optionally, the language
code can be left out, the default is then English (``en``). Filetype can
be either ``tex`` for LaTeX files, ``md`` for Markdown, or ``pdf`` for
PDF.

Please note that many kinds of transformations on the problem
statements, such as conversion to HTML or styling to fit in a single
document containing many problems will not be possible for PDF problem
statements, so using this format should be avoided if at all possible.

Auxiliary files needed by the problem statement files must all be in
``<short_name>/problem_statement/``. ``problem.<language>.<filetype>``
should reference auxiliary files as if the working directory is
``<short_name>/problem_statement/``. Image file formats supported are
``.png``, ``.jpg``, ``.jpeg``, and ``.pdf``.

A LaTeX file may include the Problem name using the LaTeX command
``\problemname`` in case LaTeX formatting of the title is wanted. If
it’s not included the problem name specified in ``problem.yaml`` will be
used.

The problem statements must only contain the actual problem statement,
no sample data.

Attachments
-----------

Public, i.e. non-secret, files to be made available in addition to the
problem statement and sample test data are provided in the directory
``attachments/``.

Test data
---------

The test data are provided in subdirectories of ``data/``. 
The sample data in ``data/sample/`` and the secret data in ``data/secret/``.

Input and answer files have the filename extension ``.in`` and ``.ans`` respectively.

Annotations
~~~~~~~~~~~

Optionally a hint, a description and an illustration file may be
provided.

The hint file is a text file with filename extension\ ``.hint`` giving a
hint for solving an input file. The hint file is meant to be given as
feedback, i.e. to somebody that fails to solve the problem.

The description file is a text file with filename extension ``.desc``
describing the purpose of an input file. The description file is meant
to be privileged information that explains the purpose of the related
test file, e.g. what cases it’s supposed to test.

The Illustration is an image file with filename extension ``.png``,
``.jpg``, ``.jpeg``, or ``.svg``. The illustration is meant to be
privileged information illustrating the related test file.

Input, answer, description, hint and image files are matched by the base
name.

Interactive Problems
~~~~~~~~~~~~~~~~~~~~

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

Test Data Groups
~~~~~~~~~~~~~~~~

.. container:: not-icpc

   The test data for the problem can be organized into a tree-like
   structure. Each node of this tree is represented by a directory and
   referred to as a test data group. Each test data group may consist of
   zero or more test cases (i.e., input-answer files) and zero or more
   subgroups of test data (i.e., subdirectories).

At the top level, the test data is divided into exactly two groups:
``sample`` and ``secret``. These two groups may be further split into
subgroups as desired.

.. container:: not-icpc

   The result of a test data group is computed by applying a grader to
   all of the sub-results (test cases and subgroups) in the group. See
   `Graders <#graders>`__ for more details.

Test files and groups will be used in lexicographical order on file base
name. If a specific order is desired a numbered prefix such as ``00``,
``01``, ``02``, ``03``, and so on, can be used.


Invalid Input Files
~~~~~~~~~~~~~~~~~~~

In the ``data/`` directory, there may be an ``invalid_inputs/``
directory containing input files that must be rejected by at least one
input validator. These are meant to only test the input validators, and
are not used for judging. The rejected input files can be organized into
a tree-like structure similar to the test data. There may be
``testdata.yaml`` files within this structure, but they may only contain
the key ``input_validator_flags``.

.. container:: not-icpc

   .. rubric:: Included Code
      :name: included-code

   Code that should be included with all submissions are provided in one
   directory per supported language, called ``include/<language>/``.

   The files should be copied from a language directory based on the
   language of the submission, to the submission files before compiling,
   overwriting files from the submission in the case of name collision.
   Language must be given as one of the language codes in the language
   table in the overview section. If any of the included files are
   supposed to be the main file (i.e. a driver), that file must have the
   language dependent name as given in the table referred above.

Example Submissions
-------------------

Correct and incorrect solutions to the problem are provided in
subdirectories of ``submissions/``. The possible subdirectories are:

+--------------+---------------------------------+---------------------+
| Value        | Requirement                     | Comment             |
+==============+=================================+=====================+
| accepted     | Accepted as a correct solution  | At least one is     |
|              | for all test files              | required.           |
+--------------+---------------------------------+---------------------+
| partia       | Overall verdict must be         | Must not be used    |
| lly_accepted | Accepted. Overall score must be | for pass-fail       |
|              | less than ``max_score``.        | problems.           |
+--------------+---------------------------------+---------------------+
| wrong_answer | Wrong answer for some test      |                     |
|              | file, but is not too slow and   |                     |
|              | does not crash for any test     |                     |
|              | file                            |                     |
+--------------+---------------------------------+---------------------+
| time_li      | Too slow for some test file.    |                     |
| mit_exceeded | May also give wrong answer but  |                     |
|              | not crash for any test file.    |                     |
+--------------+---------------------------------+---------------------+
| ru           | Crashes for some test file      |                     |
| n_time_error |                                 |                     |
+--------------+---------------------------------+---------------------+

Every file or directory in these directories represents a separate
solution. Same requirements as for submissions with regards to
filenames. It is mandatory to provide at least one accepted solution.

Submissions must read input data from standard input, and write output
to standard output.

Input Validation
----------------

Input Validators, for verifying the correctness of the input files, are
provided in ``input_validators/``. Input validators can be specified as
VIVA-files (with file ending ``.viva``), Checktestdata-file (with file
ending ``.ctd``), or as a program.

All input validators provided will be run on every input file.
Validation fails if any validator fails.

Input Validator Invocation
~~~~~~~~~~~~~~~~~~~~~~~~~~

An input validator program must be an application (executable or
interpreted) capable of being invoked with a command line call.

All input validators provided will be run on every test data file using
the arguments specified for the test data group they are part of.
Validation fails if any validator fails.

When invoked the input validator will get the input file on stdin.

The validator should be possible to use as follows on the command line:

``./validator [arguments] < inputfile``

Output
~~~~~~

The input validator may output debug information on stdout and stderr.
This information may be displayed to the user upon invocation of the
validator.

Exit codes
~~~~~~~~~~

The input validator must exit with code 42 on successful validation. Any
other exit code means that the input file could not be confirmed as
valid.

Dependencies
^^^^^^^^^^^^

The validator MUST NOT read any files outside those defined in the
Invocation section. Its result MUST depend only on these files and the
arguments.

Output Validator
----------------

An output validator is a program that is given the output of a submitted
program, together with the corresponding input file, and a correct
answer file for the input, and then decides whether the output provided
is a correct output for the given input file.

The output validator provided will be run on the output for every test
data file using the arguments specified for the test data group.

Default Output Validator Specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default output validator is essentially a beefed-up diff. 
In its default mode, it tokenizes the files to compare and compares them token by token. 
It supports the following command-line arguments to control how tokens are compared.

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

When supplying both a relative and an absolute tolerance, the semantics
are that a token is accepted if it is within either of the two
tolerances. When a floating-point tolerance has been set, any valid
formatting of floating point numbers is accepted for floating point
tokens. For instance, if a token in the answer file says ``0.0314``, a
token of ``3.14000000e-2`` in the output file would be accepted.
If no floating point tolerance has been set, floating point tokens are treated
just like any other token and have to match exactly.


Grading
-------

For pass-fail problems, the verdict of a submission is the first
non-accepted verdict, where test cases are run in lexicographical order
of their full file paths (note that ``sample`` comes before ``secret``
in this order).


