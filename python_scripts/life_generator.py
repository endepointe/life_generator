import sys
import csv
import sprint3_sort
import sprint3_getData

################################################################################
# represents the commandline arguments
inFile = str(sys.argv[1])
csvFile = str(sys.argv[2]) 
(header, d) = sprint3_getData.getData(inFile)
(column_names, data) = sprint3_getData.getData(csvFile)

################################################################################
# just because it looks better
sorting = sprint3_sort

################################################################################
# do the things
print(header)
print(column_names)
#print(sorting.byUniqId(data))
#print(sorting.byNumOfReviews(data))

################################################################################
# write 
with open("output.csv", 'w', newline='') as outfile:
  output = csv.writer(outfile, delimiter=',')
  output.writerow(['input_item_type']+['input_item_category']+['input_number_to_generate']+['output_item_name']+['output_item_rating']+['output_item_num_reviews'])
  output.writerow(['data goes here'])