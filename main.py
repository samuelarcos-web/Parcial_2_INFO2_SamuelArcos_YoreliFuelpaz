from erp_clases import ArchivoCSV, validar_entero
import os

def menu_principal():
    while True:
        print("\n--- SISTEMA ERP ---")
        print("1. Procesar CSV")
        print("2. Procesar MAT")
        print("3. Salir")
        opcion = validar_entero("Seleccione una opción: ", 1, 3)

        if opcion == 1:
            ruta = input("Ingrese el nombre del archivo CSV (ej. ERP_01.csv): ")
            if not os.path.exists(ruta):
                print("El archivo no existe.")
                continue
            obj_csv = ArchivoCSV(ruta)
            print("Archivo CSV cargado exitosamente en memoria.")
            
        elif opcion == 3:
            print("Saliendo...")
            break

if __name__ == "__main__":
    menu_principal()