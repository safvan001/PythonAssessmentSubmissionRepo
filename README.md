# PythonAssessmentSubmissionRepo

# GitHub Repository Search

## Overview
This Django web application integrates with the GitHub API to search for repositories by name and display details such as the repository name, owner, description, stars, and forks. It includes pagination and stores search results in a SQLite database.

## Features
- **API Integration:** Search GitHub repositories using the GitHub API.
- **Pagination:** Display up to 10 repositories per page in search results.
- **Database Storage:** Save repository data in a SQLite database.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher
- pip (Python package installer)

## Setup and Installation
Follow these steps to get your development env running:

**Clone the repository**
git clone (https://github.com/safvan001/PythonAssessmentSubmissionRepo)
cd github_project
**Activate Virtual env**:venv\Scripts\activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

