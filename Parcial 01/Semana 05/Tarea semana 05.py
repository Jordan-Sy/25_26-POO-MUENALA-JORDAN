# Programa: Calculadora del precio final de un producto con descuento e IVA.
# Este programa permite ingresar los datos básicos de un producto,
# calcula su precio final y determina si es considerado "caro" según un criterio definido.

# Datos del producto
nombre_producto = "Audífonos Over-Ear"   # TIpo de dato string
precio_base = 42.99                      # Tipo de dato float
porcentaje_descuento = 15                # Tipo de dato int
porcentaje_iva = 12                      # TIpo de dato int

# Cálculo del descuento
monto_descuento = (precio_base * porcentaje_descuento) / 100
precio_con_descuento = precio_base - monto_descuento

# Cálculo del IVA
monto_iva = (precio_con_descuento * porcentaje_iva) / 100
precio_final = precio_con_descuento + monto_iva

# Criterio para determinar si es un producto caro
umbral_caro = 50.00                      # Tipo de dato float
es_caro = precio_final > umbral_caro     # Tipo de dato boolean

# Resultados
print("Producto:", nombre_producto)
print("Precio base:", precio_base)
print("Descuento aplicado:", porcentaje_descuento, "%")
print("Precio después del descuento:", round(precio_con_descuento, 2))
print("IVA aplicado:", porcentaje_iva, "%")
print("Precio final a pagar:", round(precio_final, 2))
print("¿El producto es considerado caro?:", es_caro)