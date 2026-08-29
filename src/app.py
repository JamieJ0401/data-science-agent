
import streamlit as st

from agent.orchestrator import ProjectContext, analyse_project


st.set_page_config(
    page_title="Data Science Implementation Agent",
    page_icon="📊",
    layout="wide",
)


st.title("📊 Data Science Implementation Agent")

st.write(
    "Get help implementing your data science project so you can focus "
    "on the statistical task and analysis."
)

st.header("Tell us about your project")


project_description = st.text_area(
    "Project description",
    placeholder="Briefly describe the problem your project is trying to solve.",
)

statistical_task = st.selectbox(
    "Statistical / data-science task",
    [
        "Select a task",
        "Classification",
        "Regression",
        "Clustering",
        "Time series",
        "Hypothesis testing",
        "Other",
    ],
)

outcome_variable = st.text_input(
    "Outcome / response variable",
    placeholder="e.g. default",
)

predictor_variables = st.text_input(
    "Predictor variables",
    placeholder="e.g. income, age, loan_amount",
)

programming_language = st.selectbox(
    "Programming language",
    [
        "Python",
        "R",
        "SAS",
        "Other",
    ],
)

current_progress = st.text_area(
    "What have you already done?",
    placeholder="Describe what you have completed so far.",
)

project_requirements = st.text_area(
    "Project requirements",
    placeholder="What does your assignment/project require you to do?",
)

existing_code = st.text_area(
    "Existing code",
    placeholder="Paste your existing code here.",
    height=250,
)


if st.button("Analyse My Project", type="primary"):

    context = ProjectContext(
        project_description=project_description,
        statistical_task=statistical_task,
        outcome_variable=outcome_variable,
        predictor_variables=predictor_variables,
        programming_language=programming_language,
        current_progress=current_progress,
        project_requirements=project_requirements,
        existing_code=existing_code,
    )

    response = analyse_project(context)

    st.divider()

    st.header("Project Analysis")

    st.subheader("Current stage")
    st.write(response.current_stage)

    st.subheader("Your next task")
    st.write(response.next_task)

    st.subheader("Recommended approach")
    st.write(response.recommended_approach)

    st.subheader("Implementation")
    st.code(
        response.implementation,
        language=programming_language.lower(),
    )

    st.subheader("Why this approach?")
    st.write(response.explanation)

    st.info(
        "Run the implementation, review the results, and return to the agent "
        "with your output or next question."
    )


