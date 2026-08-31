
def baseline_recommendation(
    statistical_task: str,
    programming_language: str,
    outcome_variable: str,
    predictor_variables: str,
) -> dict:
    """
    Simple baseline recommendation.

    Unlike the agent, this baseline does not inspect the student's
    existing code or project progress.
    """

    task = statistical_task.lower()

    if "classification" in task:
        if programming_language == "Python":
            implementation = f"""from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

predicted_probability = model.predict_proba(X_test)[:, 1]
"""

        elif programming_language == "R":
            implementation = f"""model <- glm(
  {outcome_variable} ~ {predictor_variables.replace(',', ' + ')},
  data = df,
  family = binomial()
)

summary(model)
"""

        else:
            implementation = (
                "# Classification implementation for this language "
                "is not available in the baseline."
            )

        return {
            "current_stage": "Pre-modelling",
            "next_task": "Build a classification model",
            "recommended_approach": (
                "Use logistic regression as a baseline classification model."
            ),
            "implementation": implementation,
            "explanation": (
                "The baseline provides a generic modelling recommendation "
                "without analysing the student's existing project work."
            ),
        }

    return {
        "current_stage": "Project requirements identified",
        "next_task": "Clarify the statistical task",
        "recommended_approach": (
            "The baseline only supports classification projects."
        ),
        "implementation": (
            "# No baseline implementation available for this task."
        ),
        "explanation": (
            "The baseline does not contain workflow-specific reasoning."
        ),
    }

