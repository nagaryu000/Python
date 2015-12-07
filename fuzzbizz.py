prev_error = False
nums = 0

while True:
  try:
    if prev_error:
      print('Please enter number you like again! (0: quit)')
    else:
      print('enter any number you like! (0: quit)')
    nums = int(input())
    prev_error = False
  except:
    prev_error = True
    continue

  if nums <= 0:
    break;
  if nums % 15 == 0:
    print('FizzBuzz')
  elif nums % 5 == 0:
    print('Buzz')
  elif nums % 3 == 0:
    print('Fizz')
  else:
    print(nums)
