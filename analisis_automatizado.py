import pandas as pd
import matplotlib.pyplot as plt
import os

# --- CONFIGURACIÓN DE CARPETAS ---
# Esto soluciona el problema de no tener carpetas en GitHub
for folder in ['data', 'output']:
    if not os.path.exists(folder):
        os.makedirs(folder)

def ejecutar_pipeline():
    print("🚀 Iniciando sistema de automatización...")
    
    # 1. Simulación de datos (En un caso real, leerías un Excel/CSV)
    data = {
        'Fecha': ['2026-01-01', '2026-01-02', '2026-02-01', '2026-02-15', '2026-03-01'],
        'Producto': ['Laptop', 'Mouse', 'Laptop', 'Teclado', 'Mouse'],
        'Ventas': [1200, 25, 1200, 45, 25],
        'Stock': [5, 50, 4, 30, 48]
    }
    df = pd.DataFrame(data)
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # 2. Limpieza y Procesamiento (Pandas)
    # Eliminamos duplicados y calculamos métricas
    df_limpio = df.drop_duplicates()
    resumen = df_limpio.groupby(df_limpio['Fecha'].dt.month_name())['Ventas'].sum()

    # 3. Visualización de Tendencias (Matplotlib)
    plt.figure(figsize=(8, 5))
    resumen.plot(kind='line', marker='o', color='green')
    plt.title('Tendencia de Ventas Mensuales 2026')
    plt.ylabel('Ingresos ($)')
    plt.grid(True)
    
    # Guardar resultado
    plt.savefig('output/reporte_tendencias.png')
    print("✅ Reporte visual generado en /output")
    
    # 4. Exportar a Excel optimizado
    df_limpio.to_excel('output/datos_procesados.xlsx', index=False)
    print("✅ Excel limpio generado en /output")

if __name__ == "__main__":
    ejecutar_pipeline()
