import streamlit as st
import pickle

# Page Configuration
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#FFE5EC,#FFD6E8,#F8E1FF);
}

/* Main Card */
.block-container{
background:#F6E8FF;
padding:35px;
border-radius:25px;
box-shadow:0px 10px 30px rgba(0,0,0,0.15);
}

/* Title */
.title{
background:linear-gradient(90deg,#8E2DE2,#DA22FF);
padding:18px;
border-radius:20px;
text-align:center;
font-size:40px;
font-weight:bold;
color:white;
margin-bottom:20px;
}

/* Student Details Heading */
h2,h3{
color:#6A0DAD;
font-weight:bold;
}

/* Labels */
label{
font-size:17px !important;
font-weight:bold !important;
color:#4B0082 !important;
}

/* Input Boxes */
.stNumberInput input{
background:#F3E5FF !important;
border:2px solid #C084FC !important;
border-radius:12px !important;
font-weight:bold;
color:#4B0082;
}

/* Dropdown */
.stSelectbox div{
background:#F3E5FF !important;
border-radius:12px;
font-weight:bold;
color:#4B0082;
}

/* Slider */
.stSlider{
color:#8E2DE2;
}

/* Button */
.stButton>button{
background:linear-gradient(90deg,#8E2DE2,#DA22FF);
color:white;
font-size:20px;
font-weight:bold;
border:none;
border-radius:12px;
height:55px;
width:100%;
}

.stButton>button:hover{
background:linear-gradient(90deg,#DA22FF,#8E2DE2);
transform:scale(1.03);
}

/* Student Details Box */
.details{
background:#EFE0FF;
padding:20px;
border-radius:15px;
border-left:8px solid #8E2DE2;
margin-top:20px;
}

/* Success Box */
.success-box{
background:#D8F5D0;
padding:18px;
border-radius:15px;
font-size:22px;
font-weight:bold;
color:#006400;
}

/* Error Box */
.error-box{
background:#FFDADA;
padding:18px;
border-radius:15px;
font-size:22px;
font-weight:bold;
color:#B00020;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='background: linear-gradient(90deg,#ff6ec7,#c471ed,#7f7fd5);
padding:20px;
border-radius:15px'>
<h1>🎓 Student Placement Prediction </h1>
</div>
""", unsafe_allow_html=True)

st.write("### Enter Student Details")

# Load Model
model = pickle.load(open("model.pkl","rb"))

# Inputs
cgpa = st.slider("CGPA",0.0,10.0,7.5)
internships = st.number_input("Internships",0,10,1)
projects = st.number_input("Projects",0,20,2)
workshops = st.number_input("Workshops",0,20,2)
aptitude = st.slider("Aptitude Score",0,100,70)
softskills = st.slider("Soft Skills Rating",1,5,3)

extra = st.selectbox("Extracurricular Activities",["No","Yes"])
training = st.selectbox("Placement Training",["No","Yes"])

ssc = st.slider("SSC Percentage",0,100,80)
hsc = st.slider("HSC Percentage",0,100,75)

extra = 1 if extra=="Yes" else 0
training = 1 if training=="Yes" else 0

# Prediction
if st.button("🔍 Predict Placement"):

    data=[[cgpa,internships,projects,workshops,
           aptitude,softskills,
           extra,training,ssc,hsc]]

    prediction=model.predict(data)

    st.subheader("📋 Student Details")

    st.write(f"**CGPA:** {cgpa}")
    st.write(f"**Internships:** {internships}")
    st.write(f"**Projects:** {projects}")
    st.write(f"**Workshops:** {workshops}")
    st.write(f"**Aptitude Score:** {aptitude}")
    st.write(f"**Soft Skills:** {softskills}")

    if hasattr(model,"predict_proba"):
        probability=model.predict_proba(data)[0][1]

        st.subheader("📊 Prediction Confidence")
        st.progress(int(probability*100))
        st.write(f"Confidence: **{probability*100:.2f}%**")

    if prediction[0]==1:
    
        st.success("🎉 Congratulations! Student is likely to be Placed.")
    else:
        st.error("❌ Student is likely to be Not Placed.")
        st.warning("Improve your CGPA, Aptitude Score and Placement Training.")

# Sidebar

st.sidebar.success("Developer: Diksha Patil")


st.sidebar.write("Machine Learning Project")

unsafe_allow_html=True
