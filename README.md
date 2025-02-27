# Proposal Evaluation API

This repository contains a Flask-based API for evaluating proposals based on various criteria, including age, salary, medical history, and selected plan.

## Overview

The API provides an endpoint (`/evaluate_proposal`) that accepts JSON data containing proposal details and returns a decision (accepted or rejected) along with reasons for rejection if applicable. The evaluation logic is based on predefined rules and plan-specific conditions.

## Features

* **Plan-based Evaluation:** Proposals are evaluated based on the selected plan, each with its own specific age and salary criteria.
* **Medical History Check:** The API checks for unacceptable medical conditions (cancer, heart disease, stroke).
* **Input Validation:** Robust input validation to ensure data integrity and prevent security vulnerabilities.
* **Clear Error Handling:** Returns informative JSON error messages for invalid input.
* **CORS Support:** Cross-Origin Resource Sharing (CORS) is enabled to allow requests from different origins.
* **Toast Notifications:** Front end uses toast notifications to display the result of the proposal evaluation.

## Technologies Used

* **Python:** Programming language.
* **Flask:** Web framework.
* **Flask-CORS:** CORS support.
* **HTML/JavaScript/Bootstrap:** Front-end implementation.

## Getting Started

### Prerequisites

* Python 3.6+
* pip (Python package installer)

### Installation

1.  Clone the repository:

    ```bash
    git clone [repository URL]
    cd proposal-evaluation-api
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Flask application:

    ```bash
    python app.py
    ```

    The API will be available at `http://127.0.0.1:5000`.

### Front-End Setup

1.  Open the `index.html` file in your web browser.

### API Endpoint

* **`/evaluate_proposal` (POST):**

    * Accepts JSON data with the following fields:
        * `name` (string): Applicant's name.
        * `age` (integer): Applicant's age.
        * `salary` (integer): Applicant's salary.
        * `health_condition` (string): Applicant's medical history (comma-separated).
        * `plan` (string): Selected plan (1, 2, or 3).
    * Returns a JSON response with the evaluation decision.

### Example Request

```json
{
    "name": "John Doe",
    "age": 30,
    "salary": 60000,
    "health_condition": "none",
    "plan": "2"
}



## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request.

## Contact Information
For any questions or issues, feel free to reach out at saksalstha@gmail.com.
