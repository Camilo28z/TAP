import streamlit as st

# Título de la aplicación
st.title("Interfaz de Chequeo para Estrategia de Trading")

# Inicializar variables de puntuación
puntuacion_total = 0
puntuacion_maxima = 12

# Paso 1: Revisar la Macrotendencia
st.subheader("Paso 1: Revisar la Macrotendencia")
macrotendencia = st.checkbox("¿Macrotendencia Alcista/Bajista confirmada?")
if macrotendencia:
    puntuacion_total += 1

# Paso 2: Zona de Reversión (ZR)
st.subheader("Paso 2: Zona de Reversión (ZR)")
zona_reversion = st.checkbox("¿Precio está en la Zona de Reversión (ZR) entre niveles 0.618 y 0.786 de Fibonacci?")
if zona_reversion:
    puntuacion_total += 2

# Paso 3: Zona PHY
st.subheader("Paso 3: Zona PHY")
zona_phy = st.checkbox("¿Precio está en la Zona PHY entre niveles 1.272 y 1.618 de Fibonacci?")
if zona_phy:
    puntuacion_total += 2

# Paso 4: Análisis de Microtendencia
st.subheader("Paso 4: Análisis de Microtendencia")
microtendencia = st.checkbox("¿Microtendencia confirmada (canales o movimientos laterales)?")
if microtendencia:
    puntuacion_total += 1

# Paso 5: Confirmación con Indicadores
st.subheader("Paso 5: Confirmación con Indicadores")
indicador_adx = st.checkbox("¿Indicador ADX confirma fuerza de tendencia?")
indicador_sqzmom = st.checkbox("¿Indicador SQZMOM muestra expansión o contracción?")
if indicador_adx:
    puntuacion_total += 1
if indicador_sqzmom:
    puntuacion_total += 1

# Paso 6: Figuras de Reversión y Patrones
st.subheader("Paso 6: Figuras de Reversión y Patrones")
figura_tr = st.checkbox("¿Figura de Triángulo Reventado (TR) confirmada?")
figura_ld = st.checkbox("¿Figura de Leading Diagonal (LD) confirmada?")
if figura_tr or figura_ld:
    puntuacion_total += 2

# Paso 7: Entrada Estrategia Sniper
st.subheader("Paso 7: Entrada Estrategia Sniper")
estrategia_sniper = st.checkbox("¿Condiciones para entrada 'sniper' cumplidas?")
if estrategia_sniper:
    puntuacion_total += 3

# Mostrar el progreso de la puntuación
progreso = (puntuacion_total / puntuacion_maxima) * 100
st.progress(progreso)

# Sugerencia de acción basada en progresión
st.write(f"Progreso: {progreso:.2f}%")

if progreso >= 75:
    st.success("¡Alta probabilidad! Considera entrar en operación.")
elif 50 <= progreso < 75:
    st.warning("Condiciones favorables, pero monitorea el mercado.")
else:
    st.error("Condiciones no favorables. Espera más confirmaciones.")
