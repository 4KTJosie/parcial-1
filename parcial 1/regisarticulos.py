import redis
import json

# Conectar a la base de datos KeyDB
keydb = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Función para agregar un artículo
def agregar_articulo():
    nombre = input("Nombre del artículo: ")
    categoria = input("Categoría: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")

    # Crear un diccionario con los datos del artículo
    articulo = {
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
    }

    # Guardar el artículo en KeyDB (clave: nombre del artículo)
    keydb.set(nombre, json.dumps(articulo))
    print("Artículo agregado con éxito.")

# Función para actualizar un artículo existente
def actualizar_articulo():
    ver_articulos()
    nombre = input("Nombre del artículo a actualizar: ")

    # Verificar si el artículo existe
    if keydb.exists(nombre):
        articulo = json.loads(keydb.get(nombre))
        print(f"Nombre actual: {articulo['nombre']}")
        print(f"Categoría actual: {articulo['categoria']}")
        print(f"Cantidad actual: {articulo['cantidad']}")
        print(f"Precio actual: {articulo['precio']}")

        nuevo_nombre = input("Nuevo nombre del artículo (deja en blanco para no cambiar): ")
        nueva_categoria = input("Nueva categoría (deja en blanco para no cambiar): ")
        nueva_cantidad = input("Nueva cantidad (deja en blanco para no cambiar): ")
        nuevo_precio = input("Nuevo precio (deja en blanco para no cambiar): ")

        if nuevo_nombre:
            articulo["nombre"] = nuevo_nombre
        if nueva_categoria:
            articulo["categoria"] = nueva_categoria
        if nueva_cantidad:
            articulo["cantidad"] = nueva_cantidad
        if nuevo_precio:
            articulo["precio"] = nuevo_precio

        # Actualizar el artículo en KeyDB
        keydb.delete(nombre)
        keydb.set(articulo["nombre"], json.dumps(articulo))
        print("Artículo actualizado con éxito.")
    else:
        print("Artículo no encontrado.")

# Función para eliminar un artículo existente
def eliminar_articulo():
    ver_articulos()
    nombre = input("Nombre del artículo a eliminar: ")

    # Eliminar el artículo de KeyDB
    if keydb.exists(nombre):
        keydb.delete(nombre)
        print("Artículo eliminado con éxito.")
    else:
        print("Artículo no encontrado.")

# Función para ver el listado de artículos
def ver_articulos():
    claves = keydb.keys()
    print("\nListado de artículos:")
    for clave in claves:
        articulo = json.loads(keydb.get(clave))
        print(f"Nombre: {articulo['nombre']}, Categoría: {articulo['categoria']}, Cantidad: {articulo['cantidad']}, Precio: {articulo['precio']}")
    print()

# Función para buscar un artículo
def buscar_articulo():
    nombre = input("Nombre del artículo a buscar: ")

    # Buscar el artículo por nombre en KeyDB
    if keydb.exists(nombre):
        articulo = json.loads(keydb.get(nombre))
        print("\nCategoría:", articulo["categoria"])
        print("Cantidad:", articulo["cantidad"])
        print("Precio:", articulo["precio"])
    else:
        print("Artículo no encontrado.")

# Menú principal
def menu():
    while True:
        print("\n--- Sistema de Registro de Presupuesto ---")
        print("1. Agregar nuevo artículo")
        print("2. Actualizar artículo existente")
        print("3. Eliminar artículo existente")
        print("4. Ver listado de artículos")
        print("5. Buscar artículo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_articulo()
        elif opcion == '2':
            actualizar_articulo()
        elif opcion == '3':
            eliminar_articulo()
        elif opcion == '4':
            ver_articulos()
        elif opcion == '5':
            buscar_articulo()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    menu()
