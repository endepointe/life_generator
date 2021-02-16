from tkinter import *
from tkinter import ttk
import sys
import csv
import sprint3_sort
import sprint3_getData

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

################################################################################
# get the data from the local csv file
(header, data) = sprint3_getData.getData()

################################################################################
# just because it looks better
sorting = sprint3_sort

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
  try:
    cnt = int(result_count.get()) 
    cat = category.get()
    subcat = subcategory.get()
    print(cat, cnt)
    params = [subcat, cat, cnt]
    ##################################################
    # get the fields to search for from the user input 
    uniqIds = sorting.byUniqId(params, data, header)
    numReviews = sorting.byNumOfReviews(params, data, header)
    avgRatings = sorting.byAvgRevRating(params, data, header)
    data_area = ttk.Frame(root).grid()
    # specify the columns, as many or as little as needed
    cols_to_print = [1,2,4,6,8,9]
    for row in range(len(avgRatings)):
      for col in range(len(cols_to_print)):
        val = cols_to_print[col]
        ttk.Label(data_area, text=avgRatings[row][val]).grid(column=col, row=row+5)

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

category = StringVar(window)
category.set(MAINCAT[0])

subcategory = StringVar(window)
subcategory.set(SUBCAT[0])

result_count = StringVar(window)
count_entry = ttk.Entry(window, textvariable=result_count)
count_entry.grid(column=1,row=0)

mainc = OptionMenu(window, category, *MAINCAT)
mainc.grid(column=2, row=0)

subc = OptionMenu(window, subcategory, *SUBCAT)
subc.grid(column=3, row=0)

button = Button(window, text="Get Results", command=getResults)
button.grid(column=1,row=1)

root.mainloop()