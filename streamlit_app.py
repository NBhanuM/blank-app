import streamlit as st

st.title("🎈 My new app")
def main():
    uploaded_file = st.file_uploader("Choose an excel file")
    if uploaded_file is not None:
        try:
            st.write(f"Uploaded file: {uploaded_file.name}, Type: {uploaded_file.type}")
            file_contents = uploaded_file.read()
            df = pd.read_excel(uploaded_file)
            
        except Exception as e:
            st.error(f"Error processing file: {e}")
    st.write('File not uploaded')

if __name__ == "__main__":
    main()
