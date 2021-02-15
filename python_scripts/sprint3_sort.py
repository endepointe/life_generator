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
  uniq_ids = []
  sorted_by_uniq_id = []
  
  for i in range(len(data[0])):
    if (data[8][i].find(param[0]) >= 0) or (data[8][i].find(param[1]) >= 0):
      row = []
      #print("********************************")
      # the first index will be the identifier, then append
      # the columns of data. index 0 is the uniq id
      #print(data[0][i])
      row.append(data[0][i])
      for j in range(len(data)):
        row.append(data[j][i])
        #print(header[j],": ", row)
      #print("\n")
      uniq_ids.append(row)

  #[row][col]#
  #sort the list by uniq_id
  uniq_ids.sort()
  sorted_by_uniq_id = uniq_ids

def byNumOfReviews(param = [], data = [], header = []):

  num_reviews = []
  sorted_by_num_reviews = []

  size = len(data[0])
  for i in range(size):
    # 8 is the category type and or subcategory
    if (data[8][i].find(param[0]) >= 0) or (data[8][i].find(param[1]) >= 0):
      row = []
      #print("********************************")
      # the first index will be the identifier, then append
      # the columns of data. index 5 is the number of reviews
      #row.append(data[5][i])
      val = data[5][i]
      #print(len(val), type(val))
      #idkwtfiamdoingbutimdoingitthisway
      s = []
      for x in val:
        s += x
      row += str(s)
      for j in range(7):#len(data)):
        row.append(data[j][i])
        #print(header[j],": ", row)
      #print("\n")
      num_reviews.append(row)
  
  num_reviews.sort()
  
  for i in range(len(num_reviews)):
    print(num_reviews[i])

  sorted_by_num_reviews = num_reviews

  return  sorted_by_num_reviews
