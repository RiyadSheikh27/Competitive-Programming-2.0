def distinct_digits(year):
    while True:
        year += 1
        year_str = str(year)
        if len(set(year_str)) == len(year_str):
            return year


y = int(input())
result = distinct_digits(y)
print(result)
