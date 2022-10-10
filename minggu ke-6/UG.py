class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']

    # method untuk menambahkan data baru 
    def push(self,data):
        self.stackList.append(data)

    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    def cekValidExpression(self, expression):
        for i in expression:
            if i.isalpha() or i == "(" or i == ")":
                return False
        return True

    def infixToPrefix(self, expression):

        if " " in expression:
            expression = expression.split()
        if not self.cekValidExpression(expression):
            return "Expresi Infix yang anda masukkan tidak valid !!"
        #belumm selesaii



# Test Case
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))