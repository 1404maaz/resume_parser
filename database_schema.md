# Database Schema

## Collections

### resumes
Stores parsed resume data.

#### Fields
- name: String
- email: String
- phone: String
- experience: List of Objects
  - job_title: String
  - company: String
  - duration: String
- education: List of Objects
  - degree: String
  - institution: String
  - graduation_year: String
- skills: List of Strings

### taxonomy
Stores the taxonomy for classification.

#### Fields
- category: String
- terms: List of Strings