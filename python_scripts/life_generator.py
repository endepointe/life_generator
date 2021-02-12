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
print(sorting.byUniqId(params, data))
# print(sorting.byNumOfReviews(inFile, data))

################################################################################
# write 
with open("output.csv", 'w', newline='') as outfile:
  output = csv.writer(outfile, delimiter=',')
  output.writerow(['input_item_type']+['input_item_category']+['input_number_to_generate']+['output_item_name']+['output_item_rating']+['output_item_num_reviews'])
  output.writerow(['data goes here'])