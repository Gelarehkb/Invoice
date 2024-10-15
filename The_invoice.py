chairs = int(input("Input the number of ordered chairs: "))
tables = int(input("Input the number of ordered tables: "))
lamps = int(input("Input the number of ordered lamps: "))

chairs_price=49.99
tables_price=199.99
lamp_price=29.99

chairs_total = chairs * chairs_price
tables_total = tables * tables_price
lamps_total = lamps * lamp_price
total = chairs_total + tables_total + lamps_total
print()
print("Order Form:")
print("---------------------------------")
print(f"Chairs: {chairs:3} x {chairs_price:6.2f} = {chairs_total:10.2f}")
print(f"Tables: {tables:3} x {tables_price:6.2f} = {tables_total:10.2f}")
print(f"Lamps: {lamps:4} x {lamp_price:6.2f} = {lamps_total:10.2f}")
print("---------------------------------")
print(f"Total: {total:26.2f}")
print("=================================")
