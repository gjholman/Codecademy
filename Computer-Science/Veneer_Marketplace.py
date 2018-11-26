# Veneer Marketplace
# Codecademy project to practice object oriented programming
# 11/18

# Class Definitions
class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return('{artist}. "{title}". {year}, {medium}. Owned by {owner_name}, {owner_location}'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner_name=self.owner.name, owner_location=self.owner.location))
   
class Marketplace:
  def __init__(self):
    self.listings = []
  
  def add_listing(self, listing):
    self.listings.append(listing)
    
  def remove_listing(self, listing):
    self.listings.remove(listing)
    
  def show_listings(self):
    print("VENEER LISTINGS")
    if not self.listings:
      print("Listing is empty")
    else:
      for m_listing in self.listings:
        print("{listing} \n".format(listing=m_listing))

# Instantiate Martketplace
veneer = Marketplace()
#In order to use the marketplace

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  def sell_artwork(self, artwork, price):
    if(artwork.owner==self):
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
      
  def buy_artwork(self, artwork):
    if(artwork.owner!=self):
      for listing in veneer.listings:
        if(artwork == listing.art):
          artwork.owner = self
          veneer.remove_listing(listing)
        
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return('{name}, {price}'.format(name=self.art.title, price=self.price))
    
# Creating Clients
edytta = Client('Edytta Halpirt', 'Private Collection', False)
moma = Client('THE MOMA', 'New York', True)

# Creating Art
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
print('Created art, printing girl with mandolin\n')
print(girl_with_mandolin)

# Actions in the market
veneer.show_listings()
print("\n>>selling artwork\n")
edytta.sell_artwork(girl_with_mandolin, 6000000)
print("Sold art, showing listings\n")
veneer.show_listings()
print(">>moma buys artwork \n")
moma.buy_artwork(girl_with_mandolin)
veneer.show_listings()
print("\nPrinting girl with Mandolin\n")
print(girl_with_mandolin)
