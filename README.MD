![1717540564111](image/README/1717540564111.png)

# Proyecto individual N2 - Siniestros Viales

---

### Seguridad Vial Armani - SVA

🚗 Los sucesos viales, también conocidos como accidentes de tráfico, ocurren en las vías públicas e incluyen desde colisiones de vehículos hasta atropellos, choques contra objetos fijos y vuelcos de automóviles. Estos eventos pueden causar daños materiales, lesiones graves o, tristemente, la pérdida de vidas humanas.

🏙️ En una ciudad grande como Buenos Aires, la preocupación por estos incidentes es significativa debido al tráfico denso y la alta densidad poblacional. Esto afecta la seguridad de los residentes y visitantes, así como la infraestructura vial y los servicios de emergencia.

📊 Las estadísticas de mortalidad relacionadas con estos accidentes son indicadores críticos de la seguridad vial. Se evalúan en función del número de fallecimientos en relación con la población o el número de vehículos. Reducir estas cifras es fundamental para mejorar la seguridad y salvar vidas.

En Argentina, alrededor de 4,000 personas pierden la vida anualmente en estos sucesos, siendo la principal causa de muertes violentas. Entre 2018 y 2022, se registraron 19,630 fallecimientos según el Sistema Nacional de Información Criminal, lo que equivale a un promedio de 11 muertes diarias. En 2022, se registraron 3,828 decesos.

🔍 Abordar estos problemas y reducir las tasas de mortalidad es esencial para mejorar la seguridad vial en Buenos Aires y en todo el país.

---

### Descripción del Proyecto

📊 **Propósito:**

* El objetivo principal de este proyecto es realizar un análisis exhaustivo de los datos relacionados con homicidios en accidentes viales ocurridos en la Ciudad de Buenos Aires durante el período de 2016 a 2021.

🎯 **Objetivo:**

* Generar información relevante y detallada que pueda ser utilizada por las autoridades locales. Esta información tiene el propósito de ayudar en la implementación de medidas efectivas que reduzcan la cantidad de víctimas mortales en accidentes de tránsito.

🚦 **Contexto:**

* **Área de Estudio:** Ciudad de Buenos Aires
* **Período de Análisis:** 2016 - 2021
* **Enfoque:** Homicidios en accidentes viales

---

### Metodología y Herramientas

Para llevar a cabo este proyecto, se siguieron los siguientes procesos:

### 🛠️Empezamos por el proceso **ETL (📦 Extract, 🔄 Transform, 📤 Load)**

- 🔍 **Recopilación de Datos:**

  - Se obtuvo un conjunto de datos suministrado por la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires, el cual detallaba información sobre homicidios en accidentes de tránsito.
- **📦 Extraccio**n de datos:

  - La fuente de datos para este proyecto fueron 2 archivos xslx.
  - Podes ver el diccionario de datos de Siniestros Viales tocando **ACALINK**
- 🔄 **Transformaciones de los datos:**

  - Preparamos los datos para correcta lectura:
  - Eliminadas columnas irrelevantes.
  - Eliminados datos faltantes o nulos.
  - Eliminados registros o filas repetidas.
  - Transformaciones en los tipos de datos.
- **📤 Carga de datos limpios**

  - Exportamos los datos como un archivo CSV.
- Podes observar el proceso ETL haciendo click **ACA.**

#### 🔎EDA (Análisis Exploratorio de Datos)

✅ Una vez que toda la data esta limpia gracias al Data Engineer que hizo **🛠️ETL** , hacer 🔎 **EDA** nos permite entender bien los datos a los que tenemos acceso.

Puedes leer un poco más sobre EDA en [este articulo](https://medium.com/swlh/introduction-to-exploratory-data-analysis-eda-d83424e47151)

El codigo usado en esta parte del proceso se encuentra en: ACA LINK

* **Visualización Inicial:** Se crearon gráficos para comprender la distribución y las tendencias de los datos.
* **Identificación de Patrones:** Se analizaron variables influyentes como tiempo, ubicación y circunstancias de los accidentes.

---

### 🔧 **Herramientas y Tecnologías:**

* **Lenguajes de Programación:** Python
* **Herramientas de Análisis:** Pandas, NumPy
* **Visualización:** Matplotlib, Seaborn, Power Bi
* **Fuentes de Datos:** Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires

---

### 📈 **Impacto del EDA:**

La información obtenida a través de este análisis permitirá a las autoridades locales:

* El análisis exploratorio de datos permitió extraer información valiosa sobre tendencias y patrones de homicidios en accidentes de tránsito, fundamentales para desarrollar recomendaciones y políticas que mejoren la seguridad vial.

🚀 **Conclusión:**

Este proyecto busca no solo analizar datos históricos, sino también proporcionar una base sólida para acciones futuras que mejoren la seguridad vial en la Ciudad de Buenos Aires, salvando vidas y mejorando la calidad de vida de sus habitantes.

---

### Estructura de navegación de los archivos:

* **📂 /0 Dataset/**: Contiene las bases de datos utilizadas para este proyecto
* **📂/1 Jupyter Notebook/:** Contiene el **ETL, EDA y data_utils.py** un archivo creado para importar funciones utiles.
* **📂/image/README**: esta carpeta contiene las imagenes utilizadas en el proyecto
* **📂/3 Power Bi/:** contiene la presentacion para Power Bi.

---

### Dashboard en Power Bi

GIF 1 

GIF 2

GIF 3

GIF 4

GIF 5

---

### Conclusiones del analisis para mejorar la situación:

En el análisis pudimos observar diferentes caracteristicas de las victimas y patrones temporales.

Estas son algunas conclusiones:



---

### Recomendaciones para mejorar la situacion


- Análisis Continuo:
- Mejorar la Educación Vial
- Respecto al tipo de vehiculo:
- 
- 

---

### KPI

* **KPI 1: Reducir en un 10% la tasa de homicidios en siniestros viales en los últimos seis meses en comparación con el semestre anterior**

  * **Tasa de homicidios en siniestros viales** : Número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes. Fórmula: (Número de homicidios en siniestros viales / Población total) * 100,000
* **KPI 2: Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año respecto al año anterior** .

  * **Cantidad de accidentes mortales de motociclistas** : Número absoluto de accidentes fatales con víctimas en moto. Fórmula: (Accidentes mortales de motociclistas del año anterior - Accidentes mortales de motociclistas del año actual) / Accidentes mortales de motociclistas del año anterior * 100
* **KPI 3: Disminuir en un 5% la cantidad total de accidentes de tránsito en la Ciudad Autónoma de Buenos Aires (CABA) cada año.**

  * **Reducció**n de Accidentes(**%**)=(total accidentes año anterior - total accidentes año actual) / total accidentes año anterior * 100
  * Si en 2022 hubo 10,000 accidentes y en 2023 se busca reducir esta cifra en un 5%, la meta para 2023 sería tener 9,500 accidentes.

---



### Recomendaciones para mejorar la situacion

- Análisis Continuo:
- Mejorar la Educación Vial
- Respecto al tipo de vehiculo:
- 
-
