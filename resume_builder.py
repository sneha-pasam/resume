class Resume:
    def __init__(self, first_name, last_name, objective, location, phone, email, linkedin, other_links, education, projects, skills, certifications, declaration):
        self.first_name = first_name
        self.last_name = last_name
        self.objective = objective
        self.location = location
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.other_links = other_links
        self.education = education
        self.projects = projects
        self.skills = skills
        self.certifications = certifications
        self.declaration = declaration

    def generate_resume(self):
        resume_text = f"Name: {self.first_name} {self.last_name}\n"
        resume_text += f"Objective: {self.objective}\n"
        resume_text += f"Location: {self.location}\n"
        resume_text += f"Phone: {self.phone}\n"
        resume_text += f"Email: {self.email}\n"
        resume_text += f"LinkedIn: {self.linkedin}\n"
        resume_text += f"Other Links: {self.other_links}\n\n"
        
        resume_text += "EDUCATION:\n"
        for edu in self.education:
            resume_text += f"{edu}\n"
        
        resume_text += "\nPROJECTS:\n"
        for project in self.projects:
            resume_text += f"{project}\n"
        
        resume_text += "\nSKILLS:\n"
        for skill, description in self.skills.items():
            resume_text += f"{skill} - {description}\n"
        
        resume_text += "\nCERTIFICATIONS:\n"
        for cert in self.certifications:
            resume_text += f"- {cert}\n"
        
        resume_text += "\nDECLARATION:\n"
        resume_text += self.declaration

        return resume_text

# Personal Details
first_name = "SNEHA"
last_name = "PASAM"
objective = "To pursue a career in technology and acquire knowledge, while leveraging my skills and passion to contribute meaningfully to innovative projects and organizational success."
location = "Narasaraopet, Andhra Pradesh"
phone = "+91 9100410084"
email = "snehapasam63@gmail.com"
linkedin = "www.linkedin.com/in/snehapasam"
other_links = "Twitter/Blog/Portfolio"

# Education
education = [
    "Bachelor of Technology | Ideal institute of technology, Kakinada, 2019 – 2023 | CGPA 6.95",
    "Intermediate | Sri Chaitanya junior college, Narasaraopet, 2017 – 2019 | CGPA 9.42",
    "10th Standard | Sri Chaitanya high school, Narasaraopet, 2017 | CGPA 9.0"
]

# Projects
projects = [
    "Automatic Timetable Generator: Developed a college project Automatic Timetable Generator using Python, GitHub, VS Code.",
    "Fire Detection System: Developed an AI/ML-based Fire Detection System for an Edunet course for TechSaksham."
]

# Skills
skills = {
    "Python": "Proficient in Python programming language, with a strong understanding of its syntax, data structures, and object-oriented principles.",
    "Java": "Familiar with Java programming language fundamentals, including variables, control structures, and basic object-oriented concepts.",
    "GitHub": "Experienced in version control using Git and GitHub, including repository management, branching, merging.",
    "AWS": "Knowledgeable about Amazon Web Services (AWS) fundamentals, including core services such as EC2, S3, and IAM, with an understanding of cloud computing concepts and basic deployment practices."
}

# Certifications
certifications = [
    "Getting started with DevOps on AWS – AWS Training and Certification",
    "Introduction to AWS Command Line Interface (CLI)",
    "AWS Cloud Development Kit Primer",
    "Improve Code Quality with Amazon CodeGuru Reviewer",
    "Advanced Testing practices using AWS DevOps Tools",
    "Introduction to Containers",
    "Cloud Foundations - AWS Academy"
]

# Declaration
declaration = "I hereby declare that all the information provided above is true to the best of my knowledge and belief."

# Create Resume Object
resume = Resume(first_name, last_name, objective, location, phone, email, linkedin, other_links, education, projects, skills, certifications, declaration)

# Generate Resume
print(resume.generate_resume())
