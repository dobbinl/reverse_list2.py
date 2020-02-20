def reverse_list(vals):
   """
   Pass in object and reverses order of existing list
   """
   reversed_vals = vals[::-1]
   vals.clear()
   vals.extend(reversed_vals)

vals = [7, -3, 12, 9]
reverse_list(vals)
print(vals)