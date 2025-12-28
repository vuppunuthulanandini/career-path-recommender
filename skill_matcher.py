import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------
# Load dataset
# ---------------------------
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, "data", "job_roles.csv")
df = pd.read_csv(csv_path)

# ---------------------------
# Take user input
# ---------------------------
user_input = input("Enter your skills (comma separated): ")
user_skills = set([s.strip().lower() for s in user_input.split(",")])

results = []

# ---------------------------
# Compare user skills with roles
# ---------------------------
for _, row in df.iterrows():
    role = row["role"]
    role_skills = set(row["skills_required"].split(";"))
    
    matched = user_skills.intersection(role_skills)
    missing = role_skills - user_skills
    
    match_percent = round((len(matched)/len(role_skills))*100, 2)

    results.append({
        "role": role,
        "match_percent": match_percent,
        "skills_have": ", ".join(matched),
        "skills_missing": ", ".join(missing)
    })

# ---------------------------
# Sort results by match percentage
# ---------------------------
results_df = pd.DataFrame(results).sort_values(by="match_percent", ascending=False)

# ---------------------------
# Display results
# ---------------------------
print("\n--- Career Match Results ---\n")
for _, r in results_df.iterrows():
    print(f"Role: {r.role}")
    print(f"Match: {r.match_percent}%")
    print(f"Skills you have: {r.skills_have}")
    print(f"Missing skills: {r.skills_missing}")
    print("-"*40)

# ---------------------------
# Visualization for top role
# ---------------------------
top_role = results_df.iloc[0]
have_skills = top_role['skills_have'].split(", ") if top_role['skills_have'] else []
missing_skills = top_role['skills_missing'].split(", ") if top_role['skills_missing'] else []

if have_skills or missing_skills:
    plt.figure(figsize=(8,5))
    if have_skills:
        plt.bar(have_skills, [1]*len(have_skills), color='green', label='Have')
    if missing_skills:
        plt.bar(missing_skills, [1]*len(missing_skills), color='red', label='Missing')
    plt.title(f"Skill Gap for {top_role['role']}")
    plt.ylabel('Skills')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ---------------------------
# Suggested next skills
# ---------------------------
if missing_skills:
    print("\nSuggested skills to learn next for your top role:")
    for skill in missing_skills:
        print(f"- {skill}")
