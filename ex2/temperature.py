def is_it_summer_yet(temp_for_comparison,temp_of_day1,temp_of_day2,temp_of_day3):
    check1 = bool(temp_for_comparison < temp_of_day1)
    check2 = bool(temp_for_comparison < temp_of_day2)
    check3 = bool(temp_for_comparison < temp_of_day3)
    lst = [check1, check2, check3]

    if lst.count(True) >= 2:
         return True

    else:
         return False

