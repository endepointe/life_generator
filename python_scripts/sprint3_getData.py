import csv

def getData(fn = ""):
  ##############################################################################
  # get data
  print("reading ", fn)

  name = ""
  if len(fn) != 0:
    name = fn 
  else:
    name = "default.csv"

  #print(name)

  l = []
  category = []

  with open(name, encoding="utf8") as f:
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
  #return the header list and db
  return (category,db)