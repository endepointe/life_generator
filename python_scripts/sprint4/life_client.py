import socket
from tkinter import *
from tkinter import ttk
import sys
import csv
import sprint4_sort
import sprint4_getData

MAINCAT = [
  "Hobbies",
  "Jigsaws Puzzles",
  "Toys",
  "Games",
  "Arts & Crafts",
  "Fancy Dress",
  "Party Supplies",
  "Die-Cast & Toy Vehicles"
] 

SUBCAT = [
  "Toys",
  "Trains",
  "Locomotives",
  "Costumes",
  "Bags",
  "Children's Craft Kits",
  "Dice & Dice Games",
  "Art Sand",
  "Bead Art & Jewellery-Making",
  "Sets & Kits",
  "Vehicles"
]

STATE = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

################################################################################
# get the data from the local csv file
data = sprint4_getData.getData()

################################################################################
# just because it looks better
sorting = sprint4_sort

#####
# data area
'''
0 uniq_id
1 product_name
2 manufacturer
3 price
4 number_available_in_stock
5 number_of_reviews
6 number_of_answered_questions
7 average_review_rating
8 amazon_category_and_sub_category
9 customers_who_bought_this_item_also_bought
10 description
11 product_information
12 product_description
13 items_customers_buy_after_viewing_this_item
14 customer_questions_and_answers
15 customer_reviews
16 sellers
'''

def getResults():

  host = 'localhost'
  port = 6000
  print(host, port)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, int(port)))
  
  try:
    cnt = int(result_count.get()) 
    cat = category.get()
    subcat = subcategory.get()
    yr = year.get()
    st = state.get()
    s.send(bytes(year.get() + ',' + state.get(), encoding='utf-8'))
    server_data = s.recv(4096)
    s = str(server_data.decode('utf-8')).split(',')
    #################################################
    # get the population data returned in a str format
    p = s[2:]
    population = ""
    for i in range(len(p)):
      population += str(p[i])
      if i < len(p) - 1:
        population += ","
    params = [subcat, cat, cnt]
    ##################################################
    # get the fields to search for from the user input 
    uniqIds = sorting.byUniqId(params, data)
    numReviews = sorting.byNumOfReviews(params, data)
    avgRatings = sorting.byAvgRevRating(params, data)
    data_area = ttk.Frame(root).grid()
    # specify the columns, as many or as little as needed
    cols_to_print = [1,2,4,6,8,9]
    for row in range(len(avgRatings)):
      for col in range(len(cols_to_print)):
        val = cols_to_print[col]
        ttk.Label(data_area, text=avgRatings[row][val]).grid(column=col, row=row+6)
    population_data = ttk.Frame(root).grid()
    ttk.Label(population_data, text="Population of " + state.get() + ": " + population + " in " + year.get()).grid(column=1, row=4)
    ttk.Label(population_data, text=" ").grid(column=1, row=5)


    #######
    # write 
    with open("gui_output.csv", 'w', newline='') as outfile:
      output = csv.writer(outfile, delimiter=',')
      output.writerow(['input_item_type']+['input_item_category']+['input_number_to_generate']+['output_item_name']+['output_item_rating']+['output_item_num_reviews\n'])
      for row in range(len(avgRatings)):
        for col in range(6):
          s = str(avgRatings[row][2]).encode("utf-8")
          output.writerow([params[0]]+[params[1]]+[params[2]]+[s]+[avgRatings[row][6]])

  except ValueError:
    pass

root = Tk()
root.title("Life Generator")

#window = ttk.Frame(root, width=500, height=500).grid(column=0, row=0)
window = ttk.Frame(root, padding="5 5 5 5").grid()

ttk.Label(window, text="Number of Results").grid(column=0, row=0)

# main category
category = StringVar(window)
category.set(MAINCAT[0])

subcategory = StringVar(window)
subcategory.set(SUBCAT[0])

# number of items to return
result_count = StringVar(window)
count_entry = ttk.Entry(window, textvariable=result_count)
count_entry.grid(column=1,row=0)

mainc = OptionMenu(window, category, *MAINCAT)
mainc.grid(column=2, row=0)

subc = OptionMenu(window, subcategory, *SUBCAT)
subc.grid(column=3, row=0)

ttk.Label(window, text="Year").grid(column=0, row=1)
year = StringVar(window)
year_entry = ttk.Entry(window, textvariable=year)
year_entry.grid(column=1,row=1)

state = StringVar(window)
state.set(STATE[0])
st = OptionMenu(window, state, *STATE)
st.grid(column=2, row=1)

button = Button(window, text="Get Results", command=getResults)
button.grid(column=1,row=2)

root.mainloop()