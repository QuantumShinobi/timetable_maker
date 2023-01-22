import random
st = input("Enter school starting time:")
p = int(input("Enter number of periods:"))
np = int(input("Enter lunch period number:"))
mins_per_period = int(input("Enter number of minutes taken for 1 period:"))
no_of_teachers = int(input("Enter number of teachers:"))
# making each grade timetable lists
grades_subj = {}  # dictionary for subjects taught to different grades
# g_subj = {teacher:{grade:subjects}}

teacher_names = []
g1 = []  # elements are in [{teacher:subj}]
# g1= [{"abc":"chemitry"}, {"someone":"eng"}]
g2 = []
g3 = []
g4 = []
g5 = []
g6 = []
g7 = []
g8 = []
g9 = []
g10 = []
g11 = []
g12 = []
# Capital G lists are for sorted order
G1 = []
G2 = []
G3 = []
G4 = []
G5 = []
G6 = []
G7 = []
G8 = []
G9 = []
G10 = []
G11 = []
G12 = []

_g2 = []
_g3 = []
_g4 = []
_g5 = []
_g6 = []
_g7 = []
_g8 = []
_g9 = []
_g10 = []
_g11 = []
_g12 = []
# d= {
# "teacher":{"grade":"subj"}
# }
for i in range(0, no_of_teachers, 1):
    s = {}  # for convenience - grade:subj dictionary per teacher
    t = input("Enter teacher name:")
    teacher_names = teacher_names + [t]
    g = int(input("Enter number of grades taught:"))
    for j in range(0, g, 1):
        sj = input("Enter subject name:")
        gr = int(input("Enter grade for subject:"))
        s[gr] = sj
    grades_subj[t] = s
for a in range(0, no_of_teachers, 1):
    # putting a nested dictionary is each list of the grade in the {teacher:subj} format
    kt = list(grades_subj[teacher_names[a]].keys())
    for q in range(0, len(kt), 1):
        if kt[q] == 1:
            g1 = g1 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 2:
            g2 = g2 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 3:
            g3 = g3 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 4:
            g4 = g4 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 5:
            g5 = g5 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 6:
            g6 = g6 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 7:
            g7 = g7 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 8:
            g8 = g8 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 9:
            g9 = g9 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 10:
            g10 = g10 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 11:
            g11 = g11 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
        elif kt[q] == 12:
            g12 = g12 + [{
                teacher_names[a]: grades_subj[teacher_names[a]][kt[q]]
            }]
'''G = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]
## [[{"abc":"chemistry"}, {"someomne":"e"}],[g2]]
# to access the grade lists easly

for i in range(0, 12, 1):
    for j in range(0, p - len(G[i]) - 1, 1):
        G[i] = G[i] + [G[i][j]]
# checking extra periods than subjects
# eg 5 subjs and 10 periods, so any four subjects will repeat

g1 = G[0]
g2 = G[1]
g3 = G[2]
g4 = G[3]
g5 = G[4]
g6 = G[5]
g7 = G[6]
g8 = G[7]
g9 = G[8]
g10 = G[9]
g11 = G[10]
g12 = G[11]
# after this^, all the dictionaries have the same length which is equal to the no of periods -1 (excluding lunch)'''
for i in range(0, p - len(g1) - 1, 1):
    g1 = g1 + [g1[i]]
G1 = g1
_g2 = []
_g3 = []
_g4 = []
_g5 = []
_g6 = []
_g7 = []
_g8 = []
_g9 = []
_g10 = []
_g11 = []
_g12 = []


