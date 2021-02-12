import sys
import sprint3_getData
'''
reference help:
https://www.geeksforgeeks.org/python-finding-strings-with-given-substring-in-list/
'''

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

# param[0] searches through data[8] for a subcategory (static set to toys)
# param[1] searches through data[8] for main category
# param[2] specifies how many items to return
def byUniqId(param = [], data = [], header = []):
  '''
  input_item_type = [i for i in data[8] if str(param[0]) in i]
  input_item_category = [i for i in data[8] if str(param[1]) in i]
  print(input_item_category)
  print(input_item_type)
  '''
  items = []
  sorted_by_uniq_id = []

  for i in range(len(data[0])):
    if (data[8][i].find(param[0]) >= 0) or (data[8][i].find(param[1]) >= 0):
      row = []
      '''
      print("********************************")
      '''
      for j in range(len(data)):
        # create an index to use as a [key, value] pair for use
        # with the sort() method. unique_ids will be sorted by key
        row.append([data[0][i],data[j][i]])
        '''
        print(header[j],": ", row)
      print("\n")
        '''
      items.append(row)
  #[row][col]#
  #sort the list by key
  items.sort()
  sorted_by_uniq_id = items
  '''
  for i in range(len(sorted_by_uniq_id)):
    print(sorted_by_uniq_id[i][0],sorted_by_uniq_id[i][2])
  '''
  return  (sorted_by_uniq_id)

def byNumOfReviews(data = []):
  d = data[5] 
  return d