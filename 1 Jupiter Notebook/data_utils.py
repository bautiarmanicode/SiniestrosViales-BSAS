
import inspect
import matplotlib.pyplot as plt
import pandas as pd





def data_type_check(df):
    """
    Genera un resumen del DataFrame que incluye la proporción de valores nulos y no nulos, 
    el tipo de datos y la cantidad total de nulos por columna.

    Parámetros:
    df (pandas.DataFrame): El DataFrame a ser analizado.

    Retorna:
    None: Esta función imprime el resumen del DataFrame en la consola.
    """
    # Crear un diccionario para almacenar el resumen de los datos
    dataframe = {
        "columna": [], 
        "%_no_nulos": [], 
        "%_nulos": [], 
        "total_nulos": [], 
        "tipo_dato": []
    }
    
    # Encabezado del resumen
    print("\n" + "=" * 40)
    print(" Resumen del dataframe:")
    print("\n" + "=" * 40)
    
    for columna in df.columns:
        # Calcular el porcentaje de valores no nulos
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        # Obtener el tipo de dato directamente
        tipo_dato = df[columna].dtype  
        # Agregar la información al diccionario
        dataframe["columna"].append(columna)
        dataframe["%_no_nulos"].append(round(porcentaje_no_nulos, 2))
        dataframe["%_nulos"].append(round(100 - porcentaje_no_nulos, 2))
        dataframe["total_nulos"].append(df[columna].isnull().sum())
        dataframe["tipo_dato"].append(tipo_dato)
    
    # Crear el DataFrame con la información recopilada
    df_info = pd.DataFrame(dataframe)
    print("Dimensiones: ", df.shape)
    print(df_info) 



def data_type_check_EDA(df):
    """
Esta función realiza un análisis exploratorio de datos (EDA) sobre un DataFrame de Pandas.
Genera un resumen de las características del DataFrame, incluyendo el nombre de las columnas,
el número y porcentaje de valores nulos y no nulos, y el tipo de datos de cada columna.
Además, crea una visualización de barras horizontales que muestra el porcentaje de valores
nulos y no nulos para cada columna.
"""
    # Crear un diccionario para almacenar el resumen de los datos
    dataframe = {"columna": [], "no_nulos": [], "%_no_nulos": [], "nulos": [], "%_nulos": [], "tipo_dato": []}
    # Obtener el nombre del DataFrame
    nombre_df = [nombre for nombre, var in inspect.currentframe().f_back.f_locals.items() if var is df][0]
    # Imprimir el resumen del DataFrame
    print("\n" + "=" * 40)
    print(f" Resumen del DataFrame '{nombre_df}': ")
    print("\n" + "=" * 40)
    for columna in df.columns:
        # Calcular el porcentaje y la cantidad de valores no nulos
        cantidad_no_nulos = df[columna].count()
        cantidad_nulos = df[columna].isnull().sum()
        total_valores = len(df[columna])
        # Calcular el porcentaje de valores no nulos y nulos
        porcentaje_no_nulos = (cantidad_no_nulos / total_valores) * 100
        porcentaje_nulos = (cantidad_nulos / total_valores) * 100
        # Obtener el tipo de dato de la columna
        tipo_dato = df[columna].dtype  
        # Añadir la información al diccionario
        dataframe["columna"].append(columna)
        dataframe["no_nulos"].append(cantidad_no_nulos)
        dataframe["%_no_nulos"].append(round(porcentaje_no_nulos, 2))
        dataframe["nulos"].append(cantidad_nulos)
        dataframe["%_nulos"].append(round(porcentaje_nulos, 2))
        dataframe["tipo_dato"].append(tipo_dato)
    # Crear un DataFrame con el resumen de los datos
    df_info = pd.DataFrame(dataframe)
    print("Dimensiones: ", df.shape)
    print(df_info)
    
    # Ordenar el DataFrame por el porcentaje de valores nulos de forma descendente
    df_info = df_info.sort_values(by='%_nulos', ascending=False)
    # Graficar el porcentaje de valores nulos y no nulos por columna
    fig, ax = plt.subplots(figsize=(8, 6))
    bars1 = ax.barh(df_info['columna'], df_info['%_nulos'], color='lightcoral', label='Nulos')
    bars2 = ax.barh(df_info['columna'], df_info['%_no_nulos'], left=df_info['%_nulos'], color='lightgreen', label='No Nulos')
    # Agregar un contador de nulos y no nulos en cada barra
    for bar1, bar2, columna, no_nulos, nulos in zip(bars1, bars2, df_info['columna'], df_info['no_nulos'], df_info['nulos']):
        plt.text(bar1.get_width() - 20, bar1.get_y() + bar1.get_height()/2, f" {nulos}", va='center', ha='right', color='black', fontsize=13)
        plt.text(bar1.get_width() + 1, bar2.get_y() + bar2.get_height()/2, f"{no_nulos}", va='center', ha='left', color='black', fontsize=13)

    ax.set_xlabel('Porcentaje de valores')
    ax.set_ylabel('Columna')
    ax.set_title(f'Cantidad de valores nulos y no nulos por columna en {nombre_df}')
    ax.legend()
    ax.invert_yaxis()
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    # Mover la leyenda a la izquierda y abajo del gráfico
    plt.legend(loc='lower left', bbox_to_anchor=(0.0, -0.15), frameon=False)
    
    plt.show()

