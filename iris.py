import streamlit as st
import pandas as pd

iris = pd.read_csv("Iris.csv")
iris = iris.drop("Id", axis = 1)
iris = iris.rename(columns={"SepalLengthCm": "Sepal Length",
                            "SepalWidthCm": "Sepal Width",
                            "PetalLengthCm": "Petal Length",
                            "PetalWidthCm": "Petal Width"})
iris = iris.replace("Iris-", "", regex=True)
st.title("This is a test application for streamlit")
st.header("This application analyses the iris dataset")
if st.checkbox("Show data"):
    st.dataframe(iris)

st.subheader("Interactive Mode")
column = st.radio("Choose what you want to see:",
                  ("Sepal Length", "Sepal Width",
                   "Petal Length", "Petal Width"))
st.write("Choose which plants you want to see:")
setosa_show = st.checkbox("Setosa")
versicolor_show = st.checkbox("Versicolor")
virginica_show = st.checkbox("Virginica")

sepal_length = pd.DataFrame()

char_show = ""
if setosa_show:
    char_show = char_show + "Setosa"
    sepal_length["Setosa"] = iris[iris["Species"]=="setosa"][column]

if versicolor_show:
    if char_show == "":
        char_show = char_show + "Versicolor"
    else:
        char_show = char_show + ", " + "Versicolor"
    sepal_length["Versicolor"] = iris[iris["Species"] == "versicolor"][column].reset_index(drop=True)

if virginica_show:
    if char_show == "":
        char_show = char_show + "Virginica"
    else:
        char_show = char_show + ", " + "Virginica"
    sepal_length["Virginica"] = iris[iris["Species"]=="virginica"][column].reset_index(drop=True)

if char_show == "":
    st.write("Nothing will be displayed.")
else:
    st.write("The ", column, " of ", char_show, "will be displayed.")
    st.line_chart(sepal_length)

st.header("Up next are some streamlit tests")
p = st.number_input("Pick a number between 1 and 10", 1, 10, 5)
if p == 7:
    st.success("Congratulations!")
    st.balloons()
else:
    st.error("Wrong number. Better luck next time.")