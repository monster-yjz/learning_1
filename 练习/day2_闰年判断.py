year = float(input('请输入年份'))
laap_year = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(laap_year)
