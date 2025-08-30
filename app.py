{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import numpy as np\
from io import BytesIO\
\
# -------------------------------------------------------------\
# Streamlit App: Modelo DuPont para medir rentabilidad\
# -------------------------------------------------------------\
\
st.set_page_config(page_title="Modelo DuPont \'95 Rentabilidad", layout="wide")\
st.title("\uc0\u55357 \u56522  Modelo DuPont \'97 Rentabilidad de Negocios")\
st.caption("Sube tu base de datos y genera el reporte con periodos en columnas y conceptos en renglones, con 1 decimal.")\
\
# -------------------------------\
# Funciones\
# -------------------------------\
\
def load_data(uploaded_file):\
    """Cargar archivo Excel o CSV."""\
    if uploaded_file is not None:\
        name = uploaded_file.name.lower()\
        if name.endswith("xlsx") or name.endswith("xls"):\
            return pd.read_excel(uploaded_file, sheet_name=None)\
        elif name.endswith("csv"):\
            return pd.read_csv(uploaded_file)\
        else:\
            st.warning("Formato no soportado. Usa Excel o CSV.")\
            return None\
    return None\
\
def calculate_dupont(df):\
    """Calcular los indicadores del modelo DuPont."""\
    # Ventas = Utilidad Operativa\
    ventas = df['Utilidad Operativa']\
    # Activos = Cuentas por cobrar neto + Inventarios\
    activos = df['Cuentas por cobrar neto'] + df['Inventarios']\
    # Capital = Cuentas por pagar\
    capital = df['Cuentas por pagar']\
\
    # C\'e1lculos del modelo DuPont\
    margen_neto = df['Utilidad Operativa'] / ventas\
    rotacion = ventas / activos\
    apalancamiento = activos / capital\
    roe = margen_neto * rotacion\
    roa = rotacion * apalancamiento\
    payback_capital = 1 / roe\
    payback_activos = 1 / roa\
\
    # Crear el reporte en formato de filas como conceptos y columnas como periodos\
    report = pd.DataFrame(\{\
        "Margen Neto (%)": margen_neto * 100,\
        "Rotaci\'f3n (veces)": rotacion,\
        "Apalancamiento (veces)": apalancamiento,\
        "ROE (%)": roe * 100,\
        "ROA (%)": roa * 100,\
        "Pay Back Capital (veces)": payback_capital,\
        "Pay Back Activos (veces)": payback_activos\
    \}, index=df.index)\
\
    return report\
\
def format_report(report):\
    """Formatear los resultados a 1 decimal."""\
    return report.applymap(lambda x: f"\{x:.1f\}" if isinstance(x, (int, float)) else x)\
\
def to_excel(df):\
    """Convertir el reporte a formato Excel para descarga."""\
    buffer = BytesIO()\
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:\
        df.to_excel(writer, index=True)\
    buffer.seek(0)\
    return buffer.read()\
\
# -------------------------------\
# Cargar datos\
# -------------------------------\
st.sidebar.header("Cargar archivo")\
uploaded_file = st.sidebar.file_uploader("Sube archivo Excel (CSV o XLSX)", type=["csv", "xlsx", "xls"])\
\
if uploaded_file is not None:\
    # Cargar datos del archivo\
    df = load_data(uploaded_file)\
\
    if df is not None:\
        # Procesar los datos\
        sheet_data = df.get('Sheet1', None)\
\
        if sheet_data is not None:\
            # Aseguramos que las columnas sean correctas\
            df_data = sheet_data.set_index('Estado de resultados').T\
            report = calculate_dupont(df_data)\
            report_formatted = format_report(report)\
\
            # Mostrar el reporte\
            st.subheader("Reporte DuPont")\
            st.dataframe(report_formatted, use_container_width=True)\
\
            # Descargar el reporte\
            st.download_button(\
                label="Descargar Reporte (Excel)",\
                data=to_excel(report_formatted),\
                file_name="reporte_dupont.xlsx",\
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"\
            )\
        else:\
            st.warning("La hoja 'Sheet1' no contiene los datos esperados.")\
else:\
    st.info("Sube un archivo para ver los resultados.")\
}