import streamlit as st
import numpy as np
from modules.drawing_utils import  draw_plot_translation, draw_plot_origin

cm = 1/2.54  # centimeters in inches

# st.sidebar.write('Inserisci il complesso $z$ che definisce la trasformazione')

# z_re=st.sidebar.number_input('Parte reale', value=3, step=1, key='z_real')
# z_im=st.sidebar.number_input('Parte immaginaria', value=2, step=1, key='z_imag')


def update_plot(draw_polygon=True):
    global translation_plot
    translation_plot=draw_plot_translation(
        transform=st.session_state.z_transformation,
        in_points=st.session_state.w_input,
        ymin=st.session_state.ymin,
        ymax=st.session_state.ymax,
        xmin=st.session_state.xmin,
        xmax=st.session_state.xmax,
        draw_polygon=draw_polygon,
        minrange=-10,
        maxrange=10,
        )

    
z_form_container=st.sidebar.container()


triangle_expander=st.sidebar.expander('Definisci  3 complessi $w_0,w_1,w_2$ ')
triangle_form_container=triangle_expander.container()

fig_range_expander=st.sidebar.expander('Definisci i limiti del piano complesso')
fig_range_form_container=fig_range_expander.container()

with triangle_form_container.form("triangle_form"):


    w0_re=st.number_input('Parte reale $w_0$', value=-7, step=1, key='w1_real')
    w0_im=st.number_input('Parte immaginaria $w_0$', value=-2, step=1, key='w1_imag')
    w1_re=st.number_input('Parte reale $w_1$', value=-1, step=1, key='w2_real')
    w1_im=st.number_input('Parte immaginaria $w_1$', value=-5, step=1, key='w2_imag')
    w2_re=st.number_input('Parte reale $w_2$', value=-6, step=1, key='w3_real')
    w2_im=st.number_input('Parte immaginaria $w_2$', value=-8, step=1, key='w3_imag')
    triangle_submitted = st.form_submit_button("Submit")
    w_input=np.array([complex(w0_re,w0_im),complex(w1_re,w1_im),complex(w2_re,w2_im)])
    if 'w_input' not in st.session_state:
        st.session_state.w_input=w_input
    if triangle_submitted:
        update_plot()
      
with fig_range_form_container.form("fig_range_form"):  
    st.write('Definisci il limiti del piano complesso')
    xmin=st.number_input('xmin', value=-20, step=1, key='xmin')
    xmax=st.number_input('xmax', value=20, step=1, key='xmax')
    ymin=st.number_input('ymin', value=-20, step=1, key='ymin')
    ymax=st.number_input('ymax', value=20, step=1, key='ymax')
    fig_range_submitted = st.form_submit_button("Submit")
    
    if fig_range_submitted:
        update_plot()
 





with z_form_container.form("my_form"):
    st.write('Traslazione del piano complesso: $z+w$')
    st.write('Inserisci il complesso $z$ che definisce la trasformazione')

    z_re=st.number_input('Parte reale', value=3, step=1, key='z_real')
    z_im=st.number_input('Parte immaginaria', value=2, step=1, key='z_imag')
    
    z_transformation=z_re+z_im*1j
     
    st.session_state.z_transformation=z_transformation
    
    
   # Every form must have a submit button.
    z_submitted = st.form_submit_button("Submit")
    if z_submitted:
        update_plot(draw_polygon=True)
        # draw_plot_translation(
        #     transform=z_transformation,
        #     in_points=w_input,
        #     ymin=ymin,
        #     ymax=ymax,
        #     xmin=xmin,
        #     xmax=xmax,
        #     draw_polygon=True,
        #     minrange=-10,
        #     maxrange=10,
        #     )
        
        
## Main page        
st.write(f'Traslazione del piano complesso: $z={z_transformation:.2f}$') 
# st.session_state


#ORIGINE
origin=0


translation_plot=draw_plot_translation(
transform=z_transformation,
in_points=w_input,
ymin=ymin,
ymax=ymax,
xmin=xmin,
xmax=xmax,
draw_polygon=True,
minrange=-10,
maxrange=10,
)



st.pyplot(translation_plot)