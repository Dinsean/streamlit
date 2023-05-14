import base64
import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image

        

st.set_page_config(page_title="My webpage", page_icon=":tada:")




st.sidebar.success("Select a page above.")

st.title("WELLCOME TO OUR PROJECT :wave:")
    


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image/image.jpg")

# # Thêm một liên kết đến tệp CSS
# st.markdown("""
#     <style>
#         %s
#     </style>
# """ % open("styles.css").read(), unsafe_allow_html=True)

# # Thêm một nút với một lớp tùy chỉnh
# st.button("Click me!", type="primary")


page_img_bg = """
    <style>
        [data-testid="stAppViewContainer"] {
            # background: url("https://cdn.wallpapersafari.com/15/56/rZJpjL.png");
            # background-size: cover;
            # background: linear-gradient(to left, #9fd07f, #8dd75e);

            background-color: #85FFBD;
            background-image: linear-gradient(45deg, #85FFBD 0%, #FFFB7D 50%, #ffffff 100%);

            
        }
        
        [data-testid="stHeader"] {
            background-color: rgba(0,0,0,0);
        }
        
        [data-testid="stVerticalBlock"] {
            
            
        }
        
        [data-testid="stToolbar"] {
            right: 2rem;
        }
        
        [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{img}");
        background-position: 50% 45%;
        background-size: 400%;
}}
        
    </style>
"""
st.markdown(page_img_bg, unsafe_allow_html=True)





   
   
   


     