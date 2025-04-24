import streamlit as st
import json
import os
from datetime import datetime

def main():
    st.title("File Classification App")
    
    st.write("Upload multiple files and classify them using the provided options.")
    
    # Create a file uploader that accepts multiple files of any type
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
    
    # Define the classification options
    options = [
        "Atención al cliente",
        "Calidad de productos",
        "Descripción de producto",
        "Facturación",
        "Proceso dificil",
        "Recogo en tienda",
        "Servicio de entrega",
        "Stock de productos",
        "Transparencia en compra en mini cuotas",
        "Variedad de productos",
        "Pagina lenta",
        "Error de la pagina",
        "Opciones de pago",
        "Precio Alto"
    ]
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
        
        # Sort files alphabetically by name
        sorted_files = sorted(uploaded_files, key=lambda x: x.name.lower())
        
        # Create a form for checkboxes
        with st.form("classification_form"):
            st.subheader("Select options for each file:")
            
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
            submit_button = st.form_submit_button("Generate JSON")
            
            if submit_button:
                # Create a timestamp for the filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                json_filename = f"classifications_{timestamp}.json"
                
                # Write the JSON file
                with open(json_filename, "w", encoding="utf-8") as json_file:
                    json.dump(selections, json_file, ensure_ascii=False, indent=4)
                
                # Provide download link
                with open(json_filename, "r", encoding="utf-8") as f:
                    json_content = f.read()
                
                st.download_button(
                    label="Download JSON file",
                    data=json_content,
                    file_name=json_filename,
                    mime="application/json"
                )
                
                st.success(f"JSON file '{json_filename}' created successfully!")
    else:
        st.info("No files uploaded yet. Please upload some files to classify.")

if __name__ == "__main__":
    main()