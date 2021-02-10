import csv


def getData():
  ##############################################################################
  # get data
  num_rows = 0
  file1 = "amazon_co-ecommerce_sample.csv"
  file2 = "sample.csv"
  l = []
  category = []

  with open(file1, encoding="utf8") as f:
    reader = csv.reader(f)
    # get the column names
    category = next(reader)
    for row in reader: 
      l.append(row)
  f.close()
  ##############################################################################
  '''
  for col in range(len(category)):
    print("\n***",category[col],"***")
    for row in range(len(l)):
      print(l[row][col])
  '''
  ##############################################################################
  # construct the 2d array
  rows, cols = (len(l)+1, len(category)+1) 
  db = []
  for r in range(len(category)):
    col = []
    for c in range(len(l)):#col
      col.append(l[c][r])
    db.append(col)
  ##############################################################################
  # same as the csv column names
  header = ("uniq_id","product_name","manufacturer","price","number_available_in_stock","number_of_reviews","number_of_answered_questions","average_review_rating","amazon_category_and_sub_category","customers_who_bought_this_item_also_bought","description","product_information","product_description","items_customers_buy_after_viewing_this_item","customer_questions_and_answers","customer_reviews","sellers")
  ##############################################################################
  #return the db
  return db