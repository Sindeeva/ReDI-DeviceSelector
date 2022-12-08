deviceData = [  # [DN, min.flow, max.flow, nominal flow, price]
  [20, 0.06, 7.9, 6.3, 1140], [25, 0.1, 20.0, 12.5, 1166],
  [32, 0.25, 31.3, 25.0, 1518], [40, 0.4, 50.0, 40.0, 1673],
  [50, 0.63, 78.8, 63.0, 1598], [65, 1.0, 125.0, 100, 1741],
  [80, 1.6, 200.0, 160, 1857], [100, 2.5, 312.5, 250.0, 2018],
  [125, 4.0, 500.0, 400.0, 2286], [150, 6.30, 787.5, 630.0, 2644],
  [200, 10.0, 1250.0, 1000.0, 3379], [250, 20.0, 2500.0, 2000.0, 3749],
  [300, 25.0, 3125.0, 2500.0, 4815], [350, 35.0, 3500.0, 3000.0, 4888],
  [400, 45.0, 5625.0, 4500.0, 5724], [500, 71.0, 7100.0, 6300.0, 7396],
  [600, 102.0, 10200.0, 8000.0, 9504], [700, 140.0, 14000.0, 12000.0, 12294],
  [800, 180.0, 18000.0, 16000.0, 14675], [900, 230.0, 23000.0, 20000.0, 16528],
  [1000, 285.0, 28500.0, 25000.0, 20243],
  [1200, 410.00, 41000.0, 37000.0, 17915]
]

neededParameters = [-1, -1, -1]
param = ""
print("Please select a technical parameter from this list:")
while (param != "n"):
  param = input("DN\nMin.flow\nMax.flow\n")
  paramIndex = 0
  if param == "DN":
    paramIndex = 0
  elif param == "Min.flow":
    paramIndex = 1
  elif param == "Max.flow":
    paramIndex = 2
  else:
    print("Please enter a valid parameter from the list:")
    continue

  print("Please enter the value of this parameter.")
  if paramIndex == 0:
    print("Note that the DN can range from 20 to 1200 mm.")
  paramValue = float(input())
  if paramIndex == 0 and (paramValue < 20 or paramValue > 1200):
    print("Invalid DN value. Please try again")
    print("Please enter a valid parameter from the list:")
    continue
  neededParameters[paramIndex] = paramValue
  param = input("Would you like to add another parameter? y/n")

possibleChoices = deviceData

# Check DN
if neededParameters[0] != -1:
  for i in range(0, len(possibleChoices) - 1):
    if neededParameters[0] == possibleChoices[i][0]:
      possibleChoices = [possibleChoices[i]]
      break
    elif i + 1 < len(possibleChoices) and neededParameters[
        0] > possibleChoices[i][0] and neededParameters[0] < possibleChoices[
          i + 1][0]:
      possibleChoices = [possibleChoices[i], possibleChoices[i + 1]]
      break


# Check min. range
if (neededParameters[1] != -1):
  i = 0
  while i < len(possibleChoices):
    if neededParameters[1] < possibleChoices[i][1]:
      possibleChoices.pop(i)
    else:
      i += 1

# Check max. range
if (neededParameters[2] != -1):
  i = 0
  while i < len(possibleChoices):
    if neededParameters[2] > possibleChoices[i][2]:
      possibleChoices.pop(i)
    else:
      i += 1

if len(possibleChoices) == 0:
  print("Unfortunately, we've been unable to find a device that would fulfill your request.")
elif len(possibleChoices) == 1:
  print("This model may be suitable for you:")
else:
  print("These models may be suitable for you:")
for i in possibleChoices:
  print("SVTU-11B/DN" + str(i[0]) + "\nPrice: " + str(i[4]) + "$")
