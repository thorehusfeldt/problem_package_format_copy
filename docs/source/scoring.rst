Scoring Problems
================

Nothing of this is part of the ICPC specification.

In scoring problems, a submission that is
accepted is additionally given a score, which is a numeric value (and
the goal is to maximize this value).


Test Data Settings
------------------

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

    The maximum score allowed for this test group. It is an error to exceed this.              |

    **Default:** The sum/mininum of ``score`` and the subresults’ ``max_score`` values, dependinding on if
     ``score_aggregation`` is ``"sum"``/``"min"``.

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

.. code-block:: txt
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
