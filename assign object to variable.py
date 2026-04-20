try:
  result = 10 / 0
except ZeroDivisionError as e:
  exception_object = e
  print(exception_object)