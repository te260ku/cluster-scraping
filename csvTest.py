import csv
with open('data/sample.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([0, 1, 2])
    writer.writerow(['a', 'b', 'c'])