class PrefixCodeTree:
    def __init__(self, data = None):
        self.data = data
        self.n0 = None
        self.n1 = None

    def insert(self, codeword, symbol):
        l = len(codeword)
        w = codeword[0]
        if l == 0:
            print('GG')
            return
        if l == 1:
            if w == 0:
                self.n0 = PrefixCodeTree(symbol)
                return
            if w == 1:
                self.n1 = PrefixCodeTree(symbol)
                return

        if l > 1 :
            if w == 0:
                if self.n0 is not None and self.n0.data is None:
                    self.n0.insert(codeword[1:], symbol)
                if self.n0 is None:
                    self.n0 = PrefixCodeTree()
                    self.n0.insert(codeword[1:], symbol)
                
            if w == 1:
                if self.n1 is not None and self.n1.data is None:
                    self.n1.insert(codeword[1:], symbol)
                if self.n1 is None:
                    self.n1 = PrefixCodeTree()
                    self.n1.insert(codeword[1:], symbol)

    def decode(self, encoded, datalen):
        data = str(encoded)
        res = ''
        count = 0

        while count < datalen:
            iter = self
            # print('start =',count)
            c = count
            for i in range(datalen-count):
                now = i + c
                # print('now = ',now, 'value = ',data[now])
                                                
                if data[now] == '0':
                    if iter.n0 is None:
                        return "error"
                    iter = iter.n0
                    # print('at 0 is ',count)
                    count += 1
                    
                if data[now] == '1':
                    if iter.n1 is None:
                        return "error"
                    iter = iter.n1
                    # print('at 1 is ',count)
                    count += 1

                if iter.data is not None:
                    res += iter.data 
                    # print('true ',count, 'value = ', iter.data)
                    break    
        return res
    



# def tran(tree):
#     print(tree.data)
#     if tree is not None:      
#         if tree.n0 is not None:
#             tran(tree.n0)
#         if tree.n1 is not None:

#             tran(tree.n1)
    

# tran(codetree)   