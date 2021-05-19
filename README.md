# EasyChair to ACM copyright form data

1. Install python3
2. Download author data from EasyChair by going to *Premium* -> *Data views* -> Download the list of authors -> Uncheck no decision and REJECT
3. Convert the Excel file to CSV (File -> Save As) as authors.csv
4. Fix the CSV first line so that all the headers are on a single line
5. Call convert_to_acm.py authors.csv output.csv
6. Save the data to a CSV file and then edit it in Excel, adding in missing information