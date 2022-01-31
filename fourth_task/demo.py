from csv_reader import email_name_stacker
import csv
if __name__ == "__main__":
    with open('./data/em.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        print(email_name_stacker(data))
