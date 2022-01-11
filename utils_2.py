def calculations_2(records):
    d = {}
    i = 0

    for i in range(len(records)):
        cnt = 0
        if records[i][0] in d:
            cnt = d[records[i][0]] + 1
            d.update({records[i][0]: cnt})
        else:
            cnt = 1
            d.update({records[i][0]: cnt})

    return '</br>'.join(str(key) + ' - ' + str(round((value * records[i][1]), 2)) + '$'
                        for key, value in d.items() if value > 1)
