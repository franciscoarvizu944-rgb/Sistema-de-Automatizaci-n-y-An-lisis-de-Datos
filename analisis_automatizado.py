import pandas as pd
import matplotlib.pyplot as plt
import os

def inicializar_entorno():
    """Crea las carpetas necesarias para el proyecto."""
    for carpeta in ['data', 'output']:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"Carpeta '{carpeta}' creada.")

def crear_data_ejemplo():
    """Genera un archivo CSV de prueba si no existe."""
    path = 'data/ventas_crudo.csv'
    if not os.path.exists(path):
        data = {
            'Fecha': ['2026-01-01', '2026-01-01', '2026-01-02', '2026-02-01', '2026-02-15', '2026-03-01'],
            'Producto': ['Laptop', 'Laptop', 'Mouse', 'Laptop', 'Teclado', 'Mouse'],
            'Ventas': [1200, 1200, 25, 1250, 45, 30], # Incluye un duplicado para limpiar
            'Vendedor': ['Ana', 'Ana', 'Luis', 'Ana', 'Pedro', 'Luis']
        }
        pd.DataFrame(data).to_csv(path, index=False)
        print("Dataset de prueba generado en /data.")

def procesar_datos():
    print("--- Iniciando Procesamiento ---")
    # Leer datos
    df = pd.read_csv('data/ventas_crudo.csv')
    
    # 1. Limpieza de duplicados
    antes = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Limpieza completa: Se eliminaron {antes - len(df)} registros duplicados.")

    # 2. Transformación
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Mes'] = df['Fecha'].dt.strftime('%B')
    
    # 3. Análisis: Ventas por mes
    reporte_mes = df.groupby('Mes')['Ventas'].sum().reset_index()
    
    # 4. Generar Gráfica
    plt.figure(figsize=(10, 5))
    plt.bar(reporte_mes['Mes'], reporte_mes['Ventas'], color='#3498db')
    plt.title('Reporte Automatizado: Ventas por Mes')
    plt.xlabel('Mes')
    plt.ylabel('Ventas ($)')
    plt.savefig('output/reporte_tendencias.png')
    
    # 5. Exportar Excel
    df.to_excel('output/datos_procesados.xlsx', index=False)
    print("Éxito: Reportes generados en la carpeta /output")

if __name__ == "__main__":
    inicializar_entorno()
    crear_data_ejemplo()
    procesar_datos()
