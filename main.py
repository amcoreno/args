# args means i can use as many arguments as possible

def sum(*args):
  total = 0
  for arg in args:
    total += arg
  return total

print(sum(2,3, 767, 77, 66, 556, 65, 6, 878, 21, 93, 465))

#  kwargs are using key values and are limitless jut like the args are