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

