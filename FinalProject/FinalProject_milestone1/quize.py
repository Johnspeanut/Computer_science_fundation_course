# def make_dictionary(filename):
#     contents = {}
#     try:
#         with open(filename, 'r') as file:
#             for line in file:
#                 each_line = line.split(",")
#                 if len(each_line) == 2:
#                     contents[each_line[0].strip()] = each_line[1].strip()
#         return contents
#     except FileNotFoundError:
#         print("File doesn't exist")
#         return contents

# print(make_dictionary("try1.txt"))


# def sum_fives(n):
#     if n % 5 != 0:
#         return 0
#     elif n == 0:
#         return 0
#     else:
#         return n + sum_fives(n - 5)

# print(sum_fives(1))


# def test_is_valid_station():
#     assert(is_valid_station("Angle Lake"))
#     assert(not is_valid_station("Bellingham"))


def add_tip(bill_amt, percentage):
      MIN_TIP = 0.1
  MAX_TIP = 1
  if percentage < MIN_TIP:
    raise ValueError("Tip must be at least 0.1 (10%)")
  if percentage > MAX_TIP:
    raise ValueError("Tip must be a float between 0.1 (10%) and 1 (100%)")
  return bill_amt + bill_amt * percentage