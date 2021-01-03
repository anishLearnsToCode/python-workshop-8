# this is amazing i really like this i like how amazing it is
"""
{
    this: 2
    is: 2
    amazing: 2
    i: 2
    really: 1
    like: 2
    how: 1
}
"""

passage = input()
words = passage.split()
# print(words)
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
