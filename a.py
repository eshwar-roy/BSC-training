# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import plotly.express as px
# import time

# # Configure the page and render the basic display elements below
# st.set_page_config(
#     page_title="Streamlit Features Demo",
#     page_icon="🚀",
#     layout="wide"
# )

# st.title("🚀 Streamlit 50 Features Demo")
# st.header("Basic Display Features")
# st.subheader("Learning Streamlit")

# st.write("st.write can display almost anything")
# st.text("This is simple text")
# st.markdown("**Bold Text**   *Italic Text*")

# st.success("Application Started Successfully")
# st.warning("This is a warning message")
# st.error("This is an error message")
# st.info("This is information")
# st.divider()
# st.header("Input Components")

# # Collect user input through Streamlit's widgets

# name = st.text_input("Enter Your Name")
# st.write("Hello:", name)

# age = st.number_input(
#     "Enter Age",
#     min_value=1,
#     max_value=100
# )

# salary = st.slider(
#     "Select Salary",
#     10000,
#     100000
# )

# course = st.selectbox(
#     "Choose Course",
#     ["Python", "Machine Learning", "Deep Learning"]
# )

# skills = st.multiselect(
#     "Select Skills",
#     ["Python", "SQL", "AI", "Docker"]
# )

# gender = st.radio(
#     "Select Gender",
#     ["Male", "Female"]
# )

# agree = st.checkbox("I Agree")

# if st.button("Click Me"):
#     st.write("Button Clicked")

# date = st.date_input("Select Date")

# time_input = st.time_input("Select Time")

# file = st.file_uploader("Upload CSV File")

# if file:
#     df = pd.read_csv(file)
#     st.write(df)

# color = st.color_picker("Choose Color")

# photo = st.camera_input("Take Picture")
# st.header("Layout Features")

# # Arrange the page using sidebar, columns, and containers

# st.sidebar.title("Sidebar Menu")

# option = st.sidebar.selectbox(
#     "Choose Option",
#     ["Home", "About"]
# )

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write("Column 1")

# with col2:
#     st.write("Column 2")

# with col3:
#     st.write("Column 3")

# with st.expander("Click to Expand"):
#     st.write("Hidden information")

# with st.container():
#     st.write("Inside Container")


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Professional Streamlit Demo", page_icon="🚀", layout="wide")

st.markdown("""
<style>
.main {background-color:#0E1117;}
.block-container {padding-top:2rem;}
.card{
background:#1E1E1E;
padding:20px;
border-radius:15px;
border:1px solid #333;
}
.footer{
text-align:center;
color:gray;
padding:20px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio(
    "Select Section",
    [
        "Home","Charts","DataFrames","Widgets","Forms",
        "Maps","Upload","Authentication","Media",
        "Progress","Chat"
    ]
)

st.title("🚀 Professional Streamlit Demo")
st.caption("Portfolio style application demonstrating core Streamlit components.")

c1,c2,c3 = st.columns(3)
c1.metric("Pages",10)
c2.metric("Framework","Streamlit")
c3.metric("Status","Running")


st.divider()

if page=="Home":
    st.header("Welcome")
    left,right=st.columns([2,1])
    with left:
        st.write("This application demonstrates professional Streamlit UI components.")
        st.success("Application Started Successfully")
        st.info("Everything is working correctly.")
        st.warning("Warning message example.")
        st.error("Error message example.")
        with st.expander("About"):
            st.write("Explore each section from the sidebar.")
    with right:
        st.code('print("Hello Streamlit")',language="python")
        st.json({"framework":"streamlit","language":"python","version":"demo"})

elif page=="Charts":
    st.header("Charts")
    df=pd.DataFrame(np.random.randn(40,3),columns=["Sales","Profit","Expenses"])
    t1,t2,t3=st.tabs(["Line","Bar","Area"])
    with t1:
        st.line_chart(df)
    with t2:
        st.bar_chart(df)
    with t3:
        st.area_chart(df)

    fig=px.scatter(
        x=np.random.randn(200),
        y=np.random.randn(200),
        title="Plotly Scatter Chart"
    )
    st.plotly_chart(fig,use_container_width=True)

    fig2,ax=plt.subplots()
    ax.plot(df["Sales"])
    ax.set_title("Matplotlib Example")
    st.pyplot(fig2)

elif page=="DataFrames":
    st.header("DataFrames")
    data=pd.DataFrame({
        "Name":["Alice","Bob","Charlie","David"],
        "Age":[23,30,28,35],
        "Salary":[40000,60000,70000,80000]
    })
    st.dataframe(data,use_container_width=True)
    st.subheader("Editable Table")
    st.data_editor(data,use_container_width=True)

elif page=="Widgets":
    st.header("Widgets")
    name=st.text_input("Name")
    age=st.slider("Age",18,60,25)
    gender=st.radio("Gender",["Male","Female","Other"])
    country=st.selectbox("Country",["India","USA","Germany","Canada"])
    skills=st.multiselect("Skills",
                          ["Python","SQL","AWS","Docker","AI","FastAPI"])
    if st.checkbox("Accept Terms"):
        st.success(f"Welcome {name}")
    st.write({
        "Name":name,
        "Age":age,
        "Gender":gender,
        "Country":country,
        "Skills":skills
    })

elif page=="Forms":
    st.header("Registration Form")
    with st.form("register"):
        uname=st.text_input("Username")
        email=st.text_input("Email")
        pwd=st.text_input("Password",type="password")
        submit=st.form_submit_button("Register")
    if submit:
        st.success(f"Registration completed for {uname}")

elif page=="Maps":
    st.header("Maps")
    map_df=pd.DataFrame(
        np.random.randn(500,2)/50+[37.76,-122.4],
        columns=["lat","lon"]
    )
    st.map(map_df)

elif page=="Upload":
    st.header("File Upload")
    file=st.file_uploader("Upload CSV",type="csv")
    if file:
        df=pd.read_csv(file)
        st.success("File uploaded successfully")
        st.dataframe(df,use_container_width=True)
        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            file_name="processed.csv",
            mime="text/csv"
        )

elif page=="Authentication":
    st.header("Login UI")
    with st.container(border=True):
        user=st.text_input("Username")
        pwd=st.text_input("Password",type="password")
        if st.button("Login"):
            if user=="admin" and pwd=="1234":
                st.success("Login Successful")
                st.balloons()
            else:
                st.error("Invalid username or password")

elif page=="Media":
    st.header("Media")
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",width=250)
    st.video("https://www.youtube.com/watch?v=VqgUkExPvLY")

elif page=="Progress":
    st.header("Progress & Spinner")
    if st.button("Start Task"):
        progress=st.progress(0)
        with st.spinner("Processing..."):
            for i in range(100):
                time.sleep(0.02)
                progress.progress(i+1)
        st.success("Task Completed")
        st.snow()

elif page=="Chat":
    st.header("Chat Demo")
    if "messages" not in st.session_state:
        st.session_state.messages=[]
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])
    prompt=st.chat_input("Type a message")
    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        with st.chat_message("user"):
            st.write(prompt)
        reply=f"You said: {prompt}"
        st.session_state.messages.append({"role":"assistant","content":reply})
        with st.chat_message("assistant"):
            st.write(reply)

st.divider()
# ==========================================================
# PROFESSIONAL INPUT COMPONENTS
# ==========================================================

st.divider()
st.header("Input Components")
st.caption("Explore various Streamlit input widgets.")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("👤 Personal Information")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=25
        )

        salary = st.slider(
            "Expected Salary (₹)",
            min_value=10000,
            max_value=100000,
            value=50000,
            step=1000,
            format="₹%d"
        )

        course = st.selectbox(
            "Select Course",
            [
                "Python",
                "Machine Learning",
                "Deep Learning",
                "Generative AI",
                "Data Science",
                "AWS"
            ]
        )

        gender = st.radio(
            "Gender",
            ["Male", "Female", "Other"],
            horizontal=True
        )

    with col2:

        st.subheader("💻 Skills & Preferences")

        skills = st.multiselect(
            "Technical Skills",
            [
                "Python",
                "SQL",
                "AI",
                "Machine Learning",
                "Deep Learning",
                "Docker",
                "FastAPI",
                "AWS",
                "Streamlit"
            ]
        )

        date = st.date_input("Joining Date")

        time_value = st.time_input("Preferred Interview Time")

        color = st.color_picker(
            "Choose Theme Color",
            "#4CAF50"
        )

        agree = st.toggle(
            "I agree to the Terms & Conditions"
        )

st.divider()

st.subheader("📂 Upload Section")

upload_col1, upload_col2 = st.columns(2)

with upload_col1:

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        dataframe = pd.read_csv(uploaded_file)

        st.success("CSV uploaded successfully!")

        st.dataframe(
            dataframe,
            use_container_width=True
        )

with upload_col2:

    picture = st.camera_input("Capture Profile Photo")

    if picture is not None:

        st.success("Photo captured successfully!")

        st.image(
            picture,
            caption="Captured Image",
            use_container_width=True
        )

st.divider()

st.subheader("🚀 Actions")

btn1, btn2, btn3 = st.columns(3)

with btn1:
    submit = st.button(
        "✅ Submit",
        use_container_width=True,
        type="primary"
    )

with btn2:
    reset = st.button(
        "🔄 Reset",
        use_container_width=True
    )

with btn3:
    preview = st.button(
        "👀 Preview",
        use_container_width=True
    )

if submit:

    if not agree:

        st.warning("Please accept the Terms & Conditions.")

    else:

        st.success("Information Submitted Successfully!")

        st.balloons()

        st.subheader("📋 Submitted Details")

        st.json({
            "Name": name,
            "Age": age,
            "Salary": salary,
            "Course": course,
            "Gender": gender,
            "Skills": skills,
            "Joining Date": str(date),
            "Interview Time": str(time_value),
            "Favorite Color": color
        })

if preview:

    st.info("Preview")

    preview_df = pd.DataFrame({
        "Field": [
            "Name",
            "Age",
            "Course",
            "Gender",
            "Salary"
        ],
        "Value": [
            name,
            age,
            course,
            gender,
            salary
        ]
    })

    st.table(preview_df)

if reset:

    st.warning("Refresh the page to clear all values.")
# ==========================================================
# PROFESSIONAL LAYOUT FEATURES
# ==========================================================

st.divider()
st.header("🏗️ Layout Components")
st.caption("Professional page layouts using sidebar, columns, containers, tabs and expanders.")

# ----------------------------------------------------------
# Sidebar Controls
# ----------------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.subheader("🏗️ Layout Demo")

layout_theme = st.sidebar.selectbox(
    "Dashboard Theme",
    ["Professional", "Minimal", "Modern"]
)

show_metrics = st.sidebar.toggle(
    "Show Statistics",
    value=True
)

# ----------------------------------------------------------
# Dashboard Metrics
# ----------------------------------------------------------

if show_metrics:

    metric1, metric2, metric3, metric4 = st.columns(4)

    metric1.metric(
        "Projects",
        "24",
        "+5"
    )

    metric2.metric(
        "Users",
        "1,280",
        "+18%"
    )

    metric3.metric(
        "Revenue",
        "₹2.5M",
        "+12%"
    )

    metric4.metric(
        "Satisfaction",
        "98%",
        "+2%"
    )

st.divider()

# ----------------------------------------------------------
# Professional Three Column Layout
# ----------------------------------------------------------

col1, col2, col3 = st.columns([1, 2, 1])

with col1:

    with st.container(border=True):

        st.subheader("📊 Analytics")

        st.metric("Visitors", "12,540")

        st.progress(75)

        st.caption("75% Monthly Goal Achieved")

with col2:

    with st.container(border=True):

        st.subheader("📈 Dashboard Overview")

        chart_df = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["Sales", "Profit", "Expenses"]
        )

        st.line_chart(chart_df)

with col3:

    with st.container(border=True):

        st.subheader("📌 Quick Actions")

        st.button(
            "➕ Create",
            use_container_width=True
        )

        st.button(
            "📥 Download",
            use_container_width=True
        )

        st.button(
            "⚙️ Settings",
            use_container_width=True
        )

st.divider()

# ----------------------------------------------------------
# Tabs
# ----------------------------------------------------------

st.subheader("📑 Tabs Layout")

tab1, tab2, tab3 = st.tabs(
    [
        "Overview",
        "Reports",
        "Settings"
    ]
)

with tab1:

    st.info("Overview Dashboard")

    st.write(
        "This tab displays summary information about your application."
    )

with tab2:

    report_df = pd.DataFrame({
        "Department": ["AI", "Cloud", "Web", "Data"],
        "Employees": [25, 18, 30, 20]
    })

    st.dataframe(
        report_df,
        use_container_width=True
    )

with tab3:

    st.success("Application Settings")

    st.checkbox("Enable Notifications")

    st.checkbox("Dark Mode")

st.divider()

# ----------------------------------------------------------
# Expanders
# ----------------------------------------------------------

st.subheader("📂 Expandable Sections")

with st.expander("📖 Project Information", expanded=False):

    st.write("""
This Streamlit application demonstrates professional layout techniques including:

- Responsive Columns
- Containers
- Tabs
- Sidebar Navigation
- Expanders
- Metrics
- Charts
- Professional Cards
""")

with st.expander("📊 Performance Summary"):

    performance = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ],
        "Value": [
            "96%",
            "94%",
            "95%",
            "95%"
        ]
    })

    st.table(performance)

st.divider()

# ----------------------------------------------------------
# Nested Containers
# ----------------------------------------------------------

st.subheader("📦 Nested Containers")

with st.container(border=True):

    left, right = st.columns(2)

    with left:

        st.success("Container A")

        st.write("Responsive left panel.")

    with right:

        st.info("Container B")

        st.write("Responsive right panel.")

st.divider()

# ----------------------------------------------------------
# Footer
# ----------------------------------------------------------

st.success("✅ Layout Components Demonstration Completed Successfully!")

st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>',unsafe_allow_html=True)