import sys
import sprint3_getData

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

def byUniqId(param = [], data = []):
  d = data[0]

  if any(param[0] in entry for entry in data[0])
  d.sort()
  return d 

def byNumOfReviews(data = []):
  d = data[5] 
  return d