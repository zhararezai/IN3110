from curses.ascii import isdigit
from datetime import date
import re
from typing import Tuple
from requesting_urls import get_html

## -- Task 3 (IN3110 optional, IN4110 required) -- ##

# create array with all names of months
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

...


def get_date_patterns() -> Tuple[str, str, str]:
    """Return strings containing regex pattern for year, month, day
    arguments:
        None
    return:
        year, month, day (tuple): Containing regular expression patterns for each field
    """

    # Regex to capture days, months and years with numbers
    # year should accept a 4-digit number between at least 1000-2029
    year = r"(?P<year>[1-2][0-9]{3})"
    
    # month should accept month names or month numbers
    jan = r"\b[jJ]an(?:uary)?\b"
    feb = r"\b[fF]eb(?:ruary)?\b"
    mar = r"\b[mM]ar(?:ch)?\b"
    apr = r"\b[aA]pr(?:il)?\b"
    may = r"\b[mM]a(?:y)?\b"
    jun = r"\b[jJ]un(?:e)?\b"
    jul = r"\b[jJ]ul(?:y)?\b"
    aug = r"\b[aA]ugu(?:st)?\b"
    sep = r"\b[sS]ep(?:tember)?\b"
    oct = r"\b[oO]ct(?:ober)?\b"
    nov = r"\b[nN]ov(?:ember)?\b"
    dec = r"\b[dD]ec(?:ember)?\b"
    iso_month_format = r"\b(?:0\d|1[0-2])\b"

    month = rf"(?P<month>{jan}|{feb}|{mar}|{apr}|{may}|{jun}|{jul}|{aug}|{sep}|{oct}|{nov}|{dec}|{iso_month_format})"
    

    # day should be a number, which may or may not be zero-padded
    day = r"(?P<day>\b(?:0\d|1[0-9]{1}|2[0-9]{1}|3[0-1]{1}|\d{1})\b)"
    #print(day)

    return year, month, day


def convert_month(s: str) -> str:
    """Converts a string month to number (e.g. 'September' -> '09'.

    You don't need to use this function,
    but you may find it useful.

    arguments:
        month_name (str) : month name
    returns:
        month_number (str) : month number as zero-padded string
    """

    month_number = s

    # If s is not a digit 
    if s.isdigit() == False:
        month_number = 0
        # Convert to number as string
        for month in month_names:
            if s == month:
                month_number = month_names.index(month) + 1 #finding the correct month number
                if month_number < 10:
                    month_number = zero_pad(str(month_number))
    
    return str(month_number) 


def zero_pad(n: str):
    """zero-pad a number string

    turns '2' into '02'

    You don't need to use this function,
    but you may find it useful.

    Args:
        n (string): a digit in string format
    return: 
        the same digit (n), but with zero padding
    """
    zero_padded = "0" + n

    return zero_padded


def find_dates(text: str, output: str = None) -> list:
    """Finds all dates in a text using reg ex

    arguments:
        text (string): A string containing html text from a website
    return:
        results (list): A list with all the dates found
    """

    year, month, day = get_date_patterns()

    # Date on format YYYY/MM/DD - ISO, 2020-10-13
    ISO = rf"{year}-{month}-{day}"
    
    # Date on format DD/MM/YYYY, 13 October 2020
    DMY = rf"{day}\s{month}\s{year}"
   

    # Date on format MM/DD/YYYY, October 13, 2020
    MDY = rf"{month}\s{day},\s{year}"


    # Date on format YYYY/MM/DD, 2020 October 13
    YMD = rf"{year}\s{month}\s{day}"
 

   
    # list with all supported formats
    formats = [ISO, DMY, MDY, YMD]
    dates = [] #format year/month/day


    # find all dates in any format in text
    for format in formats:
        for tuppel in re.findall(rf"{format}", text):  # finding all format matches using re.findall:
            temp_list = list(tuppel) #making a temp list to be able to change value of day
    
            for element in temp_list:
                if len(element) < 2: #checking for zero padding                
                    temp_list[temp_list.index(element)] = zero_pad(element)
                
    
            if format == ISO: 
                # reformat ISO(Y-M-D) as Y/M/D
                date_element = f"{tuppel[0]}/{tuppel[1]}/{tuppel[2]}"
            elif format == DMY: 
                #converting the month name to number
                temp_list[1] = convert_month(temp_list[1])
                tuppel = tuple(temp_list)
                # reformat DMY as Y/M/D
                date_element = f"{tuppel[2]}/{tuppel[1]}/{tuppel[0]}"
            elif format == MDY:
                #converting the month name to number
                temp_list[0] = convert_month(temp_list[0])
                tuppel = tuple(temp_list)
                #reformat MDY as Y/M/D 
                date_element = f"{tuppel[2]}/{tuppel[0]}/{tuppel[1]}"
            elif format == YMD: 
                #converting the month name to number
                temp_list[1] = convert_month(temp_list[1])
                tuppel = tuple(temp_list)
                #reformat YMD as Y/M/D 
                date_element = f"{tuppel[0]}/{tuppel[1]}/{tuppel[2]}"
                

            dates.append(date_element)

    
    #print(ISO_list)
    #print(DMY_list)
    #print(f"MDY LISTE: {MDY_list}")
    #print(YMD_list)


    # Write to file if wanted
    if output:
        get_html("https://en.wikipedia.org", output=output)


    return dates
