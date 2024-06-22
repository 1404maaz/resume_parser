# Resume Parser

## Project Description
This project provides a set of API services to parse resumes and extract relevant data attributes, such as personal information, professional experience, education, and skills.

## Setup and Installation

1. Clone the repository:
    
    git clone https://github.com/yourusername/resume_parser.git
    cd resume_parser
    

2. Install dependencies:
    
    pip install -r requirements.txt
    

3. Start the Flask server:
    
    python app.py
    

4. MongoDB should be running locally on the default port.

## Usage

### Parse a Resume
Endpoint: /parse
Method: POST
Form-data:
- file: The resume file to be parsed.

### Get Taxonomy
Endpoint: /taxonomy
Method: GET

## API Example Requests

- Parsing a resume using curl:
    
    curl -X POST -F 'file=@resume.pdf' http://127.0.0.1:5000/parse
    

## Taxonomy
Refer to taxonomy.md for the detailed classification taxonomy.

## Database Schema
Refer to database_schema.md for the database schema.