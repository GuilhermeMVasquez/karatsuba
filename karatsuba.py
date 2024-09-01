import sys

sys.setrecursionlimit(10**9)

def main():
    print(karatsuba(sys.argv[1], sys.argv[2]))

def karatsuba(strArg1: str, strArg2: str) -> str:
    if len(strArg1) == 1 and len(strArg2) == 1:
        return '0' if strArg1 == '0' or strArg2 == '0' else '1'

    strArg1, strArg2 = sameEvenLen(strArg1, strArg2)

    a1 = strArg1[:len(strArg1)//2]
    a2 = strArg1[len(strArg1)//2:]
    b1 = strArg2[:len(strArg2)//2]
    b2 = strArg2[len(strArg2)//2:]

    left = karatsuba(a1, b1)
    right = karatsuba(a2, b2)
    middle = karatsuba(sum(a1, a2), sum(b1, b2))

    result = sum(sum(left + '0' * len(strArg1), sum(middle, sum(left, right), True) + '0' * (len(strArg1) // 2)), right).lstrip('0')
    return result if result else '0'

def sameEvenLen(strArg1: str, strArg2: str):
    strArg1, strArg2 = sameLen(strArg1, strArg2)
    if len(strArg1) % 2 != 0:
        strArg1 = '0' + strArg1
        strArg2 = '0' + strArg2
    return strArg1, strArg2

def sameLen(strArg1: str, strArg2: str):
    if len(strArg1) != len(strArg2):
        for i in range(abs(len(strArg1) - len(strArg2))):
            if len(strArg1) > len(strArg2):
                strArg2 = '0' + strArg2
            else:
                strArg1 = '0' + strArg1
    return strArg1, strArg2

def sum(strArg1: str, strArg2: str, isSub: bool = False) -> str:
    strArg1, strArg2 = sameLen(strArg1, strArg2)
    if isSub:
        strArg2 = complementOf1(strArg2)
    result = ''
    carry = '0'
    for i in range(len(strArg1)-1, -1, -1):
        if carry == '0':
            if strArg1[i] == '1' and strArg2[i] == '1':
                result = '0' + result
                carry = '1'
            elif strArg1[i] == '0' and strArg2[i] == '0':
                result = '0' + result
                carry = '0'
            else:
                result = '1' + result
                carry = '0'
        else:
            if strArg1[i] == '1' and strArg2[i] == '1':
                result = '1' + result
                carry = '1'
            elif strArg1[i] == '0' and strArg2[i] == '0':
                result = '1' + result
                carry = '0'
            else:
                result = '0' + result
                carry = '1'
    if isSub:
        return sum(result, '1') if carry == '1' else complementOf1(result)
    return result if carry == '0' else carry + result    

def complementOf1(strArg: str) -> str:
    result = ''
    for i in range(len(strArg)):
        result += '1' if strArg[i] == '0' else '0'
    return result


main()