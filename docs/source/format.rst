Problem Package Format
======================

This is the ``2023-07-draft`` version of the Kattis problem package
format.

Overview
--------

This document describes the format of a *Kattis problem package*, used
for distributing and sharing problems for algorithmic programming
contests as well as educational use.

General Requirements
~~~~~~~~~~~~~~~~~~~~

The package consists of a single directory containing files as described
below. The name of the directory must consist solely of lower case
letters a-z and digits 0-9. Alternatively it can be a ZIP compressed
archive of such a directory with identical base name and extension
``.kpp`` or ``.zip``.

All file names for files included in the package must match the
following regexp:

``[a-zA-Z0-9][a-zA-Z0-9_.-]*[a-zA-Z0-9]``

I.e., it must be of length at least 2, consist solely of lower or upper
case letters a-z, A-Z, digits 0-9, period, dash or underscore, but must
not begin or end with period, dash or underscore.

All text files for a problem must be UTF-8 encoded and not have a byte
order mark.

All floating point numbers must be given as the external character
sequences defined by IEEE 754-2008 and may use up to double precision.

Programs
~~~~~~~~

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
