# importando as bibiliotecas
from sklearn.ensemble import BaggingClassifier
import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Carregando o modelo
model =  pickle.load(open('avaliacao_v3.pkl', 'rb'))


# Criando uma função para receber as features
def predict(GoodForKids,BikeParking, WiFi, bp_garage, bp_street):
    input=np.array([[GoodForKids,BikeParking, WiFi, bp_garage, bp_street]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0] [0], 2)
    return float(pred)
    



def main():
    
    # Add titulo, imagem e uma pequena descrição do nosso projeto
    from PIL import Image
    image =  Image.open("stars.png")
    st.image(image, use_column_width=False)
   

    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h1 style="color:white;text-align:center;">
       Qual Será A Avaliação Do Seu Estabelecimento?</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.sidebar.subheader('Por favor preencha as informações abaixo e clique no botão para saber qual será a sua avaliação!')
    st.sidebar.warning('Para preencher o Campo Wifi considere: 0=Não tem, 1=Wifi Pago, 2=Wifi Gratuito')
    st.sidebar.warning('Para preencher os demais campos: 0=Sim e 1=Não')
    
    
    # inserindo os dados para predição
    GoodForKids =  st.sidebar.selectbox("Tem Espaco para Crianças?", (0, 1))
    BikeParking =  st.sidebar.selectbox("Tem estacionamento para bicicletas?", (0, 1))
    bp_garage=  st.sidebar.selectbox("Tem estacionamento interno para carros?", (0, 1))
    bp_street=  st.sidebar.selectbox("Tem estacionamento na rua para carros?", (0, 1))
    WiFi = st.sidebar.selectbox("Tem Wifi", (0, 1, 2))
    
    
    
    #definindo o nível de cores para o tipo de avaliação
    boa_html="""  
      <div style="background-color:#38ff77;padding:40px >
       <h2 style="color:green;text-align:center;"> BOA</h2>
       </div>
    """
       
    ruim_html="""  
      <div style="background-color:#d61d40;padding:40px >
       <h2 style="color:red ;text-align:center;">  RUIM</h2>
       </div>
        """
 

     # criando botão para predição
    if st.sidebar.button("Clique para fazer a avaliação!"):
        output=predict(GoodForKids,BikeParking, WiFi, bp_garage, bp_street)
        st.success('De acordo com as informações fornecidas sua avaliação será:')
        
        if output > 0.6:
            st.markdown(ruim_html,unsafe_allow_html=True)
            st.info('Você precisa melhorar :(')
        else:
            st.markdown(boa_html,unsafe_allow_html=True)
            st.balloons()
        st.write('Probabilidade de ocorrência em:')
        st.write(output)
        
    

            

if __name__ == '__main__':
    main()           
