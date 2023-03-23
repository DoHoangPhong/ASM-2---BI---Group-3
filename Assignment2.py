import os
import pandas as pd

from pathlib import Path


def delete_rows():
    # Read CSV file
    df = pd.read_csv("Sample.csv")

    # Get input from user
    delete_rows = input("Enter the rows you want to delete: ")

    # Split input into a list of row numbers to delete
    delete_rows = delete_rows.split(",")

    # Convert row numbers to integers
    delete_rows = [int(i) for i in delete_rows]

    # Delete rows from DataFrame
    df = df.drop(delete_rows)

    # Write modified DataFrame to CSV file
    output_file = 'Sample_delete_row.csv'
    df.to_csv(output_file, index=False)

    # Print message indicating successful save
    print(f'The modified DataFrame was saved to {output_file}.')
def clean_data():
    data = pd.read_csv("Sample.csv")
    cleaned_data = data.dropna()
    cleaned_data.to_csv("cleaned_data.csv", index=False)
def blank_data():
    data = pd.read_csv("Sample.csv")

    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)

    # Set display options to show all columns
    # pd.set_option('display.max_colwidth', None)

    # missing_data = data[data.isna().any(axis=1)]

    # # Display the missing data
    # print(missing_data.head(10))
    # # Display the next 5 rows of the DataFrame
    # print(missing_data.iloc[10:15])
def display_data():
    data = pd.read_csv("Sample.csv")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
        # Set display options to show all columns
    pd.set_option('display.max_colwidth', None)
    print(data.head(10))
#Menu
def main():

    while True:
        print()
        print("***Menu***")
        print("Please choose your options:")
        print("1. Input data")
        print("2. Display data")
        print("3. Show the blanks")
        print("4. Delete rows")
        print("5. Clean Data")
        print("6. Save")
        print("7. Quit")
        print("Enter your option: ", end='')
        choose = str(input())
        if choose == '1':
            file_name = Path(input("Please enter the file name: "))
            if not (file_name.is_file()):
                print("File has name [" + str(file_name) + "] is not found")
            else:
                file_data = pd.read_csv(file_name)
            header = list(file_data.columns)
            print("Import successfully!")
        elif choose == '2':
            display_data()
        elif choose == '3':
           blank_data()
        elif choose == '4':
            delete_rows()
        elif choose == '5':
            clean_data()
            print('Clean successful')
        elif choose == '6':
            try:

                # load the original data from a CSV file
                df = pd.read_csv('Sample.csv')

                # modify the DataFrame
                df.dropna(inplace=True)  # remove rows with null values

                # save the modified DataFrame to a new CSV file
                df.to_csv('new_file.csv', index=False)  # set index=False to avoid writing the index column
                print("Save successfully")
            except:
                print("sorry you have not entered the data yet")

        elif choose == '7':
            print("You have exited the program")
            exit()
        else:
            print("Enter the wrong key")

        option = int(input("Enter an option: "))
main()
