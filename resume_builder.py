import datetime

class Resume:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d")

    def format_section(self, title, content):
        return f"\n{'='*30}\n{title.upper()}\n{'='*30}\n{content}"

    def generate_text(self):
        header = (
            f"{self.data['first_name']} {self.data['last_name']}\n"
            f"{self.data['location']}\n"
            f"Email: {self.data['email']} | LinkedIn: {self.data['linkedin']}\n"
            f"Phone: {self.data['phone']}\n"
        )
        
        body = self.format_section("Professional Summary", self.data['objective'])
        
        # Experience Section
        exp_str = ""
        for job in self.data['experience']:
            exp_str += f"• {job['role']} | {job['company']} ({job['duration']})\n"
            exp_str += f"  {job['description']}\n\n"
        body += self.format_section("Experience", exp_str.strip())
        
        # Education Section
        edu_str = "\n".join([f"• {e}" for e in self.data['education']])
        body += self.format_section("Education", edu_str)
        
        # Projects Section
        proj_str = ""
        for p in self.data['projects']:
            proj_str += f"• {p['title']}: {p['desc']}\n"
        body += self.format_section("Projects", proj_str.strip())
        
        # Skills Section
        skill_str = ""
        for category, skills in self.data['skills'].items():
            skill_str += f"• {category}: {', '.join(skills)}\n"
        body += self.format_section("Technical Skills", skill_str.strip())
        
        # Certifications
        cert_str = "\n".join([f"• {c}" for c in self.data['certifications']])
        body += self.format_section("Certifications", cert_str)
        
        return header + body + f"\n\nGenerated on: {self.timestamp}"

    def save_to_file(self, filename="Sneha_Pasam_Experience_Resume.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.generate_text())
        print(f"Success! File saved as {filename}")

# Updated Data with LinkedIn Experience
resume_data = {
    "first_name": "SNEHA",
    "last_name": "PASAM",
    "objective": "Aspiring Cloud and DevOps Professional passionate about automation, infrastructure management, and building scalable systems.",
    "location": "Hyderabad, Telangana, India",
    "phone": "+91 9100410084",
    "email": "snehapasam63@gmail.com",
    "linkedin": "linkedin.com/in/snehapasam-768a6922b",
    "experience": [
        {
            "role": "Software Engineer – Terminal Bench (Remote)",
            "company": "Dusker AI",
            "duration": "Dec 2025 - Present",
            "description": "Engineering AI evaluation benchmarks in Linux environments. Focused on Docker containerization, Bash automation, and systems debugging."
        },
        {
            "role": "AWS Cloud Intern",
            "company": "F13 Technologies",
            "duration": "Dec 2024 - May 2025",
            "description": "Hands-on experience with EC2, S3, and Load Balancers. Collaborated on cloud infrastructure simulations and customer case studies."
        }
    ],
    "education": [
        "B.Tech in Computer Science | Ideal Institute of Technology (2019-2023) | CGPA 6.95",
        "Intermediate | Sri Chaitanya Junior College (2017-2019) | CGPA 9.42"
    ],
    "projects": [
        {"title": "CI/CD Pipeline Automation", "desc": "Jenkins, GitHub, Docker, and Kubernetes integration for automated software delivery."},
        {"title": "Automatic Timetable Generator", "desc": "Genetic Algorithm based scheduling using Python, Tkinter, and SQLite."}
    ],
    "skills": {
        "Cloud/DevOps": ["AWS", "Docker", "Kubernetes", "CI/CD", "Jenkins"],
        "Systems": ["Linux", "Bash Scripting", "Infrastructure Management"],
        "Programming": ["Python", "Java", "Genetic Algorithms"]
    },
    "certifications": [
        "AWS Partner: Accreditation (Technical) - Jan 2025",
        "AWS Partner: Cloud Economics - Jan 2025",
        "Cloud Foundations - AWS Academy"
    ]
}

if __name__ == "__main__":
    my_resume = Resume(resume_data)
    my_resume.save_to_file()
