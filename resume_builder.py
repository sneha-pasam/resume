import datetime

class Resume:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d")

    def format_section(self, title, content):
        return f"\n{'='*20}\n{title.upper()}\n{'='*20}\n{content}"

    def generate_text(self):
        # Header Section
        header = (
            f"{self.data['first_name']} {self.data['last_name']}\n"
            f"{self.data['location']} | {self.data['phone']}\n"
            f"Email: {self.data['email']} | LinkedIn: {self.data['linkedin']}\n"
        )
        
        # Build Body
        body = self.format_section("Objective", self.data['objective'])
        
        edu_str = "\n".join([f"• {e}" for e in self.data['education']])
        body += self.format_section("Education", edu_str)
        
        proj_str = "\n".join([f"• {p}" for p in self.data['projects']])
        body += self.format_section("Projects", proj_str)
        
        skill_str = "\n".join([f"• {k}: {v}" for k, v in self.data['skills'].items()])
        body += self.format_section("Skills", skill_str)
        
        cert_str = "\n".join([f"• {c}" for c in self.data['certifications']])
        body += self.format_section("Certifications", cert_str)
        
        footer = f"\n\nDeclaration: {self.data['declaration']}\nGenerated on: {self.timestamp}"
        
        return header + body + footer

    def save_to_file(self, filename="Sneha_Pasam_Resume.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.generate_text())
        print(f"Success! Resume saved as {filename}")

# Centralized Data Dictionary
resume_data = {
    "first_name": "SNEHA",
    "last_name": "PASAM",
    "objective": "To pursue a career in technology and acquire knowledge, while leveraging my skills and passion to contribute meaningfully to innovative projects.",
    "location": "Narasaraopet, Andhra Pradesh",
    "phone": "+91 9100410084",
    "email": "snehapasam63@gmail.com",
    "linkedin": "linkedin.com/in/snehapasam",
    "education": [
        "B.Tech | Ideal Institute of Technology, Kakinada (2019–2023) | CGPA 6.95",
        "Intermediate | Sri Chaitanya Junior College (2017–2019) | CGPA 9.42",
        "10th | Sri Chaitanya High School (2017) | CGPA 9.0"
    ],
    "projects": [
        "Automatic Timetable Generator: Python-based scheduling system using Git/VS Code.",
        "Fire Detection System: AI/ML-based system developed for TechSaksham (Edunet)."
    ],
    "skills": {
        "Python": "Syntax, Data Structures, and OOP principles.",
        "Cloud": "AWS (EC2, S3, IAM), Cloud Foundations.",
        "DevOps": "Version Control (Git/GitHub), CI/CD concepts.",
        "Java": "Fundamental programming and basic OOP."
    },
    "certifications": [
        "Getting started with DevOps on AWS",
        "Introduction to AWS CLI",
        "AWS Cloud Development Kit Primer",
        "Cloud Foundations - AWS Academy"
    ],
    "declaration": "I hereby declare that all the information provided above is true to the best of my knowledge."
}

if __name__ == "__main__":
    my_resume = Resume(resume_data)
    print(my_resume.generate_text())
    my_resume.save_to_file()
