import streamlit as st
import json
import os
import base64
from datetime import datetime

def main():
    st.title("App para Clasificar Audio de NPS")
    
    st.write("Sube múltiples archivos y clasifícalos usando las opciones proporcionadas.")
    
    # Create a file uploader that accepts multiple files of any type
    uploaded_files = st.file_uploader("Selecciona archivos", accept_multiple_files=True)
    
    # Define the classification options and normalize them (remove accents)
    options = [
        "Atencion al cliente",
        "Calidad de productos",
        "Descripcion de producto",
        "Error de la pagina",
        "Facturacion",
        "Opciones de pago",
        "Pagina lenta",
        "Precio Alto",
        "Proceso dificil",
        "Recogo en tienda",
        "Servicio de entrega",
        "Stock de productos",
        "Transparencia en compra en mini cuotas",
        "Variedad de productos"
    ]
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} archivo(s) subido(s) con éxito!")
        
        # Sort files alphabetically by name
        sorted_files = sorted(uploaded_files, key=lambda x: x.name.lower())
        
        # Create a form for checkboxes
        with st.form("classification_form"):
            st.subheader("Selecciona opciones para cada archivo:")
            
            # Dictionary to store selections for each file
            selections = {}
            
            # Create checkboxes for each file
            for file in sorted_files:
                st.write(f"### {file.name}")
                file_selections = []
                
                # Create columns for checkboxes to save space
                cols = st.columns(3)
                for i, option in enumerate(options):
                    col_idx = i % 3
                    with cols[col_idx]:
                        if st.checkbox(option, key=f"{file.name}_{option}"):
                            file_selections.append(option)
                
                selections[file.name] = file_selections
                st.divider()
            
            # Submit button
            submit_button = st.form_submit_button("Generar JSON")
            
            if submit_button:
                # Create a timestamp for the filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                json_filename = f"classifications_{timestamp}.json"
                
                # Write the JSON file
                with open(json_filename, "w", encoding="utf-8") as json_file:
                    json.dump(selections, json_file, ensure_ascii=False, indent=4)
                
                # Show the path where the file was saved
                abs_path = os.path.abspath(json_filename)
                
                # Display JSON content in the app
                json_str = json.dumps(selections, ensure_ascii=False, indent=4)
                st.text_area("Contenido JSON", json_str, height=300)
                
                # Create a download link using HTML
                json_bytes = json_str.encode('utf-8')
                b64 = base64.b64encode(json_bytes).decode()
                href = f'<a href="data:file/txt;base64,{b64}" download="{json_filename}" target="_blank">Descargar archivo JSON</a>'
                st.markdown(href, unsafe_allow_html=True)
                
                st.success(f"¡Archivo JSON '{json_filename}' creado con éxito en {abs_path}!")
    else:
        st.info("No hay archivos subidos aún. Por favor, sube algunos archivos para clasificarlos.")

if __name__ == "__main__":
    main()