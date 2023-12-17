import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from modules.drawing_utils import  draw_plot_translation, draw_plot_origin




st.set_page_config(layout="wide")
st.title('Numeri complessi')
# st.sidebar.title('Menu')
# st.sidebar.header('Traslazione')

st.markdown('''
I numeri complessi come operazioni di trasformazione del piano complesso

Puoi utilizzare questa applicazione per testare traslazioni,rotazioni e omotetie del piano complesso.

## Somma

La somma di due complessi $z$ e $w$ può essere rappresentata come una traslazione del piano complesso. L'input $w$ viene traslato di $z$. In questo senso $z$ trasla il piano complesso.


## Moltiplicazione

La moltiplicazione tra due complessi $z$ e $w$ può essere rappresentata come una rotazione-omotetia del piano complesso. L'input $w$ viene ruotato e dilatato. In questo senso $z$ ruota e dilata (comprime) il piano complesso.
Rotazione e omotetia sono legate all'angolo che $z$ forma con l'asse reale e al suo modulo.
Questi valori sono evidenti se $z$ viene espresso in forma polare.

''')





# tab1, tab2 = st.tabs(["Traslazione", "Rotazione-omotetia"])


# with tab1:
    
#     col1,col2 =st.columns([0.1,0.9])
#     with col1:
#         st.sidebar.write('Inserisci il complesso $z$ che definisce la trasformazione')

#         z_re=st.sidebar.number_input('Parte reale', value=3, step=1, key='real')
#         z_im=st.sidebar.number_input('Parte immaginaria', value=2, step=1, key='imag')
        
#         st.sidebar.write('Definisci il limiti del piano complesso')
#         xmin=st.sidebar.number_input('xmin', value=-20, step=1, key='xmin')
#         xmax=st.sidebar.number_input('xmax', value=20, step=1, key='xmax')
#         ymin=st.sidebar.number_input('ymin', value=-20, step=1, key='ymin')
#         ymax=st.sidebar.number_input('ymax', value=20, step=1, key='ymax')
        
        
        

#         st.sidebar.write('Definisci i punti del triangolo da trasformare utilizzando la notazione $a+bj$')
    
#         w0_re=st.sidebar.number_input('Parte reale $w_0$', value=-7, step=1, key='w1_real')
#         w0_im=st.sidebar.number_input('Parte immaginaria $w_0$', value=-2, step=1, key='w1_imag')
#         w1_re=st.sidebar.number_input('Parte reale $w_1$', value=-1, step=1, key='w2_real')
#         w1_im=st.sidebar.number_input('Parte immaginaria $w_1$', value=-5, step=1, key='w2_imag')
#         w2_re=st.sidebar.number_input('Parte reale $w_2$', value=-6, step=1, key='w3_real')
#         w2_im=st.sidebar.number_input('Parte immaginaria $w_2$', value=-8, step=1, key='w3_imag')
        
        
        
#         # w_inputs=st.text_input('Aggiungi i complessi separati da virgola', value='-7+10j,-1+2j,-6+3j', key='poly')
#         # polygon=w_inputs.split(',')
#         # complex_polygon=[complex(z) for z in polygon]
      
        
        
    
#     with col2:
#         w_input=np.array([complex(w0_re,w0_im),complex(w1_re,w1_im),complex(w2_re,w2_im)])
#         z_transformation=z_re+z_im*1j
#         #z_transformation=np.exp(1j*np.pi)
#         #2*np.exp(1j*np.pi/3)

#         #LISTA INPUTS

#       #np.array([4+1j,1+2j,2-2j])
#         #w_input=2-3j #np.array([3+2j])

#         #ORIGINE
#         origin=0

       

#         translation_plot=draw_plot_translation(
#             transform=z_transformation,
#             in_points=w_input,
#             ymin=ymin,
#             ymax=ymax,
#             xmin=xmin,
#             xmax=xmax,
#             draw_polygon=True,
#             minrange=-10,
#             maxrange=10,
#             )
        
#         # operator_sym='+' if z_im>=0 else ''
        
#         # st.write(f'$z={z_re:.0f}{operator_sym}{z_im:.0f}i$')
#         # st.write(f'$z={w1_re:.0f}{operator_sym}{w1_im:.0f}i$')
#         st.pyplot(translation_plot)
    
# with tab2:
    # st.header("Rotazione-omotetia")

    # rot_col1,rot_col2 =st.columns([0.3,0.7])
    
    # with rot_col1:
    
    #     st.write("Definisci l'origine della rotazione-omotetia")
    #     # st.write('Definisci i punti del triangolo da trasformare utilizzando la notazione $a+bj$')
    
    #     O_re=st.number_input('Parte reale $O$', value=0, step=1, key='O_real')
    #     O_im=st.number_input('Parte immaginaria $O$', value=0, step=1, key='O_imag')
    
    
    # with rot_col2:
        
    #     z_transformation=z_re+z_im*1j
    #     origin=O_re+O_im*1j
    #     w_input=np.array([complex(w0_re,w0_im),complex(w1_re,w1_im),complex(w2_re,w2_im)])

 

    #     plot=draw_plot_origin(
    #         transform=z_transformation,
    #         in_points=w_input,
    #         origin=origin,
    #         ymin=ymin,
    #         ymax=ymax,
    #         xmin=xmin,
    #         xmax=xmax,
    #         draw_polygon=True
    #     )
    #     st.pyplot(plot)
