import csv
data = [
    ["Year (January)", "Population (thousands)", "Rural (%)", "Urban (%)", "Source"],
    [1897, '4,000', 'n/a', 'n/a', 'census'],
    [1926, '6,198', 'n/a', 'n/a', 'census'],
    [1939, '6,081', 72, 28, 'census'],
    [1959, '9,295', 56, 44, 'census'],
    [1970, '13,001', 50, 50, 'census'],
    [1979, '14,685', 46, 54, 'census'],
    [1989, '16,537', 43, 57, 'census'],
    [1999, '14,953', 43, 57, 'census'],
    [2009, '15,982', 46, 54, 'census'],
    [2023, '20,137', 39, 61, 'estimate']
]
with open('population_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
with open('population_data.csv', 'r') as file:
    print(file.read())
