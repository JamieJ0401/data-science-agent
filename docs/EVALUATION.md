# Evaluation

## Objective

The evaluation tests whether the final agent can identify an appropriate next
data-science implementation step based on a student's project context and
existing code.

The final agent is compared with the original baseline workflow using the same
evaluation cases.

## Evaluation setup

Each case provides:

- Project description
- Statistical task
- Outcome variable
- Predictor variables
- Programming language
- Current progress
- Project requirements
- Existing code

The baseline provides a generic recommendation based primarily on the selected
statistical task.

The final agent additionally inspects the student's existing code and uses
evidence of completed work to determine the current project stage.

## Evaluation cases

| Case | Student state | Expected next step |
|---|---|---|
| 1 | Classification, no model implemented | Build baseline classification model |
| 2 | Classification, logistic regression fitted | Evaluate current model |
| 3 | Classification, model and ROC-AUC evaluation completed | Interpret model results |
| 4 | Classification, predictions already generated | Evaluate predictions |
| 5 | Classification, logistic regression mentioned in progress | Evaluate current model |
| 6 | Classification, model code present but progress description is vague | Evaluate current model |
| 7 | Classification, evaluation code present but model description is vague | Interpret model results |
| 8 | Classification, only data-loading code is present | Build baseline classification model |
| 9 | Classification, logistic regression and evaluation code are present | Interpret model results |
| 10 | Challenging case: progress description conflicts with existing code | Use existing code evidence to determine the appropriate stage |

## Metrics

The primary metric is **next-step identification accuracy**.

A recommendation is considered correct when the agent's recommended next task
matches the expected next step for the evaluation case.

The same cases are applied to both the baseline and final agent.

## Baseline

The baseline implementation provides a generic classification recommendation
without analysing the student's existing project work.

## Final agent

The final agent:

1. Reads the project context.
2. Inspects the student's existing code for evidence of completed work.
3. Identifies the current modelling stage.
4. Considers project requirements.
5. Recommends the next implementation step.
6. Generates implementation guidance in the selected programming language.

## Limitations

This evaluation uses representative test cases rather than a large real-world
student dataset. The cases are designed to test the core behaviour of the
prototype: adapting recommendations to project state and existing code.

## Results

The first three evaluation cases were executed directly against the final
agent implementation.

| Case | Expected next step | Agent result | Correct |
|---|---|---|---|
| 1 | Build baseline classification model | Establish an appropriate baseline classification model | Yes |
| 2 | Evaluate current model | Evaluate the current classification model | Yes |
| 3 | Interpret model results | Interpret the model results and assess statistical significance | Yes |

### Initial result

The agent correctly identified the appropriate next stage for all three tested
cases, giving an initial accuracy of **3/3 (100%)** on these cases.

These results are limited to the three cases executed so far and should not be
interpreted as evidence of general performance.