import calendar

# Define a dictionary of holidays in Cambodia
cambodia_holidays = {
    1: {1: "New Year's Day"},
    4: {13: "Khmer New Year (Day 1)", 14: "Khmer New Year (Day 2)", 15: "Khmer New Year (Day 3)"},
    5: {1: "International Labor Day", 14: "Visak Bochea"},
    9: {24: "Constitution Day"},
    10: {15: "Pchum Ben (Day 1)", 16: "Pchum Ben (Day 2)", 17: "Pchum Ben (Day 3)",
          18: "Pchum Ben (Day 4)", 19: "Pchum Ben (Day 5)"},
    11: {9: "Independence Day", 30: "Water Festival (Day 1)", 31: "Water Festival (Day 2)"},
    12: {25: "Christmas"},
}

# Define a dictionary of holidays in Brazil
brazil_holidays = {
    1: {1: "New Year's Day"},
    2: {12: "Carnival"},
    4: {21: "Tiradentes Day"},
    5: {1: "Labor Day", 12: "Mother's Day"},
    9: {7: "Independence Day"},
    10: {12: "Our Lady of Aparecida"},
    11: {2: "All Souls' Day", 15: "Republic Day"},
    12: {25: "Christmas"},
}

# Define a dictionary of significant Catholic holidays
catholic_holidays = {
    1: {6: "Feast of the Epiphany"},
    2: {22: "Ash Wednesday (Varies)"},
    3: {19: "St. Joseph"},
    4: {23: "St. George"},
    6: {13: "St. Anthony of Padua"},
    7: {11: "St. Benedict"},
    10: {1: "St. Therese of Lisieux", 4: "St. Francis of Assisi", 15: "St. Teresa of Avila"},
    11: {1: "All Saints' Day", 2: "All Souls' Day", 9: "Independence Day"},
    12: {8: "Feast of the Immaculate Conception", 25: "Christmas"},
}

def print_calendar_with_holidays(year):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()

    # Display the full year's calendar
    for month in range(1, 13):
        print(cal.formatmonth(year, month))

        # Print holidays for Cambodia
        if month in cambodia_holidays:
            for day, holiday in cambodia_holidays[month].items():
                print(f"  {month}/{day}: Cambodia - {holiday}")

        # Print holidays for Brazil
        if month in brazil_holidays:
            for day, holiday in brazil_holidays[month].items():
                print(f"  {month}/{day}: Brazil - {holiday}")

        # Print significant Catholic holidays
        if month in catholic_holidays:
            for day, holiday in catholic_holidays[month].items():
                print(f"  {month}/{day}: Catholic - {holiday}")

        print()

# Get input from the user for the year
year = int(input("Enter year (e.g., 2024): "))
print_calendar_with_holidays(year)
