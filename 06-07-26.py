import requests
import pandas as pd
import re
from collections import Counter
url = "https://boards-api.greenhouse.io/v1/boards/stripe/jobs?content=true"

response = requests.get(url)
jobs = response.json()["jobs"]

data = []

# Simple skill keywords
skill_keywords = [
    "Python", "Java", "SQL", "AWS", "Docker", "Kubernetes",
    "TensorFlow", "PyTorch", "Machine Learning", "React",
    "Node.js", "JavaScript", "Git", "Linux", "Spark"
]

for job in jobs:

    title = job.get("title", "")

    company = "Stripe"

    location = job.get("location", {}).get("name", "")

    posting_date = job.get("updated_at", "")

    apply_link = job.get("absolute_url", "")

    description = job.get("content", "")

    # Extract skills from description
    found_skills = []
    for skill in skill_keywords:
        if re.search(rf"\b{re.escape(skill)}\b", description, re.IGNORECASE):
            found_skills.append(skill)

    skills = ", ".join(found_skills)



    data.append({
        "Job Title": title,
        "Company Name": company,
        "Skills": skills,
        "Location": location,
        "Posting Date": posting_date,
        "Apply Link": apply_link
    })

df = pd.DataFrame(data)

print(df)

df.to_csv("jobs.csv", index=False)
import pandas as pd
import numpy as np
df=pd.read_csv("jobs.csv")
print(df.head(5))
print('null values ',df.isnull().sum())
# df["Skills"]=df['Skills'].fillna(df["Skills"].mode()[0])
# df["Location"]=df['Location'].fillna(df["Location"].mode()[0])
df=df.dropna()
print('null values ',df.isnull().sum())
print("shape",df.shape,"\n","info",df.info(),"\n")
print("duplicated",df.duplicated().sum())
import matplotlib.pyplot as plt
df["Posting Date"] = pd.to_datetime(df["Posting Date"], errors="coerce")
print(df["Posting Date"].head(5))
df["Month"] = df["Posting Date"].dt.to_period("M")

hiring_trend = df.groupby("Month").size()

print("\nHiring Trend")
print(hiring_trend)

trending_role=df["Job Title"].value_counts()
print(trending_role.head(5))

frequent_opening_companys=df['Company Name'].value_counts()
print(frequent_opening_companys.head(5))

top_hiring_loc=df["Location"].value_counts()
print(top_hiring_loc.head(5))

skills = []

for item in df["Skills"].dropna():

    for skill in str(item).split(","):

        skill = skill.strip()

        if skill != "":
            skills.append(skill)

skill_count = Counter(skills)

skill_df = pd.DataFrame(skill_count.items(),
                        columns=["Skill", "Count"])

skill_df = skill_df.sort_values(
    by="Count",
    ascending=False
)

print("\nTop Skills")
print(skill_df.head(15))


plt.figure(figsize=(10,5))
hiring_trend.plot(marker='o')
plt.title("Hiring Trend")
plt.xlabel("Month")
plt.ylabel("Number of Jobs")
plt.show()

plt.figure(figsize=(10,6))
frequent_opening_companys.head(20).plot(kind="bar")
plt.title("Top Companies Hiring")
plt.ylabel("Number of Jobs")
plt.show()

plt.figure(figsize=(10,6))
top_hiring_loc.head(10).plot(kind="bar")
plt.title("Top Hiring Locations")
plt.ylabel("Jobs")

plt.show()


plt.figure(figsize=(12,6))
skill_df.head(10).plot(
    x="Skill",
    y="Count",
    kind="bar"
)
plt.title("Most Demanded Skills")
plt.ylabel("Frequency")
plt.show()

if "Salary" in df.columns:

    plt.figure(figsize=(8,5))
    df["Salary"].dropna().plot(kind="hist", bins=20)
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.tight_layout()
    plt.show()



top_hiring_loc.to_csv("location_analysis.csv")

trending_role.to_csv("job_roles_analysis.csv")

skill_df.to_csv("skills_analysis.csv", index=False)

print("\nEDA Completed Successfully!")
# plt.hist(df["Company Name"])
# plt.show()