for i in range(0, p - 1, 1):
    c = 0
    while len(G2) == i:
        if len(g2) > 0:
            v = random.choice(g2)
            if v.keys() != G1[i].keys():
                G2 = G2 + [v]
                g2.remove(v)
                _g2 = _g2 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g2)
                if v.keys() != G1[i].keys():
                    G2 = G2 + [v]
        else:
            v = random.choice(_g2)
            if v.keys() != G1[i].keys():
                G2 = G2 + [v]
    c = 0
    while len(G3) == i:

        if len(g3) > 0:
            v = random.choice(g3)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys():
                G3 = G3 + [v]
                g3.remove(v)
                _g3 = _g3 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g3)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys():
                    G3 = G3 + [v]

        else:
            v = random.choice(_g3)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys():
                G3 = G3 + [v]
    c = 0
    while len(G4) == i:

        if len(g4) > 0:
            v = random.choice(g4)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys():
                G4 = G4 + [v]
                g4.remove(v)
                _g4 = _g4 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g4)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys():
                    G4 = G4 + [v]
        else:
            v = random.choice(_g4)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys():
                G4 = G4 + [v]
    c = 0
    while len(G5) == i:
        if len(g5) > 0:
            v = random.choice(g5)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys():
                G5 = G5 + [v]
                g5.remove(v)
                _g5 = _g5 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g5)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys():
                    G5 = G5 + [v]

        else:
            v = random.choice(_g5)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys():
                G5 = G5 + [v]
    c = 0
    while len(G6) == i:
        if len(g6) > 0:
            v = random.choice(g6)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys():
                G6 = G6 + [v]
                g6.remove(v)
                _g6 = _g6 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g6)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
                ) and v.keys() != G5[i].keys():
                    G6 = G6 + [v]
        else:
            v = random.choice(_g6)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys():
                G6 = G6 + [v]
    c = 0
    while len(G7) == i:
        if len(g7) > 0:
            v = random.choice(g7)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys():
                G7 = G7 + [v]
                g7.remove(v)
                _g7 = _g7 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g7)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
                ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys():
                    G7 = G7 + [v]
        else:
            v = random.choice(_g7)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys():
                G7 = G7 + [v]
    c = 0
    while len(G8) == i:
        if len(g8) > 0:
            v = random.choice(g8)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys():
                G8 = G8 + [v]
                g8.remove(v)
                _g8 = _g8 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g8)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
                ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
                ) and v.keys() != G7[i].keys():
                    G8 = G8 + [v]

        else:
            v = random.choice(_g8)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys():
                G8 = G8 + [v]
    c = 0
    while len(G9) == i:
        if len(g9) > 0:
            v = random.choice(g9)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys():
                G9 = G9 + [v]
                g9.remove(v)
                _g9 = _g9 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g9)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
                ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
                ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys():
                    G9 = G9 + [v]
        else:
            v = random.choice(_g9)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys():
                G9 = G9 + [v]
    c = 0
    while len(G10) == i:
        if len(g10) > 0:
            v = random.choice(g10)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
            ) and v.keys() != G9[i].keys():
                G10 = G10 + [v]
                g10.remove(v)
                _g10 = _g10 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g10)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
                ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
                ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
                ) and v.keys() != G9[i].keys():
                    G10 = G10 + [v]

        else:
            v = random.choice(_g10)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
            ) and v.keys() != G9[i].keys():
                G10 = G10 + [v]
    c = 0
    while len(G11) == i:
        if len(g11) > 0:
            v = random.choice(g11)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
            ) and v.keys() != G9[i].keys() and v.keys() != G10[i].keys():
                G11 = G11 + [v]
                g11.remove(v)
                _g11 = _g11 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g11)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
                ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
                ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
                ) and v.keys() != G9[i].keys() and v.keys() != G10[i].keys():
                    G11 = G11 + [v]
        else:
            v = random.choice(_g11)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
            ) and v.keys() != G9[i].keys() and v.keys() != G10[i].keys():
                G11 = G11 + [v]
    c = 0
    while len(G12) == i:
        if len(g12) > 0:
            v = random.choice(g12)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
            ) and v.keys() != G9[i].keys() and v.keys() != G10[i].keys(
            ) and v.keys() != G11[i].keys():
                G12 = G12 + [v]
                g12.remove(v)
                _g12 = _g12 + [v]
            c = c + 1
            if c > 3 * p:
                v = random.choice(_g12)
                if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
                ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
                ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
                ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
                ) and v.keys() != G9[i].keys() and v.keys() != G10[i].keys(
                ) and v.keys() != G11[i].keys():
                    G12 = G12 + [v]

        else:
            v = random.choice(_g12)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys(
            ) and v.keys() != G3[i].keys() and v.keys() != G4[i].keys(
            ) and v.keys() != G5[i].keys() and v.keys() != G6[i].keys(
            ) and v.keys() != G7[i].keys() and v.keys() != G8[i].keys(
            ) and v.keys() != G9[i].keys() and v.keys() != G10[i].keys(
            ) and v.keys() != G11[i].keys():
                G12 = G12 + [v]

