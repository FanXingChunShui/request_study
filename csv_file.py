import csv;

file_name ="123.csv";
with open(file_name,encoding="utf-8") as f:
   reader = csv.reader(f)

   headers =next(reader)
   for row in reader:

       print(reader.line_num,row[0],row[1])