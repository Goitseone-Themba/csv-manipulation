import pandas as pd

student_books_df = pd.read_csv('student_book_records.csv')

authorised = {
    "Software Engineering": [
        "Clean Code", "Refactoring", "Continuous Delivery", "Working Effectively with Legacy Code",
        "They Mythical Man-Month", "Agile Software Engineering", "Patterns of Enterprise Application Architecture"
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

unauthorised_records = []

for index, row in student_books_df.iterrows():
    course = row['Course']
    book = row['Book']
    if book not in authorised[course]:
        unauthorised_records.append(row)

    df_unauthorised = pd.DataFrame(unauthorised_records)

df_unauthorised.to_csv("Unauthorised_book_borrowing.csv", index=False)
