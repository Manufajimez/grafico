import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

def plot_chart(df, color, show_salaries):
    fig, ax = plt.subplots()

    
    df = df.sort_values(by='salary', ascending=False)

  
    bars = ax.barh(df['full name'], df['salary'], color=color)

    
    ax.set_xlim(0, 4500)

    if not show_employees:
        plt.yticks([])
        
    if show_salaries:
        ax.set_xlabel('Salary')
        for bar in bars:
            xval = bar.get_width()
            ax.text(xval, bar.get_y() + bar.get_height()/2, round(xval, 2), va='center', ha='left')
    else:
        ax.set_xlabel('')

    return fig

st.title("Empleatronix")
#selected_color = st.selectbox('Seleccionar color de la paleta:', sns.color_palette())
st.write('Todos los datos sobre los empleados en una aplicación.')

file_employees = "./data/employees.csv"
df = pd.read_csv(file_employees)
st.write(df)

columnas = st.columns(3)

colorpicker = columnas[0].color_picker("Seleccionar color", value='#1f77b4')
show_employees = columnas[1].toggle("Mostrar Empleados", value=True)
show_salaries = columnas[2].toggle("Mostrar Sueldos", value=True)



fig = plot_chart(df, colorpicker, show_salaries)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
