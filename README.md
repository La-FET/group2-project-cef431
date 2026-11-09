# Student Grade Calculator – Jenkins CI Pipeline

**Group 2 – Software Quality Tools (CEF431)**
Objective: set up a CI pipeline using Jenkins that runs automated tests for a project hosted on GitHub.

## What the project does
`grade_calculator.py` takes a list of student scores and returns:
- the **average** (rounded to 2 decimals)
- the **letter grade**: A (≥80), B (≥70), C (≥60), D (≥50), F (<50)
- whether the student **passed** (average ≥ 50)

Invalid input (empty lists, scores below 0 or above 100, non-numbers) raises an error.

## Project files
| File | Purpose |
|---|---|
| `grade_calculator.py` | The application code |
| `test_grade_calculator.py` | Automated tests (pytest) |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files Git should ignore |

## 1. Run the tests on your own computer
```bash

# set up virtual environment
python3 -m venv venv

# activate virtual environment
# windows
venv\Scripts\activate.bat 

# mac / linux systems
source venv/bin/activate

# install dependencies
pip install -r requirements.txt


pytest -v
```

