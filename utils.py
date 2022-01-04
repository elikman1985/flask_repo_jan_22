def calculations(records):
    v_sum = 0
    d = {}
    for i in range(len(records)):
        if records[i][0] in d:
            v_sum += records[i][1]
            d.update({records[i][0]: v_sum})
        else:
            v_sum = records[i][1]
            d.update({records[i][0]: v_sum})

    return '</br>'.join(str(key) + ' - ' + str(value) for key, value in d.items())
