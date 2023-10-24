import numpy as np

#  tehtävän 1 osa 1
#  muunna asteiksi
a = 2.493
b = 0.911
print("Radiaanit asteina: ")
print(f"a = {np.degrees(a)} ja b = {np.degrees(b)}\n\n")

# tehtävän 1 osa 2
# muunna radiaaneiksi
a2 = 137.7
b2 = 62.3
print("Asteet radiaaneina: ")
print(f"a = {np.radians(a2)} ja b = {np.radians(b2)}\n\n")

# tehtävän 1 osa 3
# taulukko, jossa asteet muunnettu radiaaneiksi
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
print("Radiaanitaulukko")
for i in A:
    print(f"{np.radians(i):.2f}")
print("\n\n")

#  tehtävä 2
# lasketaan hypotenuusan pituus (k = kateetti)
k1 = 1.6
k2 = 2.3
hypo = np.hypot(k1, k2)
print(f"Kateetti 1: {k1}m ja kateetti 2: {k2}m")
print(f"Hypotenuusan pituus: {hypo:.2f}m\n\n")
