import sys
import csv
import sprint3_sort
import sprint3_getData

################################################################################
# represents the commandline arguments
inFile = str(sys.argv[1])

################################################################################
# get the data from the local csv file
(header, data) = sprint3_getData.getData()

################################################################################
# get the fields to search for from the inFile
(param_type,params) = sprint3_getData.readParams(inFile)

################################################################################
# just because it looks better
sorting = sprint3_sort

################################################################################
# pass the params representing the kind of data to retrieve.
# signature of params: 
#   input_item_type, input_item_category, input_number_to generate
# return format: [uniq_id, data_column]
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
s = sorting.byUniqId(params, data, header)
#for i in range(int(len(s) / 2)):
#  print(s[i])

'''
for i in range(3):
  print("***************************************")
  for j in range(8):
    #print(" [uniq_id, ", header[j+1], "]\n", s[i][j+1],"\n")
  print("\n")
  '''
n = sorting.byNumOfReviews(params, data, header)
#for i in range(len(n)):
#  print(n[i])



################################################################################
# write 
with open("output.csv", 'w', newline='') as outfile:
  output = csv.writer(outfile, delimiter=',')
  output.writerow(['input_item_type']+['input_item_category']+['input_number_to_generate']+['output_item_name']+['output_item_rating']+['output_item_num_reviews'])
  output.writerow(['data goes here'])