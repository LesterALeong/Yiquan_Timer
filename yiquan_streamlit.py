import streamlit as st
import random
import time
from datetime import timedelta

# Define the stances
front_stances = [
    "Cheng Bao Zhuang (Prop Hug)", "Fu Yun Zhuang (Float Cloud)", "Tui Tuo Zhuang (Push Prop)",
    "Fu Bao Zhuang (Float Hug)", "Fu An Zhuang (Float Press)", "Ti Cha Zhuang (Lift Jab)",
    "Xiu Xi Zhuang (Resting)", "Fun Shui Zhuang (Split Water)", "Ti Bao Zhuang (Lift Hug)",
    "Yang Shen Zhuang (Cultivating Spirit)"
]

side_stances = [
    "Hun Yuan Zhuang (Sphere)", "Mao Dun Zhuang (Spear and Shield)", "Gou Gua Zhuang (Hook Hang)",
    "Ping Bao Zhuang (Even Hug)", "Dun Bao Bei Zhuang (Hold Treasure)"
]

power_stances = [
    "Xiang Long Zhuang (Descending Dragon)", "Fu Hu Zhuang (Taming Tiger)", "Du Li Zhuang (Chicken)",
    "Ying Zhuang (Eagle)", "Cheng Tui Zhuang (Stretch Leg)"
]

# Function to generate the workout
def generate_workout(duration):
    workout = []
    
    # Add warm-up
    workout.append(("Warm-Up", 5))
    
    # Remaining time
    remaining_time = duration - 5
    
    # Generate workout
    while remaining_time > 0:
        stance_type = random.choice(['front', 'side', 'power'])
        
        if stance_type == 'front':
            stance = random.choice(front_stances)
            time_for_stance = min(remaining_time, random.randint(5, 20))
            workout.append((stance, time_for_stance))
        
        elif stance_type == 'side':
            stance = random.choice(side_stances)
            time_for_stance = min(remaining_time, random.randint(5, 20) // 2) * 2
            workout.append((stance + " (Left Side)", time_for_stance // 2))
            workout.append((stance + " (Right Side)", time_for_stance // 2))
        
        elif stance_type == 'power':
            stance = random.choice(power_stances)
            time_for_stance = min(remaining_time, random.randint(5, 20) // 2) * 2
            workout.append((stance + " (Left Side)", time_for_stance // 2))
            workout.append((stance + " (Right Side)", time_for_stance // 2))
        
        remaining_time -= time_for_stance
    
    return workout

# Streamlit app
st.title('Yiquan Stance Workout Generator')

# User input for workout duration
duration = st.slider('Select workout duration (minutes)', min_value=10, max_value=120, value=30, step=5)

if st.button('Generate Workout'):
    workout = generate_workout(duration)
    
    st.subheader('Your Workout:')
    for stance, time_for_stance in workout:
        st.write(f"{stance}: {time_for_stance} minutes")

    if st.button('Start Workout'):
        st.subheader('Workout Timer:')
        for stance, time_for_stance in workout:
            st.write(f"Current stance: {stance}")
            for remaining_time in range(time_for_stance * 60, 0, -1):
                mins, secs = divmod(remaining_time, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                st.write(f"Time remaining: {timer}")
                time.sleep(1)
                st.empty()
            st.write(f"{stance} completed!")
