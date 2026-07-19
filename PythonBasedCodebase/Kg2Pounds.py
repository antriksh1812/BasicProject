def convertToPounds(kg):
      return kg*2.2
    


try:
 weightInKg = float(input("Enter the weight in Kg"))
 poundsWeight = convertToPounds(weightInKg)
 print(f"poundsWeight {poundsWeight}")
except Exception:
 print('Enter a valid number')
