# Project Specification

## Problem

Data science projects often require students to spend significant amounts of time searching for appropriate code, adapting examples from different sources, and troubleshooting implementation issues.

However, the primary purpose of many data science projects is not the coding itself. Students are expected to perform an appropriate statistical or data-science task, analyse their data, interpret the results, and answer the underlying research or business question.

The Data Science Implementation Agent aims to reduce the time and effort spent on the coding and implementation aspects of a project, allowing students to focus more of their time on the statistical reasoning, analysis, and interpretation that the project actually requires.

## Proposed Solution

The Data Science Implementation Agent assists students in progressing through their existing data science projects by using the work they have already completed and the requirements of their project to help implement the appropriate analysis.

Rather than requiring students to start from scratch or search extensively for suitable code, the agent helps identify and implement relevant approaches within the context of the student's own project.

The agent is intended to support the student through the implementation process while keeping the statistical task and analytical objective at the centre of the workflow.

## Student Inputs

The student provides:

* Existing code
* Outcome or response variable
* Predictor variables
* Desired programming language
* Work already completed
* Project requirements and relevant constraints

## Core Objective

The core objective is to **reduce implementation and code-search time while helping students progress through their data science projects so that they can focus on the statistical task, analysis, interpretation, and conclusions.**

## Guiding Principle

> The coding is a means to complete the data science task, not the task itself.

The agent should therefore prioritise understanding the student's analytical objective and existing work before suggesting or generating implementation.

## Agent Workflow

The agent follows an iterative workflow rather than attempting to complete the entire project in a single step.

### 1. Understand the project

The agent first interprets the student's project requirements, analytical objective, outcome variable, predictor variables, programming language, and any relevant constraints.

### 2. Inspect existing work

The agent examines the student's existing code and work to determine:

* What has already been completed
* What approaches have already been attempted
* Whether the existing implementation is appropriate
* Where errors, gaps, or incomplete sections exist

### 3. Determine the student's current stage

The agent identifies what the student is currently trying to accomplish and what remains to be done.

The agent should not assume that every student requires the same workflow or that every project should begin with data cleaning or end with the same statistical model.

### 4. Identify the next required task

Based on the project requirements and the student's current progress, the agent determines the most appropriate next implementation step.

The focus should remain on the statistical or analytical objective rather than simply generating additional code.

### 5. Use existing code first

Where possible, the agent adapts and improves the student's existing code rather than replacing it unnecessarily.

This preserves the student's workflow and reduces unnecessary redevelopment.

### 6. Supplement with relevant examples

When the student's existing code is insufficient, the agent can identify relevant code examples, templates, or implementation patterns and adapt them to the student's project.

The goal is to reduce the time students spend searching for and adapting appropriate code themselves.

### 7. Explain the implementation

The agent should explain what was changed or generated and how it relates to the student's analytical task.

The student should be able to understand why an implementation is being recommended rather than receiving unexplained code.

### 8. Allow iterative progress

After completing or addressing the current implementation step, the student can provide the resulting code or output and continue working with the agent.

The workflow therefore operates as an iterative cycle:

**Understand → Inspect → Identify → Implement → Explain → Continue**

This allows the agent to support students at different stages of their projects rather than forcing every project through a fixed pipeline.


## Implementation Sources

The agent can draw on multiple sources when determining how to implement the next stage of a student's project.

### Source Priority

The agent should generally prioritise sources in the following order:

1. **Student's existing code** — adapt and improve the student's current implementation where appropriate.
2. **Student's project files and previous work** — use relevant code, outputs, and documentation already provided by the student.
3. **Curated implementation examples** — use reliable, project-relevant examples and templates maintained as part of the system.
4. **External resources** — consult relevant web resources when additional information or implementation examples are required.
5. **LLM knowledge and reasoning** — synthesise information, fill gaps, adapt implementations, and explain the resulting approach.

The agent should use these sources together rather than relying exclusively on generated code.

The purpose of using multiple sources is to reduce the student's time spent searching for suitable implementations while maintaining context with the student's existing project and analytical requirements.

## Student Intake

The agent should collect structured information about the student's project before providing implementation assistance.

### Required Inputs

* **Project description** — a brief description of the research, academic, or business problem.
* **Statistical or data-science task** — the type of analysis or modelling task the student needs to perform.
* **Outcome/response variable** — the variable the student is attempting to explain or predict.
* **Predictor variables** — the variables intended to be used as explanatory or predictive variables.
* **Programming language** — the language the student is required or prefers to use.
* **Current progress** — a description of what the student has already completed.
* **Project requirements** — relevant requirements, questions, or constraints that the implementation must satisfy.
* **Existing code** — the student's current implementation, where available.

### Optional Inputs

The student may also provide:

* Dataset description
* Previous analysis or model output
* Error messages
* Assignment rubric or project instructions
* Lecturer or supervisor requirements
* Additional project files
* Previous implementation attempts

### Dataset Requirement

The initial version of the agent does not require the student to upload the underlying dataset.

The agent instead works primarily from the student's existing code, project description, variables, requirements, progress, and other supporting information.

This keeps the focus on implementation assistance and allows the student to retain responsibility for their data and analysis.

### Intake Objective

The purpose of the intake process is to give the agent sufficient context to understand:

1. What the student is trying to accomplish.
2. What the student has already done.
3. What they are required to do.
4. What implementation problem they currently need help with.
5. What programming environment they are working in.
