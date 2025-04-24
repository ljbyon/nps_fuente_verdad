import streamlit as st

def main():
    st.title("File Upload Listing App")
    
    st.write("Upload multiple files to see their names listed below.")
    
    # Create a file uploader that accepts multiple files of any type
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
        
        st.subheader("Uploaded Files:")
        
        # Display the names of all uploaded files
        for i, file in enumerate(uploaded_files, 1):
            st.write(f"{i}. {file.name}")
    else:
        st.info("No files uploaded yet. Please upload some files to see their names.")

if __name__ == "__main__":
    main()