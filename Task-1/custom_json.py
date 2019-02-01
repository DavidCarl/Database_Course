def dumps(data):
    string = '{'
    length = len(data)
    for i, key in enumerate(data):
        string += '{"' + key + '":"' + data[key] + '"}'
        if (i + 1) != length:
            string += ','
    string += '}'
    return string

def loads(data):
    amount = len(data.split(':'))
    data = data.split('"')
    data_disk = {}
    for x in range(0, (int(amount) - 1)):
        data_disk[data[(1 + (x * 4))]] = data[(3 + (x * 4))]
    return data_disk