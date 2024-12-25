import pandas as pd
from enum import Enum
import os
import platform


class Actions(Enum):
    EXIT = 1
    HIGHEST_PRICE = 2
    AVG_PRICE = 3
    IDEAL_COUNT = 4
    COLORS_NUM = 5
    HEZION = 6
    AVG_CUT_CARAT = 7
    COLOR_AVG_PRICE = 8

File_Name = "dimonds.csv"
dimonds_df = pd.DataFrame(columns=["carat", "cut", "color", "clarity", "depth", "table", "price", "x", "y", "z"]) 

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def savedimonds():
    try:
        dimonds_df.to_csv(File_Name, index=False)
    except Exception as e:
        print(f"Error saving dimonds to file: {e}")


def loaddimonds():
    global dimonds_df
    try:
        dimonds_df = pd.read_csv(File_Name)
    except FileNotFoundError:
        print(f"The file {File_Name} was not found. Starting with an empty list.")
    except pd.errors.EmptyDataError:
        print(f"The file {File_Name} is empty. Starting with an empty list.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}. Starting with an empty list.")


def menu():
    for act in Actions:
        print(f"{act.value} - {act.name}")
    return input("Your selection: ")
            
def highest():
    max = 0
    for index, row in dimonds_df.iterrows():
        if row['price'] > max:
            max = row['price']
    print(f"the highest price is {max}")

def avg_Price():
    priceSum = 0
    counter = 0
    for index, row in dimonds_df.iterrows():
        priceSum += row['price']
        counter +=1
    print(f"the average price is {priceSum/counter}")

def count_Ideal_Type():
    CountIdeal = dimonds_df['cut'].value_counts().get('Ideal', 0)
    print("Occurrences of 'Ideal':", CountIdeal)

def countColor():
    cnt = 0
    DColors = []

    for value in dimonds_df['color']:
        if value not in DColors:
            DColors.append(value)
            cnt += 1

    print(f"there are {cnt} colors and they are: {DColors}")

def find_Premium_Hezion():
    dimonds_df.sort_values(["33carat"], axis=0, ascending=[False], inplace=True) 
    valCount = 0
    median_value = 0
    for index, row in dimonds_df.iterrows():
        if row['cut'] == 'Premium':
            median_value=dimonds_df['33carat'].median()
    print('Median Value: '+str(median_value))
    
def cut_carat_avg():
    result = dimonds_df.groupby('cut')['33carat'].mean()
    print(result)

def color_avg_price():
    result = dimonds_df.groupby('color')['price'].mean()
    print(result)

if __name__ == "__main__":
    clear_terminal()
    loaddimonds()
    while True:
        try:
            user_selection =  Actions(int(menu()))
        except ValueError:
            clear_terminal()
            print("Fuck you!")
            continue
        clear_terminal()
        if user_selection is Actions.EXIT:exit()
        elif user_selection is Actions.HIGHEST_PRICE:highest()
        elif user_selection is Actions.AVG_PRICE:avg_Price()
        elif user_selection is Actions.IDEAL_COUNT:count_Ideal_Type()
        elif user_selection is Actions.COLORS_NUM:countColor()
        elif user_selection is Actions.HEZION:find_Premium_Hezion()
        elif user_selection is Actions.AVG_CUT_CARAT:cut_carat_avg()
        elif user_selection is Actions.COLOR_AVG_PRICE:color_avg_price()
        else:print("pick from the menu!")
        

