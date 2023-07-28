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

    problem ID

        The unique, short name of the problem used for the problem's directory,
       	sometimes referred to as its ``<problem_id>``. 
	For instance, the problem ID of the problem whose English name is *Hello World!* is ``hello``.
	The problem ID matches ``[a-z0-9]+``.

    problem name

        The name of a problem in a natural language, such as *Hello World!*.
	All problems need at least one name;
       	most problems have an English name.
