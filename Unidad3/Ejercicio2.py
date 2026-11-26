''' Una tienda da 10% de descuento si la compra es de $1000 o más.
Haz un programa que pida el total y muestre el descuento y el total a pagar.

Tu programa debe de dar estos resultados.

Monto    Descuento    Total
500        150        1350
1000       100        900 
999        99         899
'''

total = float(input("Ingresa el total"))

if total >= 1000:
    print("Total_a_pagar:", total * 0.90)

else:
    print(total)
