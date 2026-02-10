#Sometimes during live coding, I can’t look at the documentation. Because of that, I want to memorize the syntax.
#Sometimes during live coding, I can’t look at the documentation. Because of that, I want to memorize the syntax.
#Sometimes during live coding, I can’t look at the documentation. Because of that, I want to memorize the syntax.
#Sometimes during live coding, I can’t look at the documentation. Because of that, I want to memorize the syntax.
#Sometimes during live coding, I can’t look at the documentation. Because of that, I want to memorize the syntax.
#Sometimes during live coding, I can’t look at the documentation. Because of that, I want to memorize the syntax.
#Sometimes during live coding, I can’t look at the documentation. Because of that, I want to memorize the syntax.

nums = []
for i in range(len(nums)):
for i in range(i + 1, len(nums)):
for i in nums:

count = [10, 20, 30]

for i, value in enumerate(count):
    print(i, value)

count = {
    1: 3,
    2: 5,
    7: 1
}
for num, cnt in count.items():
    print(num, cnt)
1 3
2 5
7 1

count = {
    1: 3,
    2: 5,
    7: 1
}

for num, cnt in enumerate(count):
    print(num, cnt)
0 1
1 2
2 7


count = {10, 20, 30}

count.get(10, 0)
0

count.get(10, 1)
10

count.get(10, 1)
10

count.get(10, 1)
10

freq = [10, 20, 30, 40]
for i in range(len(freq) - 1, 0, -1): # range(start, stop, step)
    print(i)
3
2
1
0

freq = [10, 20, 30, 40]
for i in range(len(freq) - 1, 0, -1):
    print(i)
3
2

count = [10, 20, 30]

for i, value in enumerate(count):
    print(i, value)

0 10
1 20
2 30


result = ""
for i in range (3):
    result += "bang"

print(result)
bangbangbang

nums=list
for i in range(len(nums)-1, -1, -1): #start,stop,decrement

mp = defaultdict(int)
if key not exists, the value will be 0 int

name = "Avanza"
price = "200000000"
year = "2022"

parsed = []
price = int(price)
year = int(year)

parsed.append((name, price, year))

print(parsed)

parsed = [
    ("Avanza", 200000000, 2022),
    ("Brio", 150000000, 2021),
]

print(parsed[0][1])

# Kenapa [0][1]?

# [0] → tuple pertama → ("Avanza", 200000000, 2022)

# [1] → elemen kedua di tuple → 200000000

for name, price, year in parsed:    
    print(name, price, year)



substrings = ["a", "ba"]


''.join(substrings)

