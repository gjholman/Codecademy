def find_cheapest_shipping(package_weight):
  ground = cost_ground(package_weight)
  drone = cost_drone(package_weight)
  premium = cost_premium(package_weight)
  
  if(ground <= drone and ground <= premium):
    print("Using the ground would cost: " + str(ground))
  if(drone <= ground and drone <= premium):
    print("Using the drone would cost: " + str(drone))
  if(premium <= drone and premium <= ground):
    print("Using the premium ground would cost: " + str(premium))
  
  #going to return with the price and the type of shipping to do so
  #assuming package weight is given in pounds and no conversion necessary
  return(cost_ground(package_weight))
  
  
  
def cost_ground(weight):
  flat_charge = 20
  additional_ppp = 0
  
  if(weight <= 2):
    additional_ppp = 1.50 * weight
  elif(weight <= 6):
    additional_ppp = 3.00 * weight
  elif(weight <= 10):
    additional_ppp = 4.00 * weight
  elif(weight > 10):
    additional_ppp = 4.75 * weight
    
  return flat_charge + additional_ppp

def cost_drone(weight):
  flat_charge = 0
  additional_ppp = 0
  
  if(weight <= 2):
    additional_ppp = 4.50 * weight
  elif(weight <= 6):
    additional_ppp = 9.00 * weight
  elif(weight <= 10):
    additional_ppp = 12.00 * weight
  elif(weight > 10):
    additional_ppp = 14.25 * weight
    
  return flat_charge + additional_ppp

def cost_premium(weight):
  flat_charge = 125
  return flat_charge


find_cheapest_shipping(4.8)
find_cheapest_shipping(41.5)
