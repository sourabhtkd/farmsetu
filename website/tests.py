import functools

headers = ['9.0', '1916', '10.0', '2019', '12.1', '2012', '15.7', '2011', '17.2', '2018', '20.5', '1940', '23.3',
           '2006', '22.8', '1995', '19.4', '1895', '15.6', '1921', '11.6', '2011', '10.7', '2015', '8.59', '1989',
           '13.98', '1893', '21.01', '1976', '14.84', '2006', '13.54', '2014']

row = ['jan', 'year', 'feb', 'year', 'mar', 'year', 'apr', 'year', 'may', 'year', 'jun', 'year', 'jul', 'year', 'aug',
       'year', 'sep', 'year', 'oct', 'year', 'nov', 'year', 'dec', 'year', 'win', 'year', 'spr', 'year', 'sum', 'year',
       'aut', 'year', 'ann', 'year']

if __name__ == "__main__":
    res = list()
    for start in range(0, len(headers), 2):
        limit = start + 2
        related_header = headers[start:limit]
        related_row = row[start:limit]

        print(related_header)
        print(related_row)
        res.append(
            {related_header[0]: related_row[0],
             related_header[1]: related_row[1]
             }
        )

    print(res)
