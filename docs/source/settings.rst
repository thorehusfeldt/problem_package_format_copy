*****************************************************
Problem Settings, Output Validation Flags, and Timing
*****************************************************

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
    multi:
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

Problem Timing
--------------

These decisions can me influenced by the specifying values for `time_multipliers` and `time_resolution` in `limits` of `problem.yaml` or overriden altogether by specifying an explicit `time_limit`.

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


Modfifying the Default Output Validator
=======================================

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



