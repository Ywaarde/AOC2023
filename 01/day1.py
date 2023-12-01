f = open("input.txt", "r").read()

calibrate_01 = f.splitlines()

e = open("example2.txt", "r").read()

calibrate_00 = e.splitlines()

numbers = ['1','2','3','4','5','6','7','8','9']

letters = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

options = letters + numbers

def calculate_one(input):
    result = 0

    for line in input:
        nums = [t for t in line if t in '0123456789']
        first = nums[0]
        last = nums[-1]
        factor = int(first+last)
        result +=factor

    return result

def calculate(input):
    result = 0

    for line in input:
        nums = [line.find(t) for t in options]

        first_index = nums.index(min([n for n in nums if n >= 0]))
        last_index = nums.index(max(nums)) #Why is this wrong?

        rev = [line[::-1].find(t[::-1]) for t in options]

        last_rev_index = rev.index(min([n for n in rev if n >= 0]))

        first = options[first_index] if options[first_index] in numbers else str(letters.index(options[first_index])+ 1)
        last = options[last_rev_index] if options[last_rev_index] in numbers else str(letters.index(options[last_rev_index])+ 1)
        
        factor = int(first+last)
        result +=factor

    return result

# print(calculate(calibrate_00))
print(calculate_one(calibrate_01))
print(calculate(calibrate_01))