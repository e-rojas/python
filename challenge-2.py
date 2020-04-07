premium_charge = 125.00

def ground_ship_cost(weight):
   flat_charge = 20
   if weight <= 2:
    return weight * 1.50 + flat_charge
   elif (weight >2 ) and (weight <= 6):
     return weight * 3 + flat_charge
   elif ((weight > 6) and (weight <= 10)):
     return weight * 4 + flat_charge
   elif weight >= 10:
     return weight * 4.75 + flat_charge

def drone_shipping(weight):
    cost = 0
    
    if weight < 2:
      cost = weight * 4.50
    elif weight > 2 and weight<= 6:
      cost = weight * 9.00
    elif weight > 6 and weight<= 10:
      cost = weight * 12.00
    elif weight >= 10:
      cost = weight * 14.25
    return cost 

def cheap_method(weight):
  if ground_ship_cost(weight) < drone_shipping(weight) :
      return 'Ground shipment is the cheapest.'
  else:
    return 'Drone shipment is the cheapest.'
  

print(cheap_method(41.5))