def main():
    input_num = input('Enter number:')
    input_exp = input('Enter exponent:')

    try:
        number = float(input_num)
    except error:
        print('Invalid number input.')
        return
    try:
        exponent = int(input_exp)
    except error:
        print('Invalid exponent input.')
        return
    
    result = 1
    for _ in range(exponent):
        result = result * number
    
    if result == int(result):
        print('Result:',int(result))
    else:
        print('Result:',result)

if __name__ == '__main__':
    main()