'''product1={'Name':'Laptop', 'Price':100, 'Quantity':1}
product2={'Name':'Keyboard', 'Price':500, 'Quantity':1}
product3={'Name':'Mouse', 'Price':500, 'Quantity':1}
product4={'Name':'Headphone', 'Price':500, 'Quantity':1}'''

cart=[{"name": "Notebook", "price": 120, "quantity": 3},
      {"name": "Pen", "price": 20, "quantity": 5},
      {"name": "USB Drive", "price": 850, "quantity": 2},
      {"name": "Mouse", "price": 650, "quantity": 1}]
total=0
for x in cart:
    total+=x['price']*x['quantity']

def applyDiscount(total):
    if total>2500:
        return total-(total*0.10)
    else:
        print('No discount applied')

print(applyDiscount(total))