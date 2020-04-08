import array

class Checker:
    def __init__(self, aa, bb, cc):
        self.numbers = []
        self.numbers.append(aa)
        self.numbers.append(bb)
        self.numbers.append(cc)
    
    def showNumbers(self):
        print("The numbers are '%s', '%s', and '%s'" % (self.numbers[0], self.numbers[1], self.numbers[2]))

    # 147 - One digit is rigt but in the wrong place
    def checkPremise01(self):
        if self.numbers[0] == '1':
            return False
        if self.numbers[1] == '4':
            return False
        if self.numbers[2] == '7':
            return False
        if '1' in self.numbers or '4' in self.numbers or '7' in self.numbers:
            return True
        return False

    # 189 - One digit is right and in its place
    def checkPremise02(self):
        if self.numbers[0] == '1' and not '8' in self.numbers and not '9' in self.numbers:
            return True
        elif self.numbers[1] == '8' and not '1' in self.numbers and not '9' in self.numbers:
            return True
        elif self.numbers[2] == '9' and not '1' in self.numbers and not '8' in self.numbers:
            return True
        return False

    # 964 - Two digits are correct but both are in the wrong place
    def checkPremise03(self):
        # Make sure it's not combination of 964
        if '9' in self.numbers and '6' in self.numbers and '4' in self.numbers:
            return False
        # Check 96
        if '9' in self.numbers and '6' in self.numbers:
            if self.numbers[0] != '9' and self.numbers[1] != '6':
                return True
        # Check 94
        elif '9' in self.numbers and '4' in self.numbers:
            if self.numbers[0] != '9' and self.numbers[2] != '4':
                return True
        # Check 64
        elif '6' in self.numbers and '4' in self.numbers:
            if self.numbers[1] != '6' and self.numbers[2] != '4':
                return True
        return False

    # 523 - All digits are wrong
    def checkPremise04(self):
        if '5' in self.numbers:
            return False
        if '2' in self.numbers:
            return False
        if '3' in self.numbers:
            return False
        return True

    # 286 - One digit is right but on the wrong place
    def checkPremise05(self):
        if self.numbers[0] == '2':
            return False
        if self.numbers[1] == '8':
            return False
        if self.numbers[2] == '6':
            return False
        if '2' in self.numbers or '8' in self.numbers or '6' in self.numbers:
            return True
        return False

