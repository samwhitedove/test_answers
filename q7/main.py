def formatNumber (number):
    if number %2 == 1:
        frm = '--'+str(number)+ '-'
    else:
        frm = '-'+str(number)+'-'
    return frm


if __name__ == '__main__':
    c = 5
    p = 5
    output = ""
    while c < 20:
        temp = c + p
        p = c
        c = temp
        output = output + formatNumber(c)
    print(output)

