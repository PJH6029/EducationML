def full_adder(x1, x2, cin):
    s = x1 ^ x2 ^ cin
    cout = (cin & (x1 ^ x2)) | (x1 & x2)
    # cout = OR(AND(x1, x2), AND(cin, XOR(x1, x2)))
    return s, cout

def adder_4bit(x1_arr, x2_arr, cin = 0):
    cout = 0
    res = list()
    for i in range(len(x1_arr) - 1, -1, -1):
        s, cout = full_adder(x1_arr[i], x2_arr[i], cin)
        res.append(s)
        cin = cout
    res.reverse()
    return res, cout


def adder_fourbit(x1_arr, x2_arr, cin = 0):
    result1 = full_adder(x1_arr[3], x2_arr[3], cin)
    result2 = full_adder(x1_arr[2], x2_arr[2], result1[1])
    result3 = full_adder(x1_arr[1], x2_arr[1], result2[1])
    result4 = full_adder(x1_arr[0], x2_arr[0], result3[1])
    tmp = [result4[0], result3[0], result2[0], result1[0]]
    if result4[1]:
        tmp.insert(0, result4[1])
    return tmp

def adder_8bit(x1_arr, x2_arr):
    res1, cout1 = adder_4bit(x1_arr[4:], x2_arr[4:])
    print(res1)
    res2, cout2 = adder_4bit(x1_arr[:4], x2_arr[:4], cout1)
    print(res2)
    return res2 + res1, cout2


print(adder_4bit([1, 1, 0, 0],
                 [1, 0, 0, 0]))

print(adder_8bit([1, 1, 0, 0, 1, 1, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0]))
