import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from modules.drawing_utils import  draw_plot_translation, draw_plot_origin


st.write('Rotazione e omotetia del piano complesso: $z$ in forma polare')

st.sidebar.write('Inserisci il complesso $z$ che definisce la trasformazione')

z_r=st.sidebar.number_input(
        'Modulo', 
        value=3.00, 
        step=0.01, 
        key='z-r', 
        format='%f',
        min_value=-10.00,
        max_value=10.00)

z_theta=st.sidebar.number_input(
    'Angolo', 
    value=15.00, 
    step=1.0, 
    key='z-theta', 
    format='%f',
    min_value=-180.00,
    max_value=180.00
    )

st.latex(f'{z_r}'+r'''\angle'''+f'{z_theta}^\circ')
st.write(f'Forma algebrica: ${z_r*(np.cos(np.deg2rad(z_theta)))+z_r*(np.sin(np.deg2rad(z_theta))*1j):.2f}$')
st.write(f'Forma trigonometrica: ${z_r:.2f}\cdot (\cos({z_theta}^\circ)+i\cdot \sin({z_theta}^\circ))$')



# st.sidebar.write('Definisci i punti del triangolo da trasformare utilizzando la notazione $a+bj$')

st.sidebar.write('Definisci  3 complessi $w_0,w_1,w_2$  ')
w0_re=st.sidebar.number_input('Parte reale $w_0$', value=2, step=1, key='w1_real')
w0_im=st.sidebar.number_input('Parte immaginaria $w_0$', value=-3, step=1, key='w1_imag')
w1_re=st.sidebar.number_input('Parte reale $w_1$', value=5, step=1, key='w2_real')
w1_im=st.sidebar.number_input('Parte immaginaria $w_1$', value=-6, step=1, key='w2_imag')
w2_re=st.sidebar.number_input('Parte reale $w_2$', value=4, step=-4, key='w3_real')
w2_im=st.sidebar.number_input('Parte immaginaria $w_2$', value=-8, step=1, key='w3_imag')
        
st.sidebar.write('Definisci il limiti del piano complesso')
xmin=st.sidebar.number_input('xmin', value=-20, step=1, key='xmin')
xmax=st.sidebar.number_input('xmax', value=30, step=1, key='xmax')
ymin=st.sidebar.number_input('ymin', value=-20, step=1, key='ymin')
ymax=st.sidebar.number_input('ymax', value=20, step=1, key='ymax')


    
st.sidebar.write("Definisci $O$, l'origine della rotazione-omotetia")


O_re=st.sidebar.number_input('Parte reale di $O$', value=0, step=1, key='O_real')
O_im=st.sidebar.number_input('Parte immaginaria di $O$', value=0, step=1, key='O_imag')



    
z_transformation=z_r*(np.cos(np.deg2rad(z_theta)))+z_r*(np.sin(np.deg2rad(z_theta))*1j)

origin=O_re+O_im*1j
w_input=np.array([complex(w0_re,w0_im),complex(w1_re,w1_im),complex(w2_re,w2_im)])



plot=draw_plot_origin(
    transform=z_transformation,
    in_points=w_input,
    origin=origin,
    ymin=ymin,
    ymax=ymax,
    xmin=xmin,
    xmax=xmax,
    draw_polygon=True
)
st.pyplot(plot)