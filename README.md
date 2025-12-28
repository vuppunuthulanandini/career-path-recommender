# Career Path Recommender
A Python project that recommends suitable career paths based on the user's skills. 
It calculates the percentage match for each role, shows skills you have and skills missing, 
and provides visual skill gap analysis for the top recommended role.
## Features
- Suggests career roles based on user skills
- Calculates match percentage for each role
- Highlights missing skills to improve
- Visualizes skill gap with a bar chart for top role
## Dataset
The dataset `data/job_roles.csv` contains roles and required skills:

| Role          | Skills Required                               |
|---------------|-----------------------------------------------|
| Data Analyst  | python;sql;excel;power bi;statistics;pandas  |
| BI Developer  | power bi;sql;dax;data modeling;excel         |
| ML Intern     | python;numpy;pandas;scikit-learn;mathematics |
| Data Engineer | python;sql;etl;data pipelines;cloud          |
## How to Run
1. Clone the repository:
2. Navigate to the project folder:
3. Install dependencies (if needed):
4. Run the script:
5. Enter your skills (comma separated) when prompted.
--- Career Match Results ---

Role: Data Analyst
Match: 66.67%
Skills you have: python, sql, excel, pandas
Missing skills: power bi, statistics
----------------------------------------
## Future Improvements
- Add more roles and skills to the dataset
- Use Streamlit to create a web dashboard
- Add skill weighting for smarter match calculation
## Technologies Used
- Python
- Pandas
- Matplotlib
<img width="778" height="551" alt="image" src="https://github.com/user-attachments/assets/f1af605c-5cba-4aa4-857f-61d495407206" />

<img width="768" height="506" alt="image" src="https://github.com/user-attachments/assets/136e90a3-642f-4690-9bf5-73c8de2c5535" />

