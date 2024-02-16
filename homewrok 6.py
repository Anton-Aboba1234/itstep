result = []

def divider(a, b):
  try:
    if a < b:
      raise ValueError("a should be greater than or equal to b")
    if b == 0:
      raise ZeroDivisionError("b should be less than or equal to 100")
    if b > 100:
      raise IndexError("b should be less than or equal to 100")
    return a/b
  except ValueError as ve:
    print(f"ValuError occurred: {ve}")
  except ZeroDivisionError as zde:
    print(f"ZeroDivisionError occurred: {zde}")
  except IndexError as ie:
    print(f"IndexError occurred: {ie}")
  except Exception as e:
    print(f"Exception occurred: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
 res = divider(key, data[key])
 result.append(res)

print(result)