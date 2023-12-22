import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from modules.drawing_utils import  draw_plot_translation, draw_plot_origin



def update_plot():
    global plot
    plot=draw_plot_origin(
        transform=st.session_state.z_transformation,
        in_points=st.session_state.w_input,
        origin=st.session_state.origin,
        ymin=st.session_state.ymin,
        ymax=st.session_state.ymax,
        xmin=st.session_state.xmin,
        xmax=st.session_state.xmax,
        draw_polygon=True,
        circle=True
    )
    
# st.session_state  
st.write('Rotazione e omotetia del piano complesso: $z$ in forma polare $z\cdot w$')
z_form_container=st.sidebar.container()


poly_col1, poly_col2 = st.sidebar.columns([0.1,0.9])
with poly_col1:
    polygon_checkbox=st.checkbox('', value=True, key='triangle_checkboxes')
with poly_col2:
    triangle_expander=st.expander('Definisci  3 complessi $w_0,w_1,w_2$ ')
    triangle_form_container=triangle_expander.container()

fig_range_expander=st.sidebar.expander('Definisci i limiti del piano complesso')
fig_range_form_container=fig_range_expander.container()

origin_expander=st.sidebar.expander("Definisci origine della rotazione-omotetia")
origin_container=origin_expander.container()

with triangle_form_container.form("triangle_form"):


    w0_re=st.number_input('Parte reale $w_0$', value=-7, step=1, key='w1_real')
    w0_im=st.number_input('Parte immaginaria $w_0$', value=-2, step=1, key='w1_imag')
    w1_re=st.number_input('Parte reale $w_1$', value=-1, step=1, key='w2_real')
    w1_im=st.number_input('Parte immaginaria $w_1$', value=-5, step=1, key='w2_imag')
    w2_re=st.number_input('Parte reale $w_2$', value=-6, step=1, key='w3_real')
    w2_im=st.number_input('Parte immaginaria $w_2$', value=-8, step=1, key='w3_imag')
    triangle_submitted = st.form_submit_button("Submit")
    w_input=np.array([complex(w0_re,w0_im),complex(w1_re,w1_im),complex(w2_re,w2_im)])
    st.session_state.w_input=w_input
    if triangle_submitted:
        update_plot()
      
with fig_range_form_container.form("fig_range_form"):  

    xmin=st.number_input('xmin', value=-20, step=1, key='xmin')
    xmax=st.number_input('xmax', value=20, step=1, key='xmax')
    ymin=st.number_input('ymin', value=-20, step=1, key='ymin')
    ymax=st.number_input('ymax', value=20, step=1, key='ymax')
    fig_range_submitted = st.form_submit_button("Submit")
    
    if fig_range_submitted:
        update_plot()
 
with origin_container.form("origin_form"):
    # st.write("Definisci $O$, l'origine della rotazione-omotetia")


    O_re=st.number_input('Parte reale di $O$', value=0, step=1, key='O_real')
    O_im=st.number_input('Parte immaginaria di $O$', value=0, step=1, key='O_imag')
    origin=O_re+O_im*1j
    st.session_state.origin=origin
    origin_submitted = st.form_submit_button("Submit")
    
    if origin_submitted:
        update_plot()
        
# st.sidebar.write('Inserisci il complesso $z$ che definisce la trasformazione')
with z_form_container.form("my_form"):
    st.write('Inserisci il complesso $z$ che definisce la trasformazione')
    z_r=st.number_input(
            'Modulo', 
            value=3.00, 
            step=0.01, 
            key='z-r', 
            format='%f',
            min_value=-10.00,
            max_value=10.00)

    z_theta=st.number_input(
        'Angolo', 
        value=15.00, 
        step=1.0, 
        key='z-theta', 
        format='%f',
        min_value=-180.00,
        max_value=180.00
        )
    z_transformation=z_r*(np.cos(np.deg2rad(z_theta)))+z_r*(np.sin(np.deg2rad(z_theta))*1j)
    st.session_state.z_transformation=z_transformation
    z_submitted = st.form_submit_button("Submit")
    if z_submitted:
        update_plot()

st.latex(f'{z_r}'+r'''\angle'''+f'{z_theta}^\circ')
st.write(f'Forma algebrica: ${z_r*(np.cos(np.deg2rad(z_theta)))+z_r*(np.sin(np.deg2rad(z_theta))*1j):.2f}$')
st.write(f'Forma trigonometrica: ${z_r:.2f}\cdot (\cos({z_theta}^\circ)+i\cdot \sin({z_theta}^\circ))$')


if not(polygon_checkbox):
    w_input=[]
    
plot=draw_plot_origin(
    transform=z_transformation,
    in_points=w_input,
    origin=origin,
    ymin=ymin,
    ymax=ymax,
    xmin=xmin,
    xmax=xmax,
    draw_polygon=polygon_checkbox,
    circle=True
)
st.pyplot(plot)