import random
import pandas as pd

# Define the data for the books and courses
books = {
    "Software Engineering": [
        "Clean Code", "Refactoring", "Continuous Delivery", "Working Effectively with Legacy Code",
        "The Mythical Man-Month", "Agile Software Development", "Patterns of Enterprise Application Architecture"
    ],
    "Environmental Science": [
        "Silent Spring", "The Sixth Extinction", "The Uninhabitable Earth", "Our Planet",
        "The Water Will Come", "Field Notes from a Catastrophe", "The Ends of the World"
    ],
    "Applied Maths": [
        "Mathematics for Machine Learning", "A Mathematician's Apology", "Discrete Mathematics",
        "Calculus", "The Princeton Companion to Mathematics", "Linear Algebra Done Right",
        "How to Solve It"
    ],
    "Biotechnology": [
        "The Biotech Primer", "Genetech", "The Biotech Investor's Bible", "Biotechnology 101",
        "Molecular Biology of the Cell", "The Double Helix", "Biotech Basics"
    ]
}

names = ["John Smith", "Jane Doe", "Michael Brown", "Sarah Johnson", "Chris Lee", "Emily Davis",
         "David Wilson", "Laura Martinez", "James Taylor", "Linda Moore", "Robert Clark", "Mary Lewis",
         "Mark Walker", "Patricia Hall", "Steven Allen", "Barbara Young", "Charles King", "Jennifer Scott",
         "George Green", "Susan Adams", "Andrew White", "Angela King", "Joshua Young", "Jessica Allen",
         "Nicholas Hall", "Rebecca Scott", "Jacob Green", "Samantha Adams", "Benjamin Clark", "Stephanie Lewis",
         "Joseph Taylor", "Olivia Martinez", "Ethan Wilson", "Ava Johnson", "Daniel Brown", "Sophia Lee",
         "Matthew Davis", "Isabella Moore", "Alexander Walker", "Mia Clark", "Elijah Martinez", "Charlotte Hall",
         "Logan Green", "Amelia Adams", "Lucas Young", "Harper King", "Mason Allen", "Evelyn Scott"]

courses = ["Software Engineering", "Environmental Science", "Applied Maths", "Biotechnology"]

# Generate 50 records with 10 incorrect ones
records = []
correct_records = 40
incorrect_records = 10

# Generate correct records
for _ in range(correct_records):
    course = random.choice(courses)
    book = random.choice(books[course])
    name = random.choice(names)
    student_id = random.randint(1001, 1050)
    records.append([book, name, student_id, course])

# Generate incorrect records
for _ in range(incorrect_records):
    valid_course = random.choice(courses)
    invalid_course = random.choice([course for course in courses if course != valid_course])
    book = random.choice(books[invalid_course])
    name = random.choice(names)
    student_id = random.randint(1001, 1050)
    records.append([book, name, student_id, valid_course])

# Shuffle records to mix correct and incorrect ones
random.shuffle(records)

# Create a DataFrame
df_records = pd.DataFrame(records, columns=["Book", "Name", "StudentID", "Course"])

# Export DataFrame to an Excel file
excel_file_path = "student_book_records.csv"
df_records.to_csv(excel_file_path, index=False)


