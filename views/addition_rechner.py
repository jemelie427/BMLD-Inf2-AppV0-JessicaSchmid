import streamlit as st
from function.addition import add

st.title("Addition Rechner")

st.write(f"Das Ergebnis der Addition ist: {result}")

with st.form("Addition_form"):
   nummer_1= st.number_input("Nummer 1")
   nummer_2= st.number_input("Nummer 2")

   resultat= add(nummer_1, nummer_2)

   button= st.form_submit_button("Berechnen")
    if button:
         st.write(f"Das Ergebnis der Addition ist: {resultat}")
         
   