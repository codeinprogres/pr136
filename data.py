import pandas as pd

df = pd.read_csv("new_final_data.csv")

names = df["Star_Name"].tolist()
distance = df["Distance"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
gravity = df["Gravity"].tolist()

final_planet_list = []
temp_dict = {
                "name": names,
                "distance": distance,
                "planet_mass": mass,
                "planet_radius": radius,
                "gravity": gravity,
            }

final_planet_list.append(temp_dict)
print(final_planet_list)

data = final_planet_list
