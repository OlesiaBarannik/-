"""
History:
    You have discovered your folder "Downloads" on your old personal computer.
    And found a lot of files. You are organized human, so you decided to sort your files by some rules.
"""

files = ["april_dashboard.xlsx", "may_dashboard.xlsx", "june_dashboard.xlsx",
         "july_dashboard.xlsx", "october_dashboard.xlsx", "Pro football theory 353-pages.pdf",
         "Clean Code 250-pages.pdf", "War&Peace 150-pages.pdf", "IKEA Instruction 35-pages.pdf",
         "october_dashboard.pptx", "july_dashboard.pptx", "(thriller) The Gray Man (2022).mp4",
         "(thriller) Level 16 (2018).mp4", "(thriller) Synchronic (2019).mp4",
         "(comedy) The Philadelphia Story (1940).mp4", "(comedy) Harold and Maude (1971).mp4",
         "(comedy) Booksmart (2019).mp4"]


for file in files:
# Print all your files
# -- * Your code here * --
    print(file)

# RESULT:
# april_dashboard.xlsx
# may_dashboard.xlsx
# june_dashboard.xlsx
# july_dashboard.xlsx
# october_dashboard.xlsx
# Pro football theory 353-pages.pdf
# Clean Code 250-pages.pdf
# War&Peace 150-pages.pdf
# IKEA Instruction 35-pages.pdf
# october_dashboard.pptx
# july_dashboard.pptx
# (thriller) The Gray Man (2022).mp4
# (thriller) Level 16 (2018).mp4
# (thriller) Synchronic (2019).mp4
# (comedy) The Philadelphia Story (1940).mp4
# (comedy) Harold and Maude (1971).mp4
# (comedy) Booksmart (2019).mp4
#
# How many files in folder?
# Use built-in function len

number_of_files  = len(files)
print(f"Number of files in folder \"Dowloads\" is {number_of_files}")

# RESULT
# Number of files in folder "Downloads" is 17.

# Let's explore unique file-extensions of files

file_extensions = []
for file in files:
    # Use a right method to separate file name and file-extension
    # You can write _ if you it's not important value. In this case I don't need to know file_name
    file_extension = file.split(".")[1]
    # Easy to understand such condition "not in". Which leads to only unique file-extensions
    if file_extension not in file_extensions:
        file_extensions.append(file_extension)
print(file_extensions)

# RESULT
# ['xlsx', 'pdf', 'pptx', 'mp4']

excel_files = []
powerpoint_files = []
book_files = []
video_files = []

for file in files:
    # Which method can check file extension at the end?
    if file.endswith("xlsx"): # -- * Your code here * --
        excel_files.append(file)
    elif file.endswith("pptx"): # -- * Your code here * --
        powerpoint_files.append(file)
    elif file.endswith("pdf"): # -- * Your code here * --
        book_files.append(file)
    elif file.endswith("mp4"): # -- * Your code here * --
        video_files.append(file)

print("Excel files:", excel_files, end = "\n\n")
print("PowerPoint files:", powerpoint_files, end = "\n\n")
print("Book files:", book_files, end = "\n\n")
print("Video files:", video_files, end = "\n\n")

# RESULT
# Excel files: ['april_dashboard.xlsx', 'may_dashboard.xlsx', 'june_dashboard.xlsx', 'july_dashboard.xlsx',
#               'october_dashboard.xlsx']

# PowerPoint files: ['october_dashboard.pptx', 'july_dashboard.pptx']

# Book files: ['Pro football theory 353-pages.pdf', 'Clean Code 250-pages.pdf', 'War&Peace 150-pages.pdf',
#              'IKEA Instruction 35-pages.pdf']

# Video files: ['(thriller) The Gray Man (2022).mp4', '(thriller) Level 16 (2018).mp4',
#               '(thriller) Synchronic (2019).mp4', '(comedy) The Philadelphia Story (1940).mp4',
#               '(comedy) Harold and Maude (1971).mp4', '(comedy) Booksmart (2019).mp4']


# The calendar year can be divided into four quarters, often abbreviated as Q1, Q2, Q3, and Q4.

Q1 = ["January", "February", "March"]
Q2 = ["April", "May", "June"]
Q3 = ["July", "August", "September"]
Q4 = ["October", "November", "December"]

# Your Boss has told you to send dashboard of Q2
excel_files_for_boss = []
for excel_file in excel_files:
    # Separate month and other stuff out of excel file name
    month, _ = excel_file.split("_") # -- * Your code here * --
    # Make condition to check if month belongs to Q2
    if month.title() in Q2: # -- * Your code here * --
        excel_files_for_boss.append(excel_file)
print(excel_files_for_boss)

# RESULT
# ['april_dashboard.xlsx', 'may_dashboard.xlsx', 'june_dashboard.xlsx']

# Your Boss has sent you a new task: send all dashboards that has the same powerpoint presentaitions
excel_files_for_boss = []
for excel_file in excel_files:
    excel_file_name, _ = excel_file.split(".")  # -- * Your code here * --

    for powerpoint_file in powerpoint_files:
        powerpoint_file_name, _ = powerpoint_file.split(".")  # -- * Your code here * --

        if  excel_file_name == powerpoint_file_name:# -- * Your code here * --
            excel_files_for_boss.append(excel_file)

print(excel_files_for_boss)

# RESULT
# ['july_dashboard.xlsx', 'october_dashboard.xlsx']

# I want to read books that has more than 120 pages but less than 300 pages

read_list = []
for book_file in book_files:

    # Retrieve number of pages out of book file name by using split method or any other you might want
    # Hint! To get last element of list use index [-1] like my_list[-1]
    # Hint! Do not forget to convert number_of_pages to number type

    book_file_name = book_file.split(" ") [-1]   # -- * Your code here * --
    book_file_number,_ = book_file_name.split ("-")
    if  120 < int(book_file_number) < 300:    # -- * Your code here * -- number_of_pages # -- * Your code here * --
        read_list.append(book_file)

print(read_list)

# RESULT
# ['Clean Code 250-pages.pdf', 'War&Peace 150-pages.pdf']

video_to_watch_for_fun = []
new_video_to_watch = []
maybe_later = []

for video_file in video_files:
    splited_text = video_file.split()
    genre, year = splited_text[0], splited_text[-1]

    # Retrieve genre and year out of paranthesis
    # Hint! Use genre/year[index_1:index_2]. Find the method to get indexes of two parenthesis
    genre = genre[genre.find("(")+1:genre.find(")")]  # -- * Your code here *
    year = year[year.find("(")+1:year.find(")")]  # -- * Your code here *
        # Convert year to numeric value
    year = int(year) # -- * Your code here * --

    # You need to sort filmes by conditions. First condition: genre is comedy and year less than 2000.
    # Second condtion is genre is comedy or thriller and film's year is greater or equal to 2019
    if  genre == "comedy" and year < 2000:
        video_to_watch_for_fun.append(video_file)
    elif (genre == "comedy" or genre == "thriller") and year >= 2019:
        new_video_to_watch.append(video_file)
    else:
        maybe_later.append(video_file)


    # Use the method to create a comma separated strinf if files.
    # ["video_1.mp4", "video_2.mp4"] -> "video_1.mp4, video_2.mp4"
video_to_watch_for_fun = ",".join(video_to_watch_for_fun) # -- * Your code here * --
new_video_to_watch = ",".join(new_video_to_watch) # -- * Your code here * --
maybe_later = ",".join(maybe_later)  # -- * Your code here * --

print("I want to watch it for fun:", video_to_watch_for_fun, end="\n\n")
print("I want to watch new video:", new_video_to_watch, end="\n\n")
print("Nah, I might watch it later:", maybe_later, end="\n\n")

# RESULT
# I want to watch it for fun: (comedy) The Philadelphia Story (1940).mp4, (comedy) Harold and Maude (1971).mp4
# I want to watch new video: (thriller) The Gray Man (2022).mp4, (thriller) Synchronic (2019).mp4, (comedy) Booksmart (2019).mp4
# Nah, I might watch it later: (thriller) Level 16 (2018).mp4




