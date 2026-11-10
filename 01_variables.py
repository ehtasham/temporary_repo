# Slide: "Variables & data types"
# Run:  python snippets/01_variables.py

file_name ="my_file.txt" #string
my_no = 100 # integer
my_second_no = 100.2 # float
is_true = False # bool



name = input("what is your name \n")
print (f"your name is {name}")






# a variable is a named box for a value
doc_name = "Q3 report"   # str
pages = 12               # int
price = 3.00             # float
is_draft = True          # bool

print(doc_name, pages, price, is_draft)
print(type(pages))       # <class 'int'>

pages = pages + 3        # reassign
print("pages is now", pages)

# arithmetic

print(1)
print(10 / 4)    # 2.5  division
print(10 // 4)   # 2    whole division
print(10 % 4)    # 2    remainder

# Ask the room: what do 7 // 2 and 7 % 2 give?  (3 and 1)
