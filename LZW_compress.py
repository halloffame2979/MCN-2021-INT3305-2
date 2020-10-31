
def encode(s):
    d1 = dict()

    encode = list()
    count = 256
    for i in range(255):
        d1[chr(i+1)] = i+1
    w = ''

    for i in range(len(s)):

        if i == len(s)-1:
            try:
                encode.append(d1[w+s[i]])
            except:
                encode.append(d1[w])
                encode.append(d1[s[i]])
            break

        if w + s[i] in d1.keys():
            w += s[i]
        else:

            d1[w+s[i]] = count
            encode.append(d1[w])
            count += 1
            w = s[i]
    for k, v in d1.items():
        if v >= 256:

            print(format(v, ' 4d'), k)
    return encode


def decode(l):
    d = dict()
    for i in range(255):
        d[i+1] = chr(i+1)
    w = ''
    decode = w
    count = 256
    for i in range(len(l)):
        if i == 0:
            w = d[l[i]]
        else:
            if i == len(l)-1:
                d[count] = w + d[l[i]]
                decode += d[l[i]]
                break

            else:

                d[count] = w + d[l[i]][:1]
                w = d[l[i]]
                print(count, d[count])
                count += 1
        decode += d[l[i]]
    return decode


s =50*'yyeu hay khong yeu khong yeu hay yeu noi mot loi khong yeu yeu hay khong yeu khong yeu hay yeu noi mot loi thoi'
# s = s.replace(' ','')

res = encode(s)
print()
print('before', len(s))
print()
print(res)
print()
print('after', len(res))
print()
print(decode(res))
print()
sum = 0
for i in res:
    if i < 256:
        sum += 8
    else:
        sum += 9


print((sum + 8*256) / (len(s)*8)*100)
