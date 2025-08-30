
# Modelo DuPont - Rentabilidad de Negocios

Este proyecto implementa un modelo DuPont para medir la rentabilidad de un negocio utilizando datos financieros básicos. La aplicación está construida en **Streamlit** y permite cargar un archivo de datos (Excel o CSV) con información de la empresa para calcular los indicadores financieros clave, tales como el **ROE**, **ROA**, **PayBack Capital**, entre otros.

## Características

- **Cálculos del Modelo DuPont**:
  - **Margen Neto (%)** = Utilidad Operativa / Ventas
  - **Rotación (veces)** = Ventas / Activos Totales
  - **Apalancamiento (veces)** = Activos Totales / Capital Contable
  - **ROE (%)** = Margen Neto × Rotación
  - **ROA (%)** = Rotación × Apalancamiento
  - **Pay Back Capital (veces)** = 1 / ROE
  - **Pay Back Activos (veces)** = 1 / ROA

- Los resultados se presentan con **1 decimal** de precisión.
- Los cálculos son realizados automáticamente por **Streamlit**, y los resultados se muestran con los períodos en las columnas y los conceptos en las filas.
- **Descarga en formato Excel** o **CSV** para análisis posterior.

## Requisitos

Para ejecutar la aplicación, necesitas instalar las siguientes bibliotecas:

- `streamlit`
- `pandas`
- `numpy`
- `openpyxl` (para exportar el reporte a Excel)

Puedes instalar las dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

### `requirements.txt`:

```
streamlit
pandas
numpy
openpyxl
```

## Instrucciones de uso

1. **Cargar el archivo de datos**:
   - La aplicación requiere un archivo **Excel** o **CSV** con las siguientes columnas:
     - **Utilidad Operativa**
     - **Cuentas por cobrar neto**
     - **Inventarios**
     - **Cuentas por pagar**
   - Las filas del archivo deben corresponder a los años (por ejemplo, 1992, 1993, 1994, etc.).

2. **Ejecutar la aplicación**:
   - Guarda el archivo `app.py` en tu directorio.
   - Abre una terminal y navega hasta el directorio donde guardaste `app.py`.
   - Ejecuta el siguiente comando:
     ```bash
     streamlit run app.py
     ```

3. **Interactuar con la aplicación**:
   - En la barra lateral, selecciona tu archivo **Excel** o **CSV**.
   - Los resultados del modelo DuPont se mostrarán en una tabla con los períodos como columnas y los conceptos como filas.
   - Puedes descargar el reporte como un archivo **Excel** o **CSV** desde la aplicación.

## Ejemplo de archivo

A continuación se muestra un ejemplo del formato que debe tener el archivo de entrada:

| Estado de resultados      | 1992     | 1993     | 1994  | 1995  | 1996  |
|---------------------------|----------|----------|-------|-------|-------|
| Utilidad Operativa         | 67.000   | 139.000  | -39   | 249   | 377   |
| Depreciaciones             | 5.000    | 5.000    | 5     | 7     | 12    |
| Cuentas por cobrar neto    | 128.556  | 292.030  | 411   | 538   | 726   |
| Inventarios                | 69.244   | 163.134  | 220   | 293   | 429   |
| Cuentas por pagar          | 117.480  | 261.820  | 538   | 403   | 466   |

## Contribuciones

Si tienes alguna mejora o sugerencia, ¡estaré encantado de recibir una **pull request**!

---

**Autor**: Izhar Santillan Quintero  
**Licencia**: MIT