G = [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12]
for i in range(0, 12, 1):
    G[i] = G[i][:np] + ['lunch'] + G[i][np:]
G1 = G[0]
G2 = G[1]
G3 = G[2]
G4 = G[3]
G5 = G[4]
G6 = G[5]
G7 = G[6]
G8 = G[7]
G9 = G[8]
G10 = G[9]
G11 = G[10]
G12 = G[11]

print(G1)
print(G3)
print(G3)
print(G4)
print(G5)
print(G6)
print(G7)
print(G8)
print(G9)
print(G10)
print(G11)
print(G12)

pst = []
st = input("Enter school starting time:")
mins_per_period = int(input("Enter number of minutes taken for 1 period:"))
p = 10
pst = []
if st[0] == 0:
    pst = pst + [st[1:]]
else:
    pst = pst + [st]
mins = int(st[:2]) * 60 + int(st[3:])
for i in range(0, p - 1, 1):
    mins = mins + mins_per_period
    pst = pst + [str(mins // 60) + ':' + str(mins % 60)]
    if len(str(mins % 60)) == 1:
        pst[i + 1] = pst[i + 1] + '0'

print(pst)
'''
Testing item:

import random
p=10
np=5
teacher_names = []
g1 = [{'a':1},{'b':2},{'c':3},{'d':4},{'e':5}]  #elements are in [{teacher:subj}]
# g1= [{"abc":"chemitry"}, {"someone":"eng"}]
g2 = [{'a':1},{'b':2},{'c':3},{'d':4},{'e':5}]
g3 = [{'a':1},{'b':2},{'c':3},{'d':4},{'e':5}]
g4 = [{'a':1},{'b':2},{'f':3},{'g':4},{'h':5}]
g5 = [{'a':1},{'b':2},{'f':3},{'g':4},{'h':5}]
g6 = [{'i':1},{'j':2},{'k':3},{'l':4},{'m':5}]
g7 = [{'i':1},{'j':2},{'k':3},{'l':4},{'m':5}]
g8 = [{'i':1},{'j':2},{'k':3},{'l':4},{'m':5}]
g9 = [{'n':1},{'o':2},{'k':3},{'l':4},{'m':5}]
g10 = [{'n':1},{'o':2},{'p':3},{'q':4},{'r':5}]
g11 = [{'n':1},{'o':2},{'p':3},{'q':4},{'r':5}]
g12 = [{'n':1},{'o':2},{'p':3},{'q':4},{'r':5}]
# Capital G lists are for sorted order
G1 = []
G2 = []
G3 = []
G4 = []
G5 = []
G6 = []
G7 = []
G8 = []
G9 = []
G10 = []
G11 = []
G12 = []
#d= {
# "teacher":{"grade":"subj"}
#}
for i in range(0,p-len(g1)-1, 1):
    g1=g1+[g1[i]]
G = [ g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12]
## [[{"abc":"chemistry"}, {"someomne":"e"}],[g2]]
# to access the grade lists easly

for i in range(0, 11, 1):
    for j in range(0, p - len(G[i]) - 1, 1):
        v=random.choice(G[i])
        G[i] = G[i] + [v]
# checking extra periods than subjects
# eg 5 subjs and 10 periods, so any four subjects will repeat



g2 = G[0]
g3 = G[1]
g4 = G[2]
g5 = G[3]
g6 = G[4]
g7 = G[5]
g8 = G[6]
g9 = G[7]
g10 = G[8]
g11 = G[9]
g12 = G[10]
# after this^, all the dictionaries have the same length which is equal to the no of periods -1 (excluding lunch

G1 = g1
_g2=[]
_g3=[]
_g4=[]
_g5=[]
_g6=[]
_g7=[]
_g8=[]
_g9=[]
_g10=[]
_g11=[]
_g12=[]


for i in range(0, p - 1, 1):
    while len(G2) == i:
        if len(g2)>0:
            v=random.choice(g2)
            if v.keys()!=G1[i].keys():
                G2=G2+[v]
                g2.remove(v)
                _g2=_g2+[v]
        else:
            v=random.choice(_g2)
            if v.keys()!=G1[i].keys():
                G2=G2+[v]
    while len(G3) == i:
        if len(g3)>0:
            v = random.choice(g3)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys():
                G3 = G3 + [v]
                g3.remove(v)
                _g3=_g3+[v]
        else:
            v = random.choice(_g3)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys():
                G3 = G3 + [v]
          
    while len(G4) == i:
        if len(g4)>0:
            v = random.choice(g4)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys():
                G4 = G4 + [v]
                g4.remove(v)
                _g4=_g4+[v]
        else:
            v = random.choice(_g4)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys():
                G4 = G4 + [v]
                
    while len(G5) == i:
        if len(g5)>0:
            v = random.choice(g5)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys():
                G5 = G5 + [v]
                g5.remove(v)
                _g5=_g5+[v]
        else:
            v = random.choice(_g5)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys():
                G5 = G5 + [v]
                
    while len(G6) == i:
        if len(g6)>0:     
            v = random.choice(g6)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys():
                G6 = G6 + [v]
                g6.remove(v)
                _g6=_g6+[v]
        else:
            v = random.choice(_g6)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys():
                G6 = G6 + [v]
    while len(G7) == i:
        if len(g7)>0:
            v = random.choice(g7)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys():
                G7 = G7 + [v]
                g7.remove(v)
                _g7=_g7+[v]
        else:
            v = random.choice(_g7)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys():
                G7 = G7 + [v]
                
    while len(G8) == i:
        if len(g8)>0: 
            v = random.choice(g8)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys():
                G8 = G8 + [v]
                g8.remove(v)
                _g8=_g8+[v]
        else:
            v = random.choice(_g8)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys():
                G8 = G8 + [v]
    while len(G9) == i:
        if len(g9)>0:
            v = random.choice(g9)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys():
                G9 = G9 + [v]
                g9.remove(v)
                _g9=_g9+[v]
        else:
            v = random.choice(_g9)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys():
                G9 = G9 + [v]
    while len(G10) == i:
        if len(g10)>0:
            v = random.choice(g10)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys() and v.keys() != G9[i].keys():
                G10 = G10 + [v]
                g10.remove(v)
                _g10=_g10+[v]
        else:
            v = random.choice(_g10)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys() and v.keys() != G9[i].keys():
                G10 = G10 + [v]
    while len(G11) == i:
        if len(g11)>0:
            v = random.choice(g11)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys() and v.keys() != G9[i].keys() and v.keys() != G10[i].keys():
                G11 = G11 + [v]
                g11.remove(v)
                _g11=_g11+[v]
        else:
            v = random.choice(_g11)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys() and v.keys() != G9[i].keys() and v.keys() != G10[i].keys():
                G11 = G11 + [v]
    while len(G12) == i:
        if len(g12)>0:
            v = random.choice(g12)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys() and v.keys() != G9[i].keys() and v.keys() != G10[i].keys() and v.keys()!=G11[i].keys():
                G12 = G12 + [v]
                g12.remove(v)
                _g12=_g12+[v]
        else:
            v = random.choice(_g12)
            if v.keys() != G1[i].keys() and v.keys() != G2[i].keys() and v.keys() != G3[i].keys() and v.keys() != G4[i].keys() and v.keys() != G5[i].keys() and v.keys() != G6[i].keys() and v.keys() != G7[i].keys() and v.keys() != G8[i].keys() and v.keys() != G9[i].keys() and v.keys() != G10[i].keys() and v.keys()!=G11[i].keys():
                G12 = G12 + [v]
                
            
       

      

G = [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12]
for i in range(0, 12, 1):
    G[i] = G[i][:np] + ['lunch'] + G[i][np:]
G1 = G[0]
G2 = G[1]
G3 = G[2]
G4 = G[3]
G5 = G[4]
G6 = G[5]
G7 = G[6]
G8 = G[7]
G9 = G[8]
G10 = G[9]
G11 = G[10]
G12 = G[11]

print(G1)
print(G2)
print(G3)
print(G4)
print(G5)
print(G6)
print(G7)
print(G8)
print(G9)
print(G10)
print(G11)
print(G12)




'''
