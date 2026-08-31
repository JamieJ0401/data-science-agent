
from dataclasses import dataclass


def inspect_existing_code(code: str) -> dict:
    """
    Identify simple indicators of work already completed
    in the student's existing code.
    """

    code_lower = code.lower()

    return {
        "has_data_loading": any(
            keyword in code_lower
            for keyword in [
                "read_csv",
                "read.csv",
                "pd.read",
                "proc import",
            ]
        ),
        "has_logistic_model": any(
            keyword in code_lower
            for keyword in [
                "logisticregression",
                "smf.logit",
                "glm(",
                "proc logistic",
            ]
        ),
        "has_predictions": any(
            keyword in code_lower
            for keyword in [
                "predict(",
                ".predict(",
                "predict_proba",
            ]
        ),
        "has_evaluation": any(
            keyword in code_lower
            for keyword in [
                "roc_auc",
                "roc(",
                "confusion_matrix",
                "classification_report",
                "auc(",
            ]
        ),
    }


@dataclass
class ProjectContext:
    project_description: str
    statistical_task: str
    outcome_variable: str
    predictor_variables: str
    programming_language: str
    current_progress: str
    project_requirements: str
    existing_code: str


@dataclass
class AgentResponse:
    current_stage: str
    next_task: str
    recommended_approach: str
    implementation: str
    explanation: str


def analyse_project(context: ProjectContext) -> AgentResponse:
    """
    Analyse a student's current project context and identify
    the most appropriate next implementation step.
    """

    progress = context.current_progress.lower()
    requirements = context.project_requirements.lower()
    task = context.statistical_task.lower()
    code_analysis = inspect_existing_code(context.existing_code)

    if "classification" in task:

        if (
            "logistic" in progress
            or "logistic regression" in progress
            or code_analysis["has_logistic_model"]
        ):

            # If evaluation has already been performed,
            # move the student toward interpretation instead
            # of generating the same evaluation code again.
            if code_analysis["has_evaluation"]:
                return AgentResponse(
                    current_stage="Model evaluation completed",
                    next_task=(
                        "Interpret the model results and assess "
                        "statistical significance"
                    ),
                    recommended_approach=(
                        "Review model performance metrics, coefficient estimates, "
                        "statistical significance and practical relevance before "
                        "deciding whether further modelling is required."
                    ),
                    implementation=(
                        "# Interpretation should be based on the model results."
                    ),
                    explanation=(
                        "Your existing code already contains model evaluation "
                        "steps. The next stage is therefore to interpret the "
                        "results rather than repeating the evaluation."
                    ),
                )

            if any(
                word in requirements
                for word in ["evaluate", "evaluation", "performance", "compare"]
            ):
                return AgentResponse(
                    current_stage="Initial modelling completed",
                    next_task="Evaluate the current classification model",
                    recommended_approach=(
                        "Assess discrimination and classification performance "
                        "using a confusion matrix, ROC-AUC, sensitivity and specificity."
                    ),
                    implementation=_classification_evaluation_code(
                        context.programming_language,
                        has_predictions=code_analysis["has_predictions"],
                    ),
                    explanation=(
                        "You have already fitted a logistic regression model. "
                        "The project requirements indicate that model evaluation "
                        "is the next appropriate step, so generating another model "
                        "would be premature."
                    ),
                )

            return AgentResponse(
                current_stage="Initial model implemented",
                next_task="Inspect and validate the logistic regression model",
                recommended_approach=(
                    "Check model assumptions, coefficient estimates, "
                    "multicollinearity and model diagnostics."
                ),
                implementation=_logistic_diagnostics_code(
                    context.programming_language
                ),
                explanation=(
                    "Because an initial logistic regression has already been "
                    "implemented, the next step should be validation rather than "
                    "restarting the modelling process."
                ),
            )

        return AgentResponse(
            current_stage="Pre-modelling",
            next_task="Establish an appropriate baseline classification model",
            recommended_approach=(
                "For a binary outcome, logistic regression provides an interpretable "
                "baseline before considering more complex models."
            ),
            implementation=_logistic_baseline_code(
                context.programming_language,
                context.outcome_variable,
                context.predictor_variables,
            ),
            explanation=(
                "The project is a classification problem and no classification "
                "model is identified in the existing progress. A baseline model "
                "provides an interpretable starting point for the analysis."
            ),
        )

    return AgentResponse(
        current_stage="Project requirements identified",
        next_task="Clarify the next statistical implementation step",
        recommended_approach=(
            "The current prototype supports classification workflows. "
            "Additional statistical tasks will be added iteratively."
        ),
        implementation="# Implementation will be added for this task.",
        explanation=(
            "The agent has identified that the requested task is outside "
            "the current prototype's supported workflow."
        ),
    )


def _logistic_baseline_code(language, outcome, predictors):
    if language == "Python":
        return f"""import statsmodels.formula.api as smf

model = smf.logit(
    "{outcome} ~ {predictors.replace(',', ' + ')}",
    data=df
).fit()

print(model.summary())
"""

    if language == "R":
        return f"""model <- glm(
  {outcome} ~ {predictors.replace(',', ' + ')},
  data = df,
  family = binomial()
)

summary(model)
"""

    return "# Baseline implementation for this language will be added."


def _logistic_diagnostics_code(language):
    if language == "Python":
        return """from sklearn.metrics import classification_report, roc_auc_score

predicted_probability = model.predict_proba(X_test)[:, 1]
predicted_class = (predicted_probability >= 0.5).astype(int)

print(classification_report(y_test, predicted_class))
print("ROC-AUC:", roc_auc_score(y_test, predicted_probability))
"""

    if language == "R":
        return """library(pROC)

probabilities <- predict(model, type = "response")
roc_curve <- roc(df$y, probabilities)

auc(roc_curve)
"""

    return "# Diagnostic implementation for this language will be added."


def _classification_evaluation_code(language, has_predictions=False):
    if language == "Python":

        if has_predictions:
            return """from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score
)

predicted_class = (predicted_probability >= 0.5).astype(int)

print(confusion_matrix(y_test, predicted_class))
print(classification_report(y_test, predicted_class))
print("ROC-AUC:", roc_auc_score(y_test, predicted_probability))
"""

        return """from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score
)

predicted_probability = model.predict_proba(X_test)[:, 1]
predicted_class = (predicted_probability >= 0.5).astype(int)

print(confusion_matrix(y_test, predicted_class))
print(classification_report(y_test, predicted_class))
print("ROC-AUC:", roc_auc_score(y_test, predicted_probability))
"""

    if language == "R":
        return """library(pROC)

probabilities <- predict(model, type = "response")
predicted_class <- ifelse(probabilities >= 0.5, 1, 0)

table(Predicted = predicted_class, Actual = df$y)

roc_curve <- roc(df$y, probabilities)
auc(roc_curve)
"""

    return "# Classification evaluation for this language will be added."

