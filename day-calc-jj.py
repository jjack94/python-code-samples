# James Jack
# 1/28/21
# this program takes the starting weekday/number of days gone and gives the weekday of the return
start = input("what day of the week did you leave? please input between 0-6 (0=sunday/6=saturday")
start = int(start)

days_gone = input(" how many days were you gone for?")
days_gone = int(days_gone)

end_day = (start + days_gone) % 7

print("the day of the week of your return is", end_day)
