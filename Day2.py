def sum(num1, num2):
    result = num1+num2
    def square(take_result):
        return take_result*take_result
    return (square(result))
print(sum(10,20))


