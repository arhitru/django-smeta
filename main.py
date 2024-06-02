# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print('x', 'y', 'z', 'w')
for x in range(0,2):
    for y in range(0,2):
        for w in range(0, 2):
            for z in range(0, 2):
                if(not(w<=z) or (x<=y) or not(x)) == 0:
                    print(x, y, z, w)
print()
print('x', 'y', 'z', 'w')
for x in range(0,2):
    for y in range(0,2):
        for w in range(0, 2):
            for z in range(0, 2):
                if(((not(y)<=w) <= (x<=z)) <= (x<=w)) == 0:
                    print(x, y, z, w)

# print()
# b = 0
# for a in range(1, 1000):
#     f = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (not (2*y+3*x==135) or (y>a) or (x>a))==0:
#                 f=False
#     if f:
#         if b < a:
#             b = a
# print(b)

# print()
# b = 0
# for a in range(1, 1000):
#     f = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if (not(y+5*x==135) or (3*x>a) or (y>a))==0:
#                 f=False
#     if f:
#         if b < a:
#             b = a
#             # print(a)
# print('a =', b)

def f(curr, end):
    if curr>end: return 0
    if curr == end: return 1
    if curr < end and curr %10 != 9: 
        return f(curr+1, end) + f(curr + 11, end)
    if curr < end and curr % 10 == 9: return f(curr + 1, end) + f(curr + 10, end)

print(25%10)
print(f(25, 51))
