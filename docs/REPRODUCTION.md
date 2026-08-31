# Reproduction Guide

## Requirements

* Python 3.9+
* Git
* A terminal
* A web browser

The project does not require a paid API or external AI service to run the demonstrated workflow.

## 1. Clone the repository

```bash
git clone https://github.com/JamieJ0401/data-science-agent.git
cd data-science-agent
```

## 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Verify the project

Run:

```bash
python -m py_compile src/agent/orchestrator.py
python -m py_compile src/baseline.py
```

No output indicates that the files compiled successfully.

## 5. Run the application

```bash
streamlit run src/app.py
```

The application will open in a browser.

## 6. Demonstrated workflow

The application accepts information about a student's project, including:

* Project description
* Statistical/data-science task
* Outcome variable
* Predictor variables
* Programming language
* Current progress
* Project requirements
* Existing code

The agent analyses this information and recommends the next appropriate implementation step.

For the demonstrated classification workflow:

1. If no model is detected, the agent recommends establishing a baseline classification model.
2. If a logistic regression model is detected, the agent recommends evaluating the model.
3. If model evaluation is already detected, the agent recommends interpreting the results.

This progression demonstrates that the agent considers the student's existing work rather than simply returning the same generic modelling recommendation.

## 7. Baseline comparison

The repository also contains a simple baseline implementation:

```bash
python -c "from src.baseline import baseline_recommendation; print(baseline_recommendation('Classification', 'Python', 'default', 'income, age, loan_amount'))"
```

The baseline provides a generic classification recommendation without analysing the student's existing project code or progress.

This provides a simple reference point for comparing the behaviour of the project-aware agent.
