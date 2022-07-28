## Variables
temperature = 81
forecast = "rain"

## <if> <and> Operators
#if temperature < 80 and forecast != "rain":
 # print("Go outside!")

## <if> <or> Operators 
# if temperature > 80 or temperature < 60:
   # print("It's too hot!")
    #print("Stay inside")

## <elif> (Else if) Operator
# elif temperature < 60:
  #  print("It's too cold!")
  #  print("Stay inside!")
#else:
    # print("Weather is great! Enjoy the outdoors!")
#    print("Stay inside!")

## LOGICAL OPERATOR - not
if not forecast == "rain":
  print("Go outside!")
else:
  print("Stay inside!") 
  