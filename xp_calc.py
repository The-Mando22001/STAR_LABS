import math

a = int(input("Target XP: "))

t1, t2, t3, t4, t5, t6 = 0, 0, 0, 0, 0, 0
m1, m2, m3, m4, m5, m6 = 0, 0, 0, 0, 0, 0
t6 = math.floor(a/1500)
if t6 >= 20:
    t6 = t6 - 20
t5 = math.floor((a - (t6*1500))/750)
if t5 >= 20:
    t5 = t5 - 20
t4 = math.floor((a - (t6*1500) - (t5*750))/375)
if t4 >= 15:
    t4 = t4 - 15
t3 = math.floor((a - (t6*1500) - (t5*750) - (t4*375))/100)
if t3 >= 15:
    t3 = t3 - 15
t2 = math.floor((a - (t6*1500) - (t5*750) - (t4*375) - (t3*100))/50)
if t2 >= 15:
    t2 = t2 - 15
t1 = math.floor((a - (t6*1500) - (t5*750) - (t4*375) - (t3*100) - (t2*50))/25)

m6 = math.floor(total_xp/3000)
if m6 >= 20:
    m6 = m6 - 20
m5 = math.floor((total_xp - (m6*3000))/1500)
if m5 >= 20:
    m5 = m5 - 20
m4 = math.floor((total_xp - (m6*3000) - (m5*1500))/750)
if m4 >= 15:
    m4 = m4 - 15
m3 = math.floor((total_xp - (m6*3000) - (m5*1500) - (m4*750))/200)
if m3 >= 15:
    m3 = m3 - 15
m2 = math.floor((total_xp - (m6*3000) - (m5*1500) - (m4*750) - (m3*200))/100)
if m2 >= 15:
    m2 = m2 - 15
m1 = math.floor((total_xp - (m6*3000) - (m5*1500) - (m4*750) - (m3*200) - (m2*100))/50)

print(f"The amount of XP Capsules required is:\nT1: {t1}\nT2: {t2}\nT3: {t3}\nT4: {t4}\nT5: {t5}\nT6: {t6}")
print(f"The amount of Matching XP Capsules required is:\nM1: {m1}\nM2: {m2}\nM3: {m3}\nM4: {m4}\nM5: {m5}\nM6: {m6}")