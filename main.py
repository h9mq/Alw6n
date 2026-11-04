import streamlit as st
import pandas as pd
import time as t
from google import genai
from dotenv import load_dotenv
import os
import numpy as np
import json
import streamlit.components.v1 as components
import random
from datetime import datetime
import threading
import sys
import urllib.parse

st.set_page_config(
    page_title="Tuwaiq Students - عين الوطن",
    page_icon="icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

def two_sum():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            sum_two = (Input_Number_One + Input_Number_Two)
            st.success(f"Result {sum_two}")

def three_sum():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            sum_three = (Input_Number_One + Input_Number_Two + Input_Number_Three)
            st.success(f"Result {sum_three}")    

def four_sum():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            sum_four = (Input_Number_One + Input_Number_Two + Input_Number_Three + Input_Number_Four)
            st.success(f"Result {sum_four}") 

def two_minus():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            minus_two = (Input_Number_One - Input_Number_Two)
            st.success(f"Result {minus_two}")

def three_minus():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            minus_three = (Input_Number_One - Input_Number_Two - Input_Number_Three)
            st.success(f"Result {minus_three}")    

def four_minus():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            minus_four = (Input_Number_One - Input_Number_Two - Input_Number_Three - Input_Number_Four)
            st.success(f"Result {minus_four}")

def two_multi():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            multi_two = (Input_Number_One * Input_Number_Two)
            st.success(f"Result {multi_two}")

def three_multi():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            multi_three = (Input_Number_One * Input_Number_Two * Input_Number_Three)
            st.success(f"Result {multi_three}")    

def four_multi():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            multi_four = (Input_Number_One * Input_Number_Two * Input_Number_Three * Input_Number_Four)
            st.success(f"Result {multi_four}")

def two_dvide():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            dvide_two = (Input_Number_One / Input_Number_Two)
            st.success(f"Result {dvide_two}")

def three_dvide():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            dvide_three = (Input_Number_One / Input_Number_Two / Input_Number_Three)
            st.success(f"Result {dvide_three}")    

def four_dvide():
    Input_Number_One = st.number_input("Enter The First Number", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number", step=1)
    Input_Number_Three = st.number_input("Enter The Third Number", step=1)
    Input_Number_Four = st.number_input("Enter The Four Number", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            dvide_four = (Input_Number_One / Input_Number_Two / Input_Number_Three / Input_Number_Four)
            st.success(f"Result {dvide_four}")

def multi_number():
    Input_Number_One = st.number_input("Enter The First Number :", step=1)
    Input_Number_Two = st.number_input("Enter The Second Number :", step=1)
    if st.button("Compute"):
        with st.spinner("Computing..."):
            t.sleep(3)
            multi_number = (Input_Number_One ** Input_Number_Two)
            st.success(f"Result : {multi_number}")


# ==========================================
# بيانات ومكونات منصة عين الوطن المحدثة (RTL)
# ==========================================

_LEGACY_CITIES = {
    "الرياض": {"region": "منطقة الرياض", "lat": 24.7136, "lon": 46.6753, "temp": "32°C", "humidity": "18%", "wind": "16 كم/س", "weather": "صحو", "dust_level": "منخفض", "incident": "لا يوجد", "risk_score": 20},
    "جدة": {"region": "منطقة مكة المكرمة", "lat": 21.5433, "lon": 39.1728, "temp": "31°C", "humidity": "65%", "wind": "22 كم/س", "weather": "رطب", "dust_level": "متوسط", "incident": "ازدحام مروري - طريق الحرمين", "risk_score": 40},
    "مكة المكرمة": {"region": "منطقة مكة المكرمة", "lat": 21.3891, "lon": 39.8579, "temp": "35°C", "humidity": "30%", "wind": "14 كم/س", "weather": "مشمس", "dust_level": "منخفض", "incident": "لا يوجد", "risk_score": 15},
    "المدينة المنورة": {"region": "منطقة المدينة المنورة", "lat": 24.5247, "lon": 39.5692, "temp": "33°C", "humidity": "15%", "wind": "18 كم/س", "weather": "صحو", "dust_level": "منخفض", "incident": "لا يوجد", "risk_score": 20},
    "الدمام": {"region": "المنطقة الشرقية", "lat": 26.4207, "lon": 50.0888, "temp": "30°C", "humidity": "55%", "wind": "28 كم/س", "weather": "غبار خفيف", "dust_level": "عالي", "incident": "تنبيه رياح نشطة", "risk_score": 50},
    "الخبر": {"region": "المنطقة الشرقية", "lat": 26.2172, "lon": 50.1971, "temp": "29°C", "humidity": "60%", "wind": "25 كم/س", "weather": "غائم جزئياً", "dust_level": "متوسط", "incident": "لا يوجد", "risk_score": 30},
    "الظهران": {"region": "المنطقة الشرقية", "lat": 26.2361, "lon": 50.0393, "temp": "30°C", "humidity": "50%", "wind": "26 كم/س", "weather": "صحو", "dust_level": "متوسط", "incident": "لا يوجد", "risk_score": 25},
    "أبها": {"region": "منطقة عسير", "lat": 18.2164, "lon": 42.5053, "temp": "18°C", "humidity": "75%", "wind": "20 كم/س", "weather": "أمطار متوسطة", "dust_level": "منعدم", "incident": "تجمع مياه - عقبة ضلع", "risk_score": 60},
    "تبوك": {"region": "منطقة تبوك", "lat": 28.3835, "lon": 36.5662, "temp": "22°C", "humidity": "25%", "wind": "38 كم/س", "weather": "رياح شديدة", "dust_level": "عالي جداً", "incident": "عاصفة رملية", "risk_score": 65},
    "بريدة": {"region": "منطقة القصيم", "lat": 26.3260, "lon": 43.9750, "temp": "28°C", "humidity": "22%", "wind": "24 كم/س", "weather": "غائم جزئياً", "dust_level": "متوسط", "incident": "لا يوجد", "risk_score": 25},
    "حائل": {"region": "منطقة حائل", "lat": 27.5114, "lon": 41.7208, "temp": "25°C", "humidity": "28%", "wind": "21 كم/س", "weather": "سحب ممطرة", "dust_level": "منخفض", "incident": "جريان سيول خفيفة", "risk_score": 45},
    "نجران": {"region": "منطقة نجران", "lat": 17.4924, "lon": 44.1277, "temp": "29°C", "humidity": "20%", "wind": "30 كم/س", "weather": "غبار مثار", "dust_level": "عالي", "incident": "تدني الرؤية", "risk_score": 55},
    "جازان": {"region": "منطقة جازان", "lat": 16.8892, "lon": 42.5511, "temp": "32°C", "humidity": "72%", "wind": "25 كم/س", "weather": "أمطار غزيرة", "dust_level": "متوسط", "incident": "تحذير سيول في الأودية", "risk_score": 70},
    "الطائف": {"region": "منطقة مكة المكرمة", "lat": 21.2703, "lon": 40.4158, "temp": "23°C", "humidity": "45%", "wind": "19 كم/س", "weather": "غائم", "dust_level": "منخفض", "incident": "لا يوجد", "risk_score": 25},
    "الباحة": {"region": "منطقة الباحة", "lat": 20.0129, "lon": 41.4677, "temp": "20°C", "humidity": "70%", "wind": "15 كم/س", "weather": "ضباب وأمطار", "dust_level": "منعدم", "incident": "انزلاق مركبات", "risk_score": 50},
    "سكاكا": {"region": "منطقة الجوف", "lat": 29.9697, "lon": 40.2064, "temp": "24°C", "humidity": "20%", "wind": "32 كم/س", "weather": "رياح نشطة", "dust_level": "متوسط", "incident": "لا يوجد", "risk_score": 35},
    "عرعر": {"region": "منطقة الحدود الشمالية", "lat": 30.9753, "lon": 41.0381, "temp": "23°C", "humidity": "19%", "wind": "35 كم/س", "weather": "عاصفة ترابية", "dust_level": "عالي", "incident": "تنبيه على الطريق الدولي", "risk_score": 55},
    "ينبع": {"region": "منطقة المدينة المنورة", "lat": 24.0895, "lon": 38.0618, "temp": "30°C", "humidity": "58%", "wind": "24 كم/س", "weather": "صحو", "dust_level": "منخفض", "incident": "لا يوجد", "risk_score": 20},
    "حفر الباطن": {"region": "المنطقة الشرقية", "lat": 28.4328, "lon": 45.9708, "temp": "27°C", "humidity": "25%", "wind": "40 كم/س", "weather": "غبار كثيف", "dust_level": "عالي جداً", "incident": "حادث مروري بسبب الغبار", "risk_score": 75},
    "الأحساء": {"region": "المنطقة الشرقية", "lat": 25.3800, "lon": 49.5888, "temp": "33°C", "humidity": "35%", "wind": "22 كم/س", "weather": "صحو", "dust_level": "متوسط", "incident": "لا يوجد", "risk_score": 30},
}

# ==========================================
# قاعدة بيانات مدن المملكة (الـ 13 منطقة إدارية)
# ==========================================
# مستوى الزوم الذي تظهر عنده المباني ثلاثية الأبعاد (بيانات المباني تبدأ من زوم 13)
CITY_ZOOM = 14.0

# مدن رئيسية: تظهر دائماً بالاسم على خريطة المملكة، والبقية تظهر كدبابيس صغيرة وتتفصّل عند التقريب
_MAJOR_CITIES = {
    "الرياض", "جدة", "مكة المكرمة", "المدينة المنورة", "الدمام", "الأحساء", "أبها", "خميس مشيط",
    "تبوك", "بريدة", "حائل", "نجران", "جازان", "الباحة", "سكاكا", "عرعر", "ينبع",
    "حفر الباطن", "الجبيل", "الطائف",
}

_REGION_ORDER = [
    "منطقة الرياض", "منطقة مكة المكرمة", "منطقة المدينة المنورة", "منطقة القصيم",
    "المنطقة الشرقية", "منطقة عسير", "منطقة تبوك", "منطقة حائل", "منطقة الحدود الشمالية",
    "منطقة جازان", "منطقة نجران", "منطقة الباحة", "منطقة الجوف",
]

# (الاسم، المنطقة، خط العرض، خط الطول) - المدن الإضافية إلى جانب المدن الأساسية أعلاه
_EXTRA_CITIES = [
    # ---- منطقة الرياض ----
    ("الخرج", "منطقة الرياض", 24.1556, 47.3120),
    ("الدرعية", "منطقة الرياض", 24.7340, 46.5770),
    ("المجمعة", "منطقة الرياض", 25.9040, 45.3450),
    ("الزلفي", "منطقة الرياض", 26.2960, 44.8050),
    ("شقراء", "منطقة الرياض", 25.2470, 45.2520),
    ("عفيف", "منطقة الرياض", 23.9060, 42.9170),
    ("الدوادمي", "منطقة الرياض", 24.5070, 44.3920),
    ("وادي الدواسر", "منطقة الرياض", 20.4934, 44.7872),
    ("السليل", "منطقة الرياض", 20.4620, 45.5760),
    ("الأفلاج", "منطقة الرياض", 22.2900, 46.7300),
    ("حوطة بني تميم", "منطقة الرياض", 23.5190, 46.8350),
    ("الحريق", "منطقة الرياض", 23.6200, 46.5100),
    ("القويعية", "منطقة الرياض", 24.0700, 45.2800),
    ("ضرما", "منطقة الرياض", 24.6050, 46.1300),
    ("المزاحمية", "منطقة الرياض", 24.4790, 46.2660),
    ("رماح", "منطقة الرياض", 25.5600, 47.1400),
    ("حريملاء", "منطقة الرياض", 25.1220, 46.1190),
    ("ثادق", "منطقة الرياض", 25.2900, 45.8700),
    # ---- منطقة مكة المكرمة ----
    ("رابغ", "منطقة مكة المكرمة", 22.7980, 39.0340),
    ("الليث", "منطقة مكة المكرمة", 20.1500, 40.2700),
    ("القنفذة", "منطقة مكة المكرمة", 19.1270, 41.0790),
    ("خليص", "منطقة مكة المكرمة", 22.1450, 39.3150),
    ("الجموم", "منطقة مكة المكرمة", 21.6150, 39.6960),
    ("تربة", "منطقة مكة المكرمة", 21.2140, 41.6330),
    ("رنية", "منطقة مكة المكرمة", 21.2660, 42.8480),
    ("الخرمة", "منطقة مكة المكرمة", 21.9100, 42.0400),
    ("بحرة", "منطقة مكة المكرمة", 21.4000, 39.4300),
    ("المويه", "منطقة مكة المكرمة", 22.4300, 41.6200),
    # ---- منطقة المدينة المنورة ----
    ("العلا", "منطقة المدينة المنورة", 26.6085, 37.9232),
    ("بدر", "منطقة المدينة المنورة", 23.7800, 38.7900),
    ("خيبر", "منطقة المدينة المنورة", 25.6970, 39.2920),
    ("مهد الذهب", "منطقة المدينة المنورة", 23.4970, 40.8590),
    ("الحناكية", "منطقة المدينة المنورة", 24.8600, 40.5000),
    # ---- منطقة القصيم ----
    ("عنيزة", "منطقة القصيم", 26.0840, 43.9940),
    ("الرس", "منطقة القصيم", 25.8690, 43.4980),
    ("المذنب", "منطقة القصيم", 25.8630, 44.2220),
    ("البكيرية", "منطقة القصيم", 26.1400, 43.6570),
    ("البدائع", "منطقة القصيم", 25.9840, 43.7690),
    ("رياض الخبراء", "منطقة القصيم", 26.0200, 43.5400),
    ("عيون الجواء", "منطقة القصيم", 26.3440, 43.5890),
    # ---- المنطقة الشرقية ----
    ("الجبيل", "المنطقة الشرقية", 27.0046, 49.6460),
    ("القطيف", "المنطقة الشرقية", 26.5560, 50.0080),
    ("رأس تنورة", "المنطقة الشرقية", 26.6450, 50.1590),
    ("بقيق", "المنطقة الشرقية", 25.9330, 49.6700),
    ("النعيرية", "المنطقة الشرقية", 27.4700, 48.4900),
    ("الخفجي", "المنطقة الشرقية", 28.4390, 48.4910),
    ("قرية العليا", "المنطقة الشرقية", 27.5200, 47.7100),
    ("سيهات", "المنطقة الشرقية", 26.4830, 50.0400),
    ("صفوى", "المنطقة الشرقية", 26.6490, 49.9540),
    # ---- منطقة عسير ----
    ("خميس مشيط", "منطقة عسير", 18.3000, 42.7300),
    ("بيشة", "منطقة عسير", 20.0000, 42.6000),
    ("النماص", "منطقة عسير", 19.1200, 42.1300),
    ("محايل عسير", "منطقة عسير", 18.5400, 42.0500),
    ("سراة عبيدة", "منطقة عسير", 18.2000, 43.0000),
    ("رجال ألمع", "منطقة عسير", 18.2000, 42.2800),
    ("تثليث", "منطقة عسير", 19.5300, 43.5200),
    ("أحد رفيدة", "منطقة عسير", 18.2200, 42.8000),
    ("ظهران الجنوب", "منطقة عسير", 17.6700, 43.5000),
    ("بارق", "منطقة عسير", 18.9330, 41.9330),
    ("المجاردة", "منطقة عسير", 19.1200, 41.9100),
    # ---- منطقة تبوك ----
    ("الوجه", "منطقة تبوك", 26.2400, 36.4600),
    ("ضباء", "منطقة تبوك", 27.3500, 35.6900),
    ("تيماء", "منطقة تبوك", 27.6300, 38.5500),
    ("أملج", "منطقة تبوك", 25.0200, 37.2700),
    ("حقل", "منطقة تبوك", 29.2900, 34.9400),
    ("البدع", "منطقة تبوك", 28.4900, 35.0200),
    # ---- منطقة حائل ----
    ("بقعاء", "منطقة حائل", 27.9000, 42.4000),
    ("الشملي", "منطقة حائل", 26.6900, 42.6700),
    # ---- منطقة الحدود الشمالية ----
    ("رفحاء", "منطقة الحدود الشمالية", 29.6200, 43.5000),
    ("طريف", "منطقة الحدود الشمالية", 29.5000, 38.6600),
    # ---- منطقة الجوف ----
    ("دومة الجندل", "منطقة الجوف", 29.8100, 39.8700),
    ("القريات", "منطقة الجوف", 31.3300, 37.3400),
    ("طبرجل", "منطقة الجوف", 30.5000, 38.2200),
    # ---- منطقة جازان ----
    ("صبيا", "منطقة جازان", 17.1500, 42.6200),
    ("أبو عريش", "منطقة جازان", 16.9700, 42.8300),
    ("صامطة", "منطقة جازان", 16.5970, 42.9440),
    ("فرسان", "منطقة جازان", 16.7000, 42.1200),
    ("بيش", "منطقة جازان", 17.3700, 42.5500),
    ("الدرب", "منطقة جازان", 17.7200, 42.2500),
    ("ضمد", "منطقة جازان", 17.1000, 42.7700),
    ("أحد المسارحة", "منطقة جازان", 16.7000, 42.9500),
    # ---- منطقة نجران ----
    ("شرورة", "منطقة نجران", 17.4730, 47.1210),
    # ---- منطقة الباحة ----
    ("بلجرشي", "منطقة الباحة", 19.8500, 41.5700),
    ("المخواة", "منطقة الباحة", 19.7800, 41.4300),
]

# نطاقات المناخ لكل منطقة (لتوليد بيانات محاكاة واقعية نسبياً للمدن الإضافية)
_W_CENTRAL = {"clear": 40, "partly": 20, "windy": 15, "dust_light": 12, "dust_heavy": 6, "thunder": 7}
_W_NORTH = {"clear": 35, "partly": 20, "windy": 20, "dust_light": 12, "dust_heavy": 6, "thunder": 7}
_W_EAST = {"clear": 30, "partly": 20, "humid": 20, "dust_light": 15, "dust_heavy": 8, "windy": 7}
_W_WEST = {"clear": 35, "partly": 20, "humid": 20, "thunder": 10, "rain_light": 8, "dust_light": 7}
_W_SW = {"clear": 20, "partly": 20, "fog": 20, "rain_light": 20, "rain_heavy": 12, "thunder": 8}
_W_JAZAN = {"humid": 25, "partly": 20, "rain_light": 20, "rain_heavy": 15, "clear": 15, "thunder": 5}
_W_SOUTH = {"clear": 30, "partly": 20, "dust_light": 20, "windy": 15, "dust_heavy": 10, "thunder": 5}

_REGION_PROFILES = {
    "منطقة الرياض": {"temp": (24, 33), "hum": (14, 35), "wind": (14, 30), "weights": _W_CENTRAL},
    "منطقة القصيم": {"temp": (23, 32), "hum": (15, 35), "wind": (16, 30), "weights": _W_CENTRAL},
    "منطقة حائل": {"temp": (20, 30), "hum": (18, 35), "wind": (16, 30), "weights": _W_CENTRAL},
    "منطقة تبوك": {"temp": (17, 27), "hum": (20, 40), "wind": (20, 38), "weights": _W_NORTH},
    "منطقة الجوف": {"temp": (18, 27), "hum": (18, 35), "wind": (20, 36), "weights": _W_NORTH},
    "منطقة الحدود الشمالية": {"temp": (17, 26), "hum": (18, 35), "wind": (22, 38), "weights": _W_NORTH},
    "المنطقة الشرقية": {"temp": (27, 34), "hum": (40, 65), "wind": (18, 32), "weights": _W_EAST},
    "منطقة مكة المكرمة": {"temp": (27, 36), "hum": (25, 65), "wind": (14, 26), "weights": _W_WEST},
    "منطقة المدينة المنورة": {"temp": (26, 35), "hum": (15, 55), "wind": (15, 28), "weights": _W_WEST},
    "منطقة عسير": {"temp": (16, 27), "hum": (55, 80), "wind": (12, 22), "weights": _W_SW},
    "منطقة الباحة": {"temp": (16, 26), "hum": (55, 78), "wind": (12, 22), "weights": _W_SW},
    "منطقة جازان": {"temp": (29, 34), "hum": (60, 78), "wind": (18, 28), "weights": _W_JAZAN},
    "منطقة نجران": {"temp": (24, 32), "hum": (15, 30), "wind": (20, 32), "weights": _W_SOUTH},
}

# (الطقس، مستوى الغبار، البلاغ، مدى نسبة الخطر)
_SCENARIOS = {
    "clear": ("صحو", "منخفض", "لا يوجد", (10, 25)),
    "partly": ("غائم جزئياً", "منخفض", "لا يوجد", (18, 30)),
    "windy": ("رياح نشطة", "متوسط", "لا يوجد", (30, 42)),
    "humid": ("رطب", "متوسط", "لا يوجد", (25, 40)),
    "dust_light": ("غبار خفيف", "عالي", "تنبيه رياح نشطة", (40, 55)),
    "dust_heavy": ("غبار كثيف", "عالي جداً", "تدني الرؤية بسبب الغبار", (62, 78)),
    "thunder": ("سحب ممطرة", "منخفض", "جريان سيول خفيفة", (40, 55)),
    "rain_light": ("أمطار متوسطة", "منعدم", "تجمع مياه في بعض الطرق", (50, 65)),
    "rain_heavy": ("أمطار غزيرة", "متوسط", "تحذير سيول في الأودية", (66, 80)),
    "fog": ("ضباب وأمطار", "منعدم", "انخفاض الرؤية على الطرق الجبلية", (45, 58)),
}


def _generate_city_weather(name, region):
    rng = random.Random(f"ain-alwatan-{name}")  # ثابتة لكل مدينة بين كل تشغيل وآخر
    prof = _REGION_PROFILES[region]
    key = rng.choices(list(prof["weights"].keys()), weights=list(prof["weights"].values()))[0]
    weather, dust, incident, (r_lo, r_hi) = _SCENARIOS[key]
    wind = rng.randint(*prof["wind"]) + (10 if key == "dust_heavy" else 0)
    return {
        "temp": f"{rng.randint(*prof['temp'])}°C",
        "humidity": f"{rng.randint(*prof['hum'])}%",
        "wind": f"{wind} كم/س",
        "weather": weather,
        "dust_level": dust,
        "incident": incident,
        "risk_score": rng.randint(r_lo, r_hi),
    }


def _build_cities_data():
    data = {name: dict(info) for name, info in _LEGACY_CITIES.items()}
    for name, region, lat, lon in _EXTRA_CITIES:
        if name in data:
            continue
        info = {"region": region, "lat": lat, "lon": lon}
        info.update(_generate_city_weather(name, region))
        data[name] = info
    for name, info in data.items():
        info["tier"] = 1 if name in _MAJOR_CITIES else 2
    ordered = sorted(data.items(), key=lambda kv: (_REGION_ORDER.index(kv[1]["region"]), kv[0]))
    return dict(ordered)


CITIES_DATA = _build_cities_data()
REGIONS_COUNT = len({c["region"] for c in CITIES_DATA.values()})


ALERT_EVENTS = [
    "سيول جارفة وتحذير من الاقتراب من الأودية",
    "أمطار رعدية غزيرة مصحوبة برياح نشطة",
    "عاصفة غبارية شديدة وتدني مدى الرؤية الأفقية",
    "تجمع مياه غزيرة وإغلاق بعض الأنفاق",
    "رياح شديدة السرعة وارتفاع الأمواج"
]

# نظام المؤقت التلقائي (كل 3 دقائق = 180 ثانية) مع عرض العد التنازلي داخل الـ Terminal
@st.cache_resource
def init_auto_alert_system():
    state = {
        "target_time": t.time() + 180,
        "latest_alert": None,
        "alert_id": 0,
        "running": True
    }
    
    def terminal_timer_worker():
        print("\n" + "="*65, flush=True)
        print("🚀 [عين الوطن] تم تفعيل نظام الإنذار المبكر التلقائي (كل 3 دقائق)", flush=True)
        print("="*65, flush=True)
        while state["running"]:
            rem = int(state["target_time"] - t.time())
            if rem > 0:
                mins, secs = divmod(rem, 60)
                sys.stdout.write(f"\r⏳ [عين الوطن - Terminal Timer] المتبقي للإنذار التلقائي القادم: {mins:02d}:{secs:02d}   ")
                sys.stdout.flush()
                t.sleep(1)
            else:
                city = random.choice(list(CITIES_DATA.keys()))
                region = CITIES_DATA[city]["region"]
                event = random.choice(ALERT_EVENTS)
                now_str = datetime.now().strftime("%H:%M:%S")
                
                state["alert_id"] += 1
                state["latest_alert"] = {
                    "id": state["alert_id"],
                    "city": city,
                    "region": region,
                    "type": event,
                    "time": now_str
                }
                
                sys.stdout.write("\r" + " " * 75 + "\r")
                print(f"\n [إنذار تلقائي عاجل - {now_str}] تم رصد ({event}) في {city} ({region})!", flush=True)
                state["target_time"] = t.time() + 180

    thread = threading.Thread(target=terminal_timer_worker, daemon=True)
    thread.start()
    return state


# ==========================================
# الخريطة ثلاثية الأبعاد (MapLibre GL):
#  - تضاريس حقيقية + صور أقمار صناعية
#  - مباني OpenStreetMap مجسّمة تقف فوق التضاريس في كل مدن المملكة
#  - أسماء الشوارع والأحياء بالعربية بدون انعكاس
#  - تفاصيل الطقس عند تمرير الماوس على أي مدينة
# ==========================================
MAP_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://unpkg.com/maplibre-gl@5.24.0/dist/maplibre-gl.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/maplibre-gl@5.24.0/dist/maplibre-gl.js"></script>
<style>
  html, body { margin:0; padding:0; height:100%; width:100%; font-family:'Cairo', Tahoma, Arial, sans-serif; background:#0F172A; }
  #map { position:absolute; inset:0; border-radius:14px; }
  .maplibregl-popup-content { background:#0F172A; color:#fff; border-radius:12px; padding:12px 14px; border:1px solid #334155;
      box-shadow:0 8px 24px rgba(0,0,0,.45); direction:rtl; text-align:right; font-family:'Cairo', Tahoma, sans-serif; min-width:230px; }
  .maplibregl-popup-anchor-bottom .maplibregl-popup-tip { border-top-color:#0F172A; }
  .maplibregl-popup-anchor-top .maplibregl-popup-tip { border-bottom-color:#0F172A; }
  .maplibregl-popup-anchor-left .maplibregl-popup-tip { border-right-color:#0F172A; }
  .maplibregl-popup-anchor-right .maplibregl-popup-tip { border-left-color:#0F172A; }
  .pp-title { font-size:15px; font-weight:700; color:#FDE047; margin-bottom:6px; padding-bottom:6px; border-bottom:1px solid #334155; }
  .pp-row { font-size:13px; line-height:1.9; }
  .pp-row b { color:#CBD5E1; font-weight:600; }
  #ctl { position:absolute; top:10px; right:10px; display:flex; flex-direction:column; gap:6px; z-index:5; }
  #ctl button { font-family:inherit; font-size:13px; font-weight:600; padding:7px 12px; border-radius:8px; border:none; cursor:pointer;
      background:rgba(79,121,66,.95); color:#fff; box-shadow:0 2px 8px rgba(0,0,0,.3); }
  #ctl button:hover { background:#3D5E33; }
  #ctl button.off { background:rgba(71,85,105,.95); }
  #hud { position:absolute; left:50%; bottom:14px; transform:translateX(-50%); z-index:5; background:rgba(15,23,42,.88); color:#E2E8F0;
      padding:7px 16px; border-radius:20px; font-size:13px; border:1px solid #334155; transition:opacity .3s; pointer-events:none; }
  #legend { position:absolute; left:10px; bottom:34px; z-index:5; background:rgba(15,23,42,.88); color:#E2E8F0; padding:8px 12px;
      border-radius:10px; font-size:12px; border:1px solid #334155; line-height:1.9; }
  #legend i { display:inline-block; width:11px; height:11px; border-radius:50%; margin-left:6px; vertical-align:middle; border:1.5px solid #fff; }
</style>
</head>
<body>
<div id="map"></div>
<div id="ctl">
  <button id="b-terrain">⛰️ التضاريس: مفعّلة</button>
  <button id="b-build">🏙️ المباني: مفعّلة</button>
  <button id="b-reset">🌍 المملكة كاملة</button>
  <button id="b-full">⛶ تكبير الشاشة</button>
</div>
<div id="legend">
  <div><i style="background:#10B981"></i>خطر منخفض</div>
  <div><i style="background:#F59E0B"></i>خطر متوسط</div>
  <div><i style="background:#EF4444"></i>خطر مرتفع</div>
</div>
<div id="hud">🔎 قرّب على أي مدينة لإظهار المباني والشوارع والأحياء</div>

<script>
const GEO = __GEOJSON__;
const VIEW = __VIEW__;
const SELECTED = __SELECTED__;

// دعم الحروف العربية المتصلة واتجاه النص من اليمين لليسار داخل الخريطة
try {
  maplibregl.setRTLTextPlugin('https://unpkg.com/@mapbox/mapbox-gl-rtl-text@0.3.0/dist/mapbox-gl-rtl-text.js', true);
} catch (e) { console.log('RTL plugin:', e); }

const FONT_R = ['Noto Sans Regular'];
const FONT_B = ['Noto Sans Bold'];
const NAME = ['coalesce', ['get', 'name:ar'], ['get', 'name']];
const HEIGHT = ['max', ['coalesce', ['get', 'render_height'], 0], 8];
const HALO = 'rgba(15,23,42,0.95)';
const RISK_COLOR = ['step', ['get', 'risk_score'], '#10B981', 40, '#F59E0B', 70, '#EF4444'];

const style = {
  version: 8,
  glyphs: 'https://demotiles.maplibre.org/font/{fontstack}/{range}.pbf',
  sources: {
    sat: { type: 'raster', tileSize: 256, maxzoom: 19,
           tiles: ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],
           attribution: 'Imagery © Esri, Maxar, Earthstar Geographics' },
    dem: { type: 'raster-dem', tileSize: 256, maxzoom: 15, encoding: 'terrarium',
           tiles: ['https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'],
           attribution: 'Terrain: Mapzen / AWS' },
    omt: { type: 'vector', url: 'https://tiles.openfreemap.org/planet' },
    cities: { type: 'geojson', data: GEO }
  },
  layers: [
    { id: 'sat', type: 'raster', source: 'sat' },

    { id: 'roads', type: 'line', source: 'omt', 'source-layer': 'transportation', minzoom: 11,
      filter: ['all',
        ['in', ['get', 'class'], ['literal', ['motorway', 'trunk', 'primary', 'secondary', 'tertiary', 'minor', 'service']]],
        ['!=', ['get', 'brunnel'], 'tunnel']],
      layout: { 'line-cap': 'round', 'line-join': 'round' },
      paint: {
        'line-color': ['match', ['get', 'class'], ['motorway', 'trunk'], '#ffcf5c', 'primary', '#fff1a8', ['secondary', 'tertiary'], '#ffffff', '#e5e7eb'],
        'line-opacity': 0.55,
        'line-width': ['interpolate', ['linear'], ['zoom'], 11, 0.6, 14, 2, 17, 6]
      } },

    { id: 'buildings', type: 'fill-extrusion', source: 'omt', 'source-layer': 'building', minzoom: 13,
      filter: ['!=', ['get', 'hide_3d'], true],
      paint: {
        'fill-extrusion-color': ['interpolate', ['linear'], HEIGHT, 0, '#e9dfc8', 30, '#d8d0bd', 80, '#c0c9d8', 200, '#98abc6'],
        'fill-extrusion-height': ['interpolate', ['linear'], ['zoom'], 13, 0, 14.2, HEIGHT],
        'fill-extrusion-base': ['interpolate', ['linear'], ['zoom'], 15.9, 0, 16, ['coalesce', ['get', 'render_min_height'], 0]],
        'fill-extrusion-opacity': 0.94
      } },

    { id: 'water-names', type: 'symbol', source: 'omt', 'source-layer': 'water_name', minzoom: 7,
      layout: { 'text-field': NAME, 'text-font': FONT_R, 'text-size': 12, 'text-letter-spacing': 0 },
      paint: { 'text-color': '#bae6fd', 'text-halo-color': HALO, 'text-halo-width': 1.6 } },

    { id: 'place-hoods', type: 'symbol', source: 'omt', 'source-layer': 'place', minzoom: 11.5,
      filter: ['in', ['get', 'class'], ['literal', ['suburb', 'neighbourhood', 'quarter', 'hamlet', 'village', 'isolated_dwelling']]],
      layout: { 'text-field': NAME, 'text-font': FONT_B, 'text-letter-spacing': 0, 'text-max-width': 8,
                'text-size': ['interpolate', ['linear'], ['zoom'], 11, 11, 15, 16] },
      paint: { 'text-color': '#FDE047', 'text-halo-color': HALO, 'text-halo-width': 1.9 } },

    { id: 'road-names', type: 'symbol', source: 'omt', 'source-layer': 'transportation_name', minzoom: 13,
      layout: { 'symbol-placement': 'line', 'symbol-spacing': 260, 'text-field': NAME, 'text-font': FONT_R,
                'text-letter-spacing': 0, 'text-max-angle': 35, 'text-keep-upright': true,
                'text-size': ['interpolate', ['linear'], ['zoom'], 13, 10, 17, 14] },
      paint: { 'text-color': '#ffffff', 'text-halo-color': HALO, 'text-halo-width': 1.7 } },

    { id: 'poi-names', type: 'symbol', source: 'omt', 'source-layer': 'poi', minzoom: 15.5,
      filter: ['in', ['get', 'class'], ['literal', ['hospital', 'school', 'college', 'place_of_worship', 'park', 'stadium', 'police', 'fire_station', 'bank', 'fuel', 'post']]],
      layout: { 'text-field': NAME, 'text-font': FONT_R, 'text-size': 11, 'text-letter-spacing': 0, 'text-max-width': 7 },
      paint: { 'text-color': '#bfdbfe', 'text-halo-color': HALO, 'text-halo-width': 1.5 } },

    { id: 'danger-zone', type: 'circle', source: 'cities', filter: ['>=', ['get', 'risk_score'], 70],
      paint: { 'circle-radius': ['interpolate', ['linear'], ['zoom'], 4, 16, 8, 34, 12, 70, 16, 120],
               'circle-color': 'rgba(239,68,68,0.22)', 'circle-stroke-color': 'rgba(239,68,68,0.95)', 'circle-stroke-width': 2 } },

    { id: 'city-hit', type: 'circle', source: 'cities',
      paint: { 'circle-radius': 17, 'circle-color': '#ffffff', 'circle-opacity': 0.01 } },

    { id: 'city-selected', type: 'circle', source: 'cities', filter: ['==', ['get', 'city'], SELECTED],
      paint: { 'circle-radius': ['interpolate', ['linear'], ['zoom'], 4, 11, 12, 16], 'circle-color': 'rgba(253,224,71,0.25)',
               'circle-stroke-color': '#FDE047', 'circle-stroke-width': 2.5 } },

    { id: 'city-dot', type: 'circle', source: 'cities',
      paint: { 'circle-radius': ['interpolate', ['linear'], ['zoom'], 4, 4.5, 8, 7, 14, 9],
               'circle-color': RISK_COLOR, 'circle-stroke-color': '#ffffff', 'circle-stroke-width': 2 } },

    { id: 'city-label-major', type: 'symbol', source: 'cities', filter: ['==', ['get', 'tier'], 1],
      layout: {
        'text-field': ['step', ['zoom'],
          ['format', ['get', 'city'], {}],
          8, ['format', ['get', 'city'], {}, '\n', {}, ['get', 'region'], { 'font-scale': 0.78, 'text-color': '#FDE047' }]],
        'text-font': FONT_B, 'text-letter-spacing': 0, 'text-anchor': 'top', 'text-offset': [0, 0.9],
        'text-size': ['interpolate', ['linear'], ['zoom'], 4, 12, 10, 15], 'text-padding': 3 },
      paint: { 'text-color': '#ffffff', 'text-halo-color': HALO, 'text-halo-width': 2.2 } },

    { id: 'city-label-minor', type: 'symbol', source: 'cities', filter: ['==', ['get', 'tier'], 2], minzoom: 6.2,
      layout: {
        'text-field': ['step', ['zoom'],
          ['format', ['get', 'city'], {}],
          8.5, ['format', ['get', 'city'], {}, '\n', {}, ['get', 'region'], { 'font-scale': 0.78, 'text-color': '#FDE047' }]],
        'text-font': FONT_B, 'text-letter-spacing': 0, 'text-anchor': 'top', 'text-offset': [0, 0.9],
        'text-size': ['interpolate', ['linear'], ['zoom'], 6, 11, 12, 14], 'text-padding': 3 },
      paint: { 'text-color': '#ffffff', 'text-halo-color': HALO, 'text-halo-width': 2 } }
  ]
};

const map = new maplibregl.Map({
  container: 'map',
  style: style,
  center: [VIEW.lon, VIEW.lat],
  zoom: VIEW.zoom,
  pitch: VIEW.pitch,
  bearing: VIEW.bearing,
  maxPitch: 85,
  minZoom: 4,
  maxZoom: 19,
  canvasContextAttributes: { antialias: true }
});

map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }), 'top-left');
map.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-right');

const hud = document.getElementById('hud');
let terrainOn = true;
let buildingsOn = true;
const TERRAIN_EXAGGERATION = 1.5;

map.on('load', () => {
  map.setTerrain({ source: 'dem', exaggeration: TERRAIN_EXAGGERATION });
});

map.on('error', (e) => {
  const msg = e && e.error ? e.error.message : String(e);
  console.log('map error:', msg);
  // إظهار أخطاء الستايل فقط (أخطاء تحميل بلاطة واحدة لا تهم)
  if (/layer|style|expression|source/i.test(msg) && !/tile|404|Failed to fetch|NetworkError/i.test(msg)) {
    hud.style.opacity = 1; hud.style.color = '#FCA5A5'; hud.textContent = '⚠️ ' + msg.slice(0, 160);
  }
});

function esc(v) {
  return String(v).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function popupHTML(p) {
  const rc = p.risk_score >= 70 ? '#EF4444' : (p.risk_score >= 40 ? '#F59E0B' : '#10B981');
  return `<div dir="rtl">
    <div class="pp-title">📍 ${esc(p.city)} - ${esc(p.region)}</div>
    <div class="pp-row"><b>🌤️ الطقس:</b> ${esc(p.weather)}</div>
    <div class="pp-row"><b>🌡️ الحرارة:</b> ${esc(p.temp)} &nbsp;|&nbsp; <b>💧 الرطوبة:</b> ${esc(p.humidity)}</div>
    <div class="pp-row"><b>💨 الرياح:</b> ${esc(p.wind)} &nbsp;|&nbsp; <b>🌫️ الغبار:</b> ${esc(p.dust_level)}</div>
    <div class="pp-row"><b>🚨 البلاغات:</b> ${esc(p.incident)}</div>
    <div class="pp-row"><b>⚠️ نسبة الخطر:</b> <span style="color:${rc};font-weight:700">${esc(p.risk_score)}%</span></div>
  </div>`;
}

// تفاصيل الطقس عند تمرير الماوس على المدينة
const popup = new maplibregl.Popup({ closeButton: false, closeOnClick: false, offset: 16, maxWidth: '340px' });
const HIT_LAYERS = ['city-hit', 'city-label-major', 'city-label-minor'];
let currentCity = null;

function cityAt(point) {
  try {
    const fs = map.queryRenderedFeatures(point, { layers: HIT_LAYERS });
    return fs.length ? fs[0] : null;
  } catch (e) { return null; }
}

map.on('mousemove', (e) => {
  const f = cityAt(e.point);
  if (f) {
    map.getCanvas().style.cursor = 'pointer';
    if (currentCity !== f.properties.city) {
      currentCity = f.properties.city;
      popup.setLngLat(f.geometry.coordinates.slice()).setHTML(popupHTML(f.properties)).addTo(map);
    }
  } else {
    map.getCanvas().style.cursor = '';
    currentCity = null;
    popup.remove();
  }
});

// النقر على المدينة: تقريب مائل ثلاثي الأبعاد
map.on('click', (e) => {
  const f = cityAt(e.point);
  if (f) {
    map.flyTo({ center: f.geometry.coordinates.slice(), zoom: Math.max(map.getZoom(), 14.2), pitch: 62, bearing: -15, speed: 0.9, essential: true });
  }
});

// إظهار تلميح عند الابتعاد (المباني تبدأ من زوم 13)
function updateHud() { hud.style.opacity = map.getZoom() < 13 ? 1 : 0; }
map.on('zoom', updateHud);
map.on('load', updateHud);

document.getElementById('b-terrain').addEventListener('click', (ev) => {
  terrainOn = !terrainOn;
  map.setTerrain(terrainOn ? { source: 'dem', exaggeration: TERRAIN_EXAGGERATION } : null);
  ev.target.textContent = terrainOn ? '⛰️ التضاريس: مفعّلة' : '⛰️ التضاريس: مغلقة';
  ev.target.classList.toggle('off', !terrainOn);
});

document.getElementById('b-build').addEventListener('click', (ev) => {
  buildingsOn = !buildingsOn;
  map.setLayoutProperty('buildings', 'visibility', buildingsOn ? 'visible' : 'none');
  ev.target.textContent = buildingsOn ? '🏙️ المباني: مفعّلة' : '🏙️ المباني: مغلقة';
  ev.target.classList.toggle('off', !buildingsOn);
});

// تكبير الخريطة على كامل الشاشة (و Esc للخروج)
const fullBtn = document.getElementById('b-full');
function isFull() { return !!(document.fullscreenElement || document.webkitFullscreenElement); }
fullBtn.addEventListener('click', () => {
  const el = document.documentElement;
  try {
    if (isFull()) {
      (document.exitFullscreen || document.webkitExitFullscreen).call(document);
    } else {
      const req = el.requestFullscreen || el.webkitRequestFullscreen;
      if (!req) { throw new Error('unsupported'); }
      const r = req.call(el);
      if (r && r.catch) { r.catch(() => { hud.style.opacity = 1; hud.style.color = '#FCA5A5'; hud.textContent = '⚠️ المتصفح منع وضع ملء الشاشة'; }); }
    }
  } catch (err) {
    hud.style.opacity = 1; hud.style.color = '#FCA5A5'; hud.textContent = '⚠️ المتصفح منع وضع ملء الشاشة';
  }
});
function onFullChange() {
  fullBtn.textContent = isFull() ? '🗗 إغلاق ملء الشاشة' : '⛶ تكبير الشاشة';
  setTimeout(() => map.resize(), 150);
}
document.addEventListener('fullscreenchange', onFullChange);
document.addEventListener('webkitfullscreenchange', onFullChange);

document.getElementById('b-reset').addEventListener('click', () => {
  map.flyTo({ center: [45.0, 24.0], zoom: 5.3, pitch: 45, bearing: 0, essential: true });
});
</script>
</body>
</html>
"""


def _js_json(obj):
    return json.dumps(obj, ensure_ascii=False, default=lambda o: o.item() if hasattr(o, "item") else str(o)).replace("</", "<\\/")


def render_3d_map(df_map, view, selected_city, height=650):
    features = []
    for rec in df_map.to_dict("records"):
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [float(rec["lon"]), float(rec["lat"])]},
            "properties": {
                "city": rec["city"],
                "region": rec["region"],
                "temp": rec["temp"],
                "humidity": rec["humidity"],
                "wind": rec["wind"],
                "weather": rec["weather"],
                "dust_level": rec["dust_level"],
                "incident": rec["incident"],
                "risk_score": int(rec["risk_score"]),
                "tier": int(rec["tier"]),
            },
        })
    geojson = {"type": "FeatureCollection", "features": features}
    html = (MAP_HTML_TEMPLATE
            .replace("__GEOJSON__", _js_json(geojson))
            .replace("__VIEW__", _js_json(view))
            .replace("__SELECTED__", _js_json(selected_city)))
    components.html(html, height=height)


def alw6n(sim_event):
    alert_system = init_auto_alert_system()

    # مراقبة الإنذارات التلقائية كل ثانية لتحديث المنصة وإرسال الإشعارات تلقائياً
    @st.fragment(run_every="1s")
    def auto_alert_watcher():
        latest = alert_system["latest_alert"]
        if latest and latest["id"] != st.session_state.get("last_seen_alert_id", 0):
            st.session_state.last_seen_alert_id = latest["id"]
            st.session_state.simulation_active = True
            st.session_state.simulated_city = latest["city"]
            st.session_state.auto_sim_event = latest["type"]
            st.session_state.selected_city_name = latest["city"]
            st.session_state.map_lat = CITIES_DATA[latest["city"]]["lat"]
            st.session_state.map_lon = CITIES_DATA[latest["city"]]["lon"]
            st.session_state.map_zoom = CITY_ZOOM
            
            st.session_state.user_reports.insert(0, {
                "city": latest["city"],
                "type": latest["type"],
                "desc": f"إنذار آلي مبكر ({latest['time']}) - {latest['region']}"
            })
            st.toast(f" إنذار تلقائي عاجل: {latest['type']} في {latest['city']} ({latest['region']})", icon="⚠️")
            st.rerun()

    auto_alert_watcher()

    active_event = st.session_state.get("auto_sim_event", sim_event)

    # ==========================================
    # الواجهة الرئيسية (Hero Section) المطابقة للصورة وبملء الشاشة
    # ==========================================
    st.markdown("""
        <style>
        .hero-full-screen {
            position: relative;
            width: 100%;
            min-height: 88vh;
            background: 
                linear-gradient(to left, rgba(16, 53, 36, 0.94) 0%, rgba(22, 68, 45, 0.85) 50%, rgba(29, 82, 55, 0.72) 100%),
                url('https://images.unsplash.com/photo-1586724237569-f3d0c1dee8c6?q=80&w=2000&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            padding: 60px 8%;
            margin-bottom: 40px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            direction: rtl !important;
            text-align: right !important;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.12);
        }

        .hero-content-box {
            max-width: 720px;
            z-index: 2;
            direction: rtl !important;
            text-align: right !important;
        }

        .hero-badge-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #E2E8F0 !important;
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 22px;
        }

        .hero-main-title {
            color: #FDE047 !important;
            -webkit-text-fill-color: #FDE047 !important;
            font-size: 62px !important;
            font-weight: 800 !important;
            line-height: 1.2 !important;
            margin: 0 0 16px 0 !important;
            text-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }

        .hero-sub-title {
            color: #F8FAFC !important;
            font-size: 24px !important;
            font-weight: 700 !important;
            margin: 0 0 22px 0 !important;
        }

        .hero-desc-text {
            color: #E2E8F0 !important;
            font-size: 17px !important;
            line-height: 1.9 !important;
            margin-bottom: 24px !important;
            font-weight: 400;
        }

        .hero-org-note {
            color: #CBD5E1 !important;
            font-size: 14px !important;
            margin-bottom: 34px !important;
            opacity: 0.9;
        }

        .hero-actions {
            display: flex;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
        }

        .hero-btn-white {
            background-color: #FFFFFF !important;
            color: #143D29 !important;
            padding: 13px 32px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 16px;
            text-decoration: none !important;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.25s ease;
        }

        .hero-btn-white:hover {
            background-color: #F1F5F9 !important;
            transform: translateY(-2px);
        }

        .hero-btn-glass {
            background-color: rgba(255, 255, 255, 0.14) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255, 255, 255, 0.35);
            padding: 13px 32px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 16px;
            text-decoration: none !important;
            display: inline-flex;
            align-items: center;
            transition: all 0.25s ease;
        }

        .hero-btn-glass:hover {
            background-color: rgba(255, 255, 255, 0.24) !important;
            transform: translateY(-2px);
        }

        /* ===== إصلاح ألوان نصوص الواجهة الرئيسية (أعلى أولوية من قواعد .stApp العامة) ===== */
        .stApp .hero-full-screen h1.hero-main-title,
        .stApp .hero-full-screen .hero-main-title,
        .stApp .stMarkdown .hero-full-screen h1.hero-main-title,
        .hero-full-screen h1.hero-main-title {
            color: #FDE047 !important;
            -webkit-text-fill-color: #FDE047 !important;
        }
        .stApp .hero-full-screen .hero-sub-title {
            color: #F8FAFC !important;
            -webkit-text-fill-color: #F8FAFC !important;
        }
        .stApp .hero-full-screen .hero-desc-text,
        .stApp .hero-full-screen .hero-desc-text b {
            color: #E2E8F0 !important;
            -webkit-text-fill-color: #E2E8F0 !important;
        }
        .stApp .hero-full-screen .hero-org-note {
            color: #CBD5E1 !important;
            -webkit-text-fill-color: #CBD5E1 !important;
        }
        .stApp .hero-full-screen .hero-badge-pill {
            color: #E2E8F0 !important;
            -webkit-text-fill-color: #E2E8F0 !important;
        }
        .stApp .hero-full-screen a.hero-btn-white {
            color: #143D29 !important;
            -webkit-text-fill-color: #143D29 !important;
        }
        .stApp .hero-full-screen a.hero-btn-glass {
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }
        </style>

        <div class="hero-full-screen">
            <div class="hero-content-box">
                <div class="hero-badge-pill">
                     محاكاة واقعية لمركز الأرصاد في المملكة العربية السعودية✨
                </div>
                <h1 class="hero-main-title">منصة عين الوطن</h1>
                <div class="hero-sub-title">عيونٌ ساهرة تحرس سماء المملكة.. وترصد المتغيرات لحظة بلحظة</div>
                <p class="hero-desc-text">
                    منصة تقنية تفاعلية متكاملة تُعد <b>محاكاة لأعمال الأرصاد في المملكة العربية السعودية</b>، حيث تعمل على متابعة حالة الطقس والظواهر الجوية في كافة مناطق ومدن المملكة، وإطلاق الإنذارات المبكرة للسيول والعواصف الغبارية، وتوجيه فرق الطوارئ الميدانية عبر خرائط الأقمار الصناعية الحية لتعزيز السلامة العامة وحماية الأرواح والممتلكات.
                </p>
                <div class="hero-org-note">
                </div>
                <div class="hero-actions">
                    <a href="#main-dashboard" class="hero-btn-white">استعراض الخريطة الحية &larr;</a>
                    <a href="#reports-section" class="hero-btn-glass">مركز البلاغات والإنذار</a>
                </div>
            </div>
        </div>
        <div id="main-dashboard"></div>
    """, unsafe_allow_html=True)

    if alert_system["latest_alert"] and st.session_state.simulation_active:
        la = alert_system["latest_alert"]
        st.error(f" **إشعار طوارئ نشط ({la['time']}):** تم رصد **{la['type']}** في **{la['city']} - {la['region']}**. تم توجيه الكاميرا وفرق الطوارئ للموقع.")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("حالة النظام", "طبيعي" if not st.session_state.simulation_active else "طوارئ نشطة ")
    with col2:
        reports_count = 4 + len(st.session_state.user_reports) + (8 if st.session_state.simulation_active else 0)
        st.metric("البلاغات النشطة", f"{reports_count}")
    with col3:
        st.metric("المدن / المناطق", f"{len(CITIES_DATA)} / {REGIONS_COUNT}")
    with col4:
        st.metric("مستوى التنبيه العام", "منخفض" if not st.session_state.simulation_active else "مرتفع جداً")

    st.divider()

    df_map = pd.DataFrame.from_dict(CITIES_DATA, orient='index').reset_index()
    df_map.rename(columns={'index': 'city'}, inplace=True)

    for rep in st.session_state.user_reports:
        idx = df_map[df_map['city'] == rep['city']].index
        if not idx.empty:
            df_map.loc[idx, 'risk_score'] = min(100, int(df_map.loc[idx, 'risk_score'].values[0]) + 35)
            df_map.loc[idx, 'incident'] = f"{rep['type']} - {rep['desc']}"
            df_map.loc[idx, 'weather'] = rep['type']

    if st.session_state.simulation_active and st.session_state.simulated_city:
        sim_idx = df_map[df_map['city'] == st.session_state.simulated_city].index
        if not sim_idx.empty:
            df_map.loc[sim_idx, 'risk_score'] = 100
            df_map.loc[sim_idx, 'weather'] = active_event
            df_map.loc[sim_idx, 'dust_level'] = "خطر"
            df_map.loc[sim_idx, 'incident'] = active_event

    head_col1, head_col2, head_col3 = st.columns([2, 1, 1])
    with head_col1:
        st.markdown("<div style='direction:rtl; text-align:right;'><h3>خريطة المملكة العربية السعودية</h3><p style='color:#5C5852; font-size:14px; margin-top:-8px;'></p></div>", unsafe_allow_html=True)
    with head_col2:
        if st.button(f"🔍 تقريب على {st.session_state.selected_city_name} وإظهار المنطقة"):
            c_row = df_map[df_map['city'] == st.session_state.selected_city_name].iloc[0]
            st.session_state.map_lat = float(c_row['lat'])
            st.session_state.map_lon = float(c_row['lon'])
            st.session_state.map_zoom = CITY_ZOOM
            st.session_state.map_pitch = 65
            st.rerun()
    with head_col3:
        if st.button("🌍 عرض خريطة المملكة كاملة"):
            st.session_state.map_lat = 24.0
            st.session_state.map_lon = 45.0
            st.session_state.map_zoom = 5.3
            st.session_state.map_pitch = 45
            st.session_state.map_bearing = 0
            st.rerun()

    # الخريطة ثلاثية الأبعاد: تضاريس + مباني + شوارع وأحياء بالعربية + تفاصيل الطقس عند تمرير الماوس
    render_3d_map(
        df_map,
        view={
            "lat": float(st.session_state.map_lat),
            "lon": float(st.session_state.map_lon),
            "zoom": float(st.session_state.map_zoom),
            "pitch": float(st.session_state.map_pitch),
            "bearing": float(st.session_state.get("map_bearing", 0)),
        },
        selected_city=st.session_state.selected_city_name,
        height=650,
    )
    st.caption("🖱️ مرّر الماوس على أي مدينة لعرض تفاصيل الطقس • انقر على المدينة للتقريب • اسحب بزر الماوس الأيمن (أو Ctrl + سحب) لإمالة الخريطة وتدويرها • قرّب على المدينة لإظهار المباني والشوارع والأحياء")



    st.divider()
    st.markdown('<div id="reports-section"></div>', unsafe_allow_html=True)
    col_map_detail, col_reports, col_routing = st.columns(3)

    with col_map_detail:
        st.markdown("<div dir='rtl' style='direction:rtl; text-align:right;'><h3>تفاصيل الطقس للمدينة والمنطقة</h3></div>", unsafe_allow_html=True)
        cities_list = list(df_map['city'].unique())
        idx = cities_list.index(st.session_state.selected_city_name) if st.session_state.selected_city_name in cities_list else 0

        selected_city_name = st.selectbox("اختر المدينة للتقريب وإظهار المنطقة تحت الدبوس:", cities_list, index=idx)
        if selected_city_name != st.session_state.selected_city_name:
            st.session_state.selected_city_name = selected_city_name
            c_row = df_map[df_map['city'] == selected_city_name].iloc[0]
            st.session_state.map_lat = float(c_row['lat'])
            st.session_state.map_lon = float(c_row['lon'])
            st.session_state.map_zoom = CITY_ZOOM
            st.rerun()

        city_info = df_map[df_map['city'] == selected_city_name].iloc[0]

        st.markdown(f"""
        <div class="metric-card" dir="rtl" style="direction:rtl; text-align:right;">
            <h3>📍 {city_info['city']} - {city_info['region']}</h3>
            <p><b>حالة الطقس:</b> {city_info['weather']}</p>
            <p><b>درجة الحرارة:</b> {city_info['temp']}</p>
            <p><b>الرطوبة:</b> {city_info['humidity']}</p>
            <p><b>سرعة الرياح:</b> {city_info['wind']}</p>
            <p><b>مستوى الغبار:</b> {city_info['dust_level']}</p>
            <p><b>البلاغات الحالية:</b> {city_info['incident']}</p>
            <p><b>نسبة الخطر:</b> {city_info['risk_score']}%</p>
        </div>
        """, unsafe_allow_html=True)

    with col_reports:
        st.markdown("<div dir='rtl' style='direction:rtl; text-align:right;'><h3> البلاغات والإنذارات</h3></div>", unsafe_allow_html=True)
        with st.expander("إضافة بلاغ جديد"):
            rep_city = st.selectbox("المدينة", cities_list, key="rep_city")
            rep_type = st.selectbox("نوع البلاغ", ["حادث مروري", "سيول وتجمع مياه", "عاصفة غبارية", "عاصفة رعدية وأمطار"])
            rep_desc = st.text_input("وصف الموقع")
            if st.button("إرسال البلاغ"):
                st.session_state.user_reports.insert(0, {
                    "city": rep_city,
                    "type": rep_type,
                    "desc": rep_desc if rep_desc else "بلاغ ميداني",
                })
                st.session_state.selected_city_name = rep_city
                c_row = df_map[df_map['city'] == rep_city].iloc[0]
                st.session_state.map_lat = float(c_row['lat'])
                st.session_state.map_lon = float(c_row['lon'])
                st.session_state.map_zoom = CITY_ZOOM
                st.success("تم إرسال البلاغ")
                st.rerun()

        if st.session_state.simulation_active:
            reports_list = [
                f"تنبيه عاجل: {active_event} في {st.session_state.simulated_city}.",
                f"مباشرة فرق الطوارئ لبلاغات في {st.session_state.simulated_city}.",
                f"تحذير من الأرصاد الجوية لسكان {st.session_state.simulated_city}."
            ]
        else:
            reports_list = [
                "الرياض: حركة السير طبيعية والأجواء صافية.",
                "جازان وأبها: تنبيه من هطول أمطار وجريان السيول.",
                "حفر الباطن: نشاط في الرياح السطحية وتدني الرؤية."
            ]

        for rep in st.session_state.user_reports[:6]:
            st.warning(f" بلاغ ({rep['city']}): {rep['type']} - {rep['desc']}")

        for item in reports_list:
            st.markdown(f"<div dir='rtl' style='direction:rtl; text-align:right; margin-bottom:6px;'>• {item}</div>", unsafe_allow_html=True)

    with col_routing:
        st.markdown("<div dir='rtl' style='direction:rtl; text-align:right;'><h3>توجيه الطوارئ</h3></div>", unsafe_allow_html=True)
        if (st.session_state.simulation_active and st.session_state.simulated_city == selected_city_name) or city_info['risk_score'] >= 65:
            st.error(f"حالة طوارئ في {selected_city_name} ({city_info['region']})")
            st.markdown(f"""
            <div dir="rtl" style="direction:rtl; text-align:right; line-height:1.8;">
                <b>نوع البلاغ:</b> {city_info['incident']}<br/>
                <b>الإجراء:</b> توجيه فرق الدفاع المدني والمرور لأقرب مسار آمن.<br/>
                <b>الوقت المقدر للوصول:</b> 7 دقائق
            </div>
            """, unsafe_allow_html=True)
            if st.button("إرسال تنبيه للفرق"):
                st.success("تم إرسال التنبيه للفرق الميدانية")
        else:
            st.success(f"الوضع مستقر في {selected_city_name} ({city_info['region']})")
            st.markdown("<div dir='rtl' style='direction:rtl; text-align:right;'>جميع الطرق سالكة ولا توجد بلاغات حرجة حالياً.</div>", unsafe_allow_html=True)


st.sidebar.title("")

with st.sidebar:        
    box_select = st.selectbox("Select The App ", ["عين الوطن","Calculator", "Ai"])

    sim_event = "سيول جارفة"

    if box_select == "Calculator":
        select_box = st.selectbox("Select", ["+", "-", "x", "÷", "x²"])
        select_box2 = st.selectbox("Select How Many Numbers You Want To Calculate", ["Two", "Three", "Four"])
    
    elif box_select == "عين الوطن":
        st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
            
            /* إجبار كافة العناصر العربية في المنصة على الاتجاه من اليمين لليسار RTL */
            .stApp, .main, .block-container, section[data-testid="stSidebar"] {
                font-family: 'Cairo', sans-serif !important;
                direction: rtl !important;
                text-align: right !important;
            }
            
            .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown ul, .stMarkdown li,
            label, div[data-testid="stHeadingWithActionElements"], div[data-testid="stCaptionContainer"],
            div[data-testid="stAlert"] div, div[data-testid="stNotification"] div, details summary {
                direction: rtl !important;
                text-align: right !important;
                unicode-bidi: embed !important;
                font-family: 'Cairo', sans-serif !important;
            }
            
            .stApp {
                background-color: #FAF8F5;
                color: #2B2B2B;
            }
            
            .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp label {
                color: #2B2B2B;
            }
            .stApp h1 {
                color: #4F7942 !important;
            }

            /* ===== ألوان نصوص الواجهة الرئيسية (Hero) - أقوى تخصيصاً من .stApp h1 ===== */
            .stApp .hero-full-screen h1.hero-main-title,
            .stApp .hero-full-screen .hero-main-title,
            .hero-full-screen h1.hero-main-title {
                color: #FDE047 !important;
                -webkit-text-fill-color: #FDE047 !important;
            }
            .stApp .hero-full-screen .hero-sub-title {
                color: #F8FAFC !important;
                -webkit-text-fill-color: #F8FAFC !important;
            }
            .stApp .hero-full-screen .hero-desc-text,
            .stApp .hero-full-screen .hero-desc-text b {
                color: #E2E8F0 !important;
                -webkit-text-fill-color: #E2E8F0 !important;
            }
            .stApp .hero-full-screen .hero-org-note {
                color: #CBD5E1 !important;
                -webkit-text-fill-color: #CBD5E1 !important;
            }
            .stApp .hero-full-screen .hero-badge-pill {
                color: #E2E8F0 !important;
                -webkit-text-fill-color: #E2E8F0 !important;
            }
            
            section[data-testid="stSidebar"] {
                background-color: #EAE3D2 !important;
                border-left: 1px solid #D5CBB8;
            }
            section[data-testid="stSidebar"] h1,
            section[data-testid="stSidebar"] h2,
            section[data-testid="stSidebar"] h3,
            section[data-testid="stSidebar"] p,
            section[data-testid="stSidebar"] label,
            section[data-testid="stSidebar"] .stMarkdown {
                color: #2C3527 !important;
                direction: rtl !important;
                text-align: right !important;
            }
            
            div[data-baseweb="select"] > div, div[data-baseweb="popover"] li, ul[role="listbox"] li {
                background-color: #FFFFFF !important;
                color: #1E293B !important;
                direction: rtl !important;
                text-align: right !important;
                font-family: 'Cairo', sans-serif !important;
            }
            div[data-baseweb="select"] > div {
                border: 1px solid #C8BFA8 !important;
            }
            div[data-baseweb="select"] span {
                color: #1E293B !important;
            }
            input {
                background-color: #FFFFFF !important;
                color: #1E293B !important;
                direction: rtl !important;
                text-align: right !important;
                font-family: 'Cairo', sans-serif !important;
            }
            
            .metric-card {
                background-color: #FFFFFF;
                color: #2B2B2B;
                border-radius: 10px;
                padding: 16px;
                border: 1px solid #E5E0D5;
                border-right: 6px solid #4F7942;
                box-shadow: 0 2px 6px rgba(0,0,0,0.04);
                direction: rtl !important;
                text-align: right !important;
            }
            .metric-card h3 {
                color: #4F7942 !important;
                margin-top: 0;
            }
            
            div[data-testid="stMetric"] {
                background-color: #FFFFFF;
                padding: 14px;
                border-radius: 10px;
                border: 1px solid #E5E0D5;
                border-top: 4px solid #4F7942;
                box-shadow: 0 2px 5px rgba(0,0,0,0.04);
                direction: rtl !important;
                text-align: right !important;
            }
            div[data-testid="stMetricLabel"] {
                display: flex !important;
                justify-content: flex-start !important;
                direction: rtl !important;
                text-align: right !important;
            }
            div[data-testid="stMetricLabel"] p {
                color: #5C5852 !important;
                font-weight: 600;
            }
            div[data-testid="stMetricValue"] div {
                color: #4F7942 !important;
                direction: rtl !important;
                text-align: right !important;
            }
            
            .stButton>button {
                width: 100%;
                background-color: #4F7942 !important;
                color: #FFFFFF !important;
                font-weight: bold;
                border-radius: 8px;
                border: none;
                direction: rtl !important;
                font-family: 'Cairo', sans-serif !important;
            }
            .stButton>button p, .stButton>button span {
                color: #FFFFFF !important;
            }
            .stButton>button:hover {
                background-color: #3D5E33 !important;
            }
            </style>
        """, unsafe_allow_html=True)

        if 'simulation_active' not in st.session_state:
            st.session_state.simulation_active = False
        if 'simulated_city' not in st.session_state:
            st.session_state.simulated_city = None
        if 'selected_city_name' not in st.session_state:
            st.session_state.selected_city_name = "الرياض"
        if 'user_reports' not in st.session_state:
            st.session_state.user_reports = []
        if 'map_lat' not in st.session_state:
            st.session_state.map_lat = 24.0
        if 'map_lon' not in st.session_state:
            st.session_state.map_lon = 45.0
        if 'map_zoom' not in st.session_state:
            st.session_state.map_zoom = 5.3
        if 'map_pitch' not in st.session_state:
            st.session_state.map_pitch = 45
        if 'map_bearing' not in st.session_state:
            st.session_state.map_bearing = 0
        if 'last_seen_alert_id' not in st.session_state:
            st.session_state.last_seen_alert_id = 0

        st.sidebar.image("https://img.icons8.com/color/96/saudi-arabia.png", width=80)
        st.sidebar.markdown("<div dir='rtl' style='direction:rtl; text-align:right;'><h2>التحكم والمحاكاة</h2><p style='font-size:13px;'></p></div>", unsafe_allow_html=True)

        sim_city = st.sidebar.selectbox("المدينة:", list(CITIES_DATA.keys()))
        sim_event = st.sidebar.selectbox("نوع الحالة:", ["سيول جارفة", "عاصفة غبارية", "حادث مروري", "أمطار رعدية غزيرة"])

        if st.sidebar.button("تشغيل المحاكاة يدوياً"):
            st.session_state.simulation_active = True
            st.session_state.simulated_city = sim_city
            st.session_state.auto_sim_event = sim_event
            st.session_state.selected_city_name = sim_city
            st.session_state.map_lat = CITIES_DATA[sim_city]["lat"]
            st.session_state.map_lon = CITIES_DATA[sim_city]["lon"]
            st.session_state.map_zoom = CITY_ZOOM
            st.toast(f" تم إطلاق إنذار: {sim_event} في {sim_city}", icon="⚠️")
            st.sidebar.success(f"تم تفعيل بلاغ {sim_event} في {sim_city}")

        if st.sidebar.button("إعادة ضبط"):
            st.session_state.simulation_active = False
            st.session_state.simulated_city = None
            st.session_state.user_reports = []
            st.session_state.map_lat = 24.0
            st.session_state.map_lon = 45.0
            st.session_state.map_zoom = 5.3
            st.session_state.map_pitch = 45
            st.session_state.map_bearing = 0
            st.sidebar.info("تمت إعادة النظام للوضع الطبيعي")


def calc():
    if select_box =="+":
        if select_box2 =="Two":
            two_sum()
        elif select_box2 =="Three":
            three_sum()
        elif select_box2 =="Four":
            four_sum()

    elif select_box =="-":
        if select_box2 == "Two":
            two_minus()        
        elif select_box2 =="Three":
            three_minus()
        elif select_box2 =="Four":
            four_minus()

    elif select_box =="x":
        if select_box2 == "Two":
            two_multi()        
        elif select_box2 == "Three":
             three_multi()
        elif select_box2 == "Four":
            four_multi()

    elif select_box =="÷":
        if select_box2 == "Two":
            two_dvide()
        elif select_box2 == "Three":
            three_dvide()
        elif select_box2 == "Four":
            four_dvide()
    elif select_box =="x²":
        multi_number()

def Ai_Sec():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        st.error("Missing GEMINI_API_KEY in .env file or environment.")
        st.stop()

    
    MODEL_NAME = "gemini-3.5-flash"

    client = genai.Client(api_key=api_key)

    st.title("🤖 AI Assistant")
    st.markdown("An Intelligent Assistant Powered By **Gemini** & **Tuwaiq Students**.")

    if "history" not in st.session_state:
        st.session_state.history = []

    def get_gemini_response(prompt, uploaded_file=None):
        contents = [prompt]

        if uploaded_file is not None:
            contents.append(
                genai.types.Part.from_bytes(
                    data=uploaded_file.getvalue(),
                    mime_type=uploaded_file.type,
                )
            )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
        )
        return response.text or "The AI returned an empty response."

   
    for role, msg in st.session_state.history:
        if role == "user":
            st.markdown(f"**You:** {msg}")
        else:
            st.markdown(f"**🤖 AI Assistant:** {msg}")

    with st.form("ai_chat_form", clear_on_submit=True):
        user_input = st.text_input("Type your message here...")
        send = st.form_submit_button("Send")

    uploaded_file = st.file_uploader(
        "Upload a file for the AI",
        type=["pdf", "png", "jpg", "jpeg", "txt", "csv", "py"],
        accept_multiple_files=False,
    )

    if uploaded_file is not None:
        st.caption(f"Attached: {uploaded_file.name}")
        if uploaded_file.type.startswith("image/"):
            st.image(uploaded_file, caption=uploaded_file.name)

    if send:
        if user_input.strip() or uploaded_file is not None:
            prompt = user_input.strip() or "Describe this uploaded file."

            st.session_state.history.append(("user", prompt))

            with st.spinner("AI Assistant is thinking..."):
                try:
                    reply = get_gemini_response(prompt, uploaded_file)
                except Exception as e:
                    reply = f"Error: {e}"

            st.session_state.history.append(("bot", reply))
            st.rerun()
        else:
            st.warning("Please enter a message or upload a file.")


if box_select == "عين الوطن":
    alw6n(sim_event)
elif box_select == "Calculator":
    calc()
elif box_select == "Ai":
    Ai_Sec()