import streamlit as st
st.title("HELLO WORLD")
st.subheader("text")
st.write("你好 世界!")
age = st.sidebar.slider("How old are you?",0,100,18)
st.write(f"You are {age} now!")

if st.button("Hit me"):
    st.write("Hello")

name = st.text_input("Your name")
if name:
    st.write(f"Hello {name}")

st.markdown('''
# 一、海报名：《清廉筑梦，青春同行》

## 1. 画面主视觉


画面正中央是一位身穿校服/学士服的青年举起一本书（书名可以写“廉洁”二字），书本像一座桥梁/灯塔，照亮前方的道路。

* 天空明亮、阳光透过云层洒在青年身上，象征正义与希望。
* 书后方隐隐约约的校园建筑（可以画武汉理工大学的地标性建筑、教学楼等），突出校园特色和归属感。
* 书本两侧蔓延开来绿树枝叶，其间隐现中国结、“莲花”等廉洁元素。
* 马路两旁插着“青春正气”“廉洁自信”“追求卓越”等标语旗帜。

## 2. 细节与点缀

* 青年身边飞舞着几张象征“正直”“诚信”字样的纸鹤。
* 左下角画几个同学在讨论/合作，象征齐心协力、共同进步。
* 画面上方用艺术字体写上主题标语：“清廉筑梦，青春同行”。
''')
st.text("CSGUKCVAIL")
#文本展示
st.dataframe()
st.table()
st.checkbox("I Agree")
choices = st.radio("What's your favorite movie genre",
     [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        captions=[
         "Laugh out loud.",
         "Get the popcorn.",
        "Never stop learning.",
   ],)

st.write("choice:        ",choices)
st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
 )

st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.slider("How old are you?", 0, 130, 25)
st.text_input("Movie title", "Life of Brian")
st.text_area(
    "Text to analyze",
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    height=120
)
st.date_input(
    ""
)
st.time_input(
    ""
)
st.file_uploader("")
