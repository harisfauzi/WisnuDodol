from Checker import Checker
from MyNumber import MyNumber

def checkNumber(aa, bb, cc):
    checker = Checker(aa, bb, cc)
    checker.showNumbers()
    if not checker.checkPremise01():
        print("Failed on Premise 01")
        return False
    if not checker.checkPremise02():
        print("Failed on Premise 02")
        return False
    if not checker.checkPremise03():
        print("Failed on Premise 03")
        return False
    if not checker.checkPremise04():
        print("Failed on Premise 04")
        return False
    if not checker.checkPremise05():
        print("Failed on Premise 05")
        return False
    return True

def main():
    mynumber = MyNumber()
    numbers = mynumber.getNumbers()
    for (aa, bb, cc) in numbers:
        # print("aa = %s bb = %s cc = %s" % (aa, bb, cc))
        found = checkNumber(aa, bb, cc)
        if found:
            print("The correct number is %s%s%s" % (aa, bb, cc))
            break

if __name__ == "__main__":
  # execute only if run as a script
  main()
