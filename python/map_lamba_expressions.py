cube = lambda x: x ** 3

def fibonacci(n):
    # return a list of fibonacci numbers
    result = [0, 1]
    for i in range(n - 2):
        result.append(result[-2] + result[-1])

    return result[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

'''
Input Format:
One line of input: an integer N.

Output Format:
A list on a single line containing the cubes of the first N fibonacci numbers.

Sample Input:
5

Sample Output:
[0, 1, 1, 8, 27]

'''