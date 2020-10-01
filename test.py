from PrefixCodeTree import *

codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1],
# 'x5': [0,1]
}

codeTree = PrefixCodeTree()


for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

mes = codeTree.decode('110100101001111100100000100', 27)

print('mes', mes)