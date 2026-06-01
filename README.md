# Data Cave

> Portfolio de prácticas y proyectos en análisis y ciencia de datos — construido de forma progresiva, desde la conexión a bases de datos hasta machine learning en la nube.

---

## Stack tecnológico

### Lenguaje y entorno
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

### Datos y bases de datos
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

### Visualización
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)

### Machine Learning y ciencia de datos
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)

### Plataforma cloud
![Azure](https://img.shields.io/badge/Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)

---

## Estructura del repositorio

```
Data_cave/
├── CRUD_ON_DB/          # Operaciones de base de datos y análisis multi-fuente
├── mining/              # Primer acercamiento a minería de datos y EDA profundo
└── science_notebooks/   # Análisis de redes, optimización, ML y visualizaciones
    └── Data fabric/     # Prácticas en el entorno Microsoft Fabric / Azure ML
```

---

## Módulos

### `CRUD_ON_DB` — Ingeniería de datos y bases de datos relacionales

Prácticas completas de ingesta, manipulación y control de transacciones sobre bases de datos reales. Los contenedores MySQL y PostgreSQL se levantan mediante **Docker Compose**, replicando un entorno de trabajo real.

| Archivo | Descripción |
|---|---|
| `docker-compose.yml` | Orquestación de contenedores MySQL 8.0 + PostgreSQL 15 |
| `crud_create/read/update/delete.py` | Operaciones CRUD completas con **mysql-connector** y visualización de resultados |
| `transaction_rollback.py` | Demostración de propiedades **ACID** con manejo de errores y `ROLLBACK` en psycopg2 |
| `transaction_commit.py` | Flujo de transacción exitosa con `COMMIT` explícito |
| `exercise1_csv.py` | Ingesta y análisis de datos desde archivos **CSV** |
| `exercise2_mysql.py` | Conexión y consultas con `conn.cursor()` sobre MySQL |
| `exercise3_postgresql.py` | Conexión a PostgreSQL, queries SQL con agregaciones y visualización con matplotlib |
| `exercise4_json.py` | Procesamiento de datos semiestructurados desde **JSON** |
| `exercise_5api.py` | Conexión a API REST pública (CoinGecko) y análisis de datos en tiempo real |
| `data_quality_assesment.py` | Perfilado de calidad de datos cruzando fuentes MySQL y PostgreSQL |
| `init_mysql.sql` / `init_postgres.sql` | Scripts de inicialización de esquemas |

**Habilidades demostradas:** diseño de esquemas SQL, gestión de transacciones, integridad de datos (ACID), multi-source data ingestion (CSV · JSON · REST API · MySQL · PostgreSQL), visualización analítica integrada al pipeline.

---

### `mining` — Minería de datos y EDA profundo

Primera inmersión en el ciclo completo de pre-procesamiento de datos, con énfasis en comprensión estadística antes de modelar.

| Archivo | Descripción |
|---|---|
| `NB1.1 EDA.ipynb` | EDA completo sobre el dataset *Garment Worker Productivity* (UCI ML Repository) |
| `mine1.py` | Fundamentos teóricos y conceptuales de minería de datos |
| `Random fores.py` | Conceptos de Random Forest + implementación con scikit-learn sobre Iris dataset |

**El notebook `NB1.1 EDA.ipynb` cubre:**

- **Análisis univariado:** detección programática de variables numéricas, binarias, ordinales y nominales; estadísticas descriptivas; histogramas y boxplots
- **Calidad de datos:** valores faltantes, duplicados, columnas near-constant, corrección de typos en categorías
- **Estadística inferencial:** skewness, kurtosis (Fisher), detección de outliers por IQR (mild 1.5× / extreme 3.5×)
- **Análisis multivariado:** heatmap de correlación de Pearson, ranking de features vs. target, scatter plots con r y p-value
- **Profiling automatizado:** reporte HTML con YData Profiling (ex pandas-profiling)

**Habilidades demostradas:** ciclo EDA completo, limpieza y clasificación de variables, análisis estadístico formal, pre-modelado, toma de decisiones basada en datos.

---

### `science_notebooks` — Ciencia de datos aplicada

Repertorio de notebooks que cubren análisis de redes, optimización de sistemas, fundamentos de visualización y análisis exploratorio de churn.

| Archivo | Descripción |
|---|---|
| `facebook_networking.ipynb` | Análisis de red social con **NetworkX** sobre el dataset de Facebook ego-graphs |
| `Scenter_optimization.ipynb` | Optimización de colas y staffing con simulación de eventos discretos usando **SimPy** |
| `first_EDA_VIZUAL.ipynb` | Rediseño de visualizaciones (Actividad 3) — principios de percepción visual |
| `several_visualizations.ipynb` | Catálogo de gráficos con matplotlib y seaborn: histogramas, boxplots, scatter, heatmaps |
| `analisis.ipynb` | Análisis exploratorio de dataset de churn de clientes |

**Habilidades demostradas:** teoría de grafos aplicada, simulación de sistemas, diseño de visualizaciones efectivas, análisis de comportamiento de clientes.

---

### `science_notebooks/Data fabric` — Machine Learning en Microsoft Azure

Prácticas desarrolladas dentro del entorno **Microsoft Fabric** (Synapse Analytics + Azure ML), con integración de MLflow para tracking de experimentos.

| Archivo | Descripción |
|---|---|
| `linear&andlogistic_datafabric.ipynb` | Regresión lineal y logística sobre el dataset de diabetes de Azure Blob Storage |
| `ml1.1.ipynb` | Clasificación binaria con regresión logística y **K-Nearest Neighbors** (Iris dataset) |
| `neuron1.ipynb` | Red neuronal con **TensorFlow/Keras** para conversión de temperaturas (Celsius → Fahrenheit) |
| `mlflow autologs work.png` | Captura del tracking de métricas con MLflow autolog |
| `ROC curve logistic.png` | Curva ROC del modelo de regresión logística |
| `raining_precision_recall_curve.png` | Curva Precision-Recall del pipeline de clasificación |

**Habilidades demostradas:** regresión lineal y logística, clasificación con KNN, redes neuronales densas (Dense layers, función sigmoid, optimizador Adam), lectura de datos desde Azure Blob Storage (Spark/WASBS), tracking de experimentos con MLflow, evaluación de modelos (ROC, Precision-Recall, Accuracy).

---

## Perfil de habilidades

### Ingeniería de datos
- Conexión y operación sobre bases de datos relacionales (MySQL, PostgreSQL) desde Python
- Fundamentos de `cursor`, `commit`, `rollback` y propiedades ACID
- Ingesta multi-fuente: archivos planos (CSV/JSON), bases de datos relacionales y APIs REST
- Orquestación de entornos de datos con Docker Compose

### Análisis y exploración de datos
- EDA completo: detección de tipos, calidad, distribuciones, outliers y correlaciones
- Estadística descriptiva e inferencial: media, mediana, desviación estándar, skewness, kurtosis, IQR
- Análisis univariado y multivariado
- Profiling automatizado con YData Profiling

### Machine Learning
- Algoritmos supervisados: Regresión Lineal, Regresión Logística, KNN, Random Forest
- Redes neuronales con TensorFlow/Keras (arquitectura secuencial, función de pérdida MSE)
- Evaluación de modelos: Accuracy, curva ROC, Precision-Recall
- Tracking de experimentos con MLflow

### Visualización de datos
- Matplotlib y Seaborn: histogramas, boxplots, scatter plots, heatmaps, gráficos de barras
- Diseño de visualizaciones orientadas a la comunicación de resultados
- Generación de reportes HTML interactivos

### Ciencia de datos aplicada
- Análisis de redes sociales con NetworkX (grafos, nodos, aristas, estructura de comunidades)
- Simulación de sistemas de colas con SimPy (optimización de staffing)

---

## Cómo ejecutar

### CRUD_ON_DB
```bash
# Levantar las bases de datos
cd CRUD_ON_DB
docker-compose up -d

# Ejecutar cualquier ejercicio
python crud_create.py
python transaction_rollback.py
```

### Notebooks
```bash
# Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate   # Linux/Mac
pip install pandas numpy matplotlib seaborn scikit-learn scipy networkx simpy ydata-profiling jupyter ucimlrepo

# Abrir Jupyter
jupyter notebook
```

---

*Trabajo en progreso — construido de forma incremental mientras avanzo en mi formación como Ingeniero de Datos.*
