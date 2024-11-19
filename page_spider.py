import os
import argparse

def main(database: str, url_list_file: str):
    print("we going to work with " + database)
    print("we going to scan " + url_list_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db",'--database', help='SQlite database name')
    parser.add_argument('-i',"--input", help='Files containing urls to read')
    arge = parser.parse_args()
    database_file = arge.database
    input_file = arge.input
    main(database=database_file, url_list_file=input_file)