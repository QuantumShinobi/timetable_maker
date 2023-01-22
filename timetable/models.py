import random
from django.db import models
import datetime
import uuid
import json


class Teacher(models.Model):
    unique_id = models.UUIDField(unique=True,
                                 default=uuid.uuid4,
                                 editable=False,
                                 primary_key=True)
    name = models.CharField(max_length=256, default="Teach")
    subject = models.CharField(max_length=256, default="None")
    grades_taught = models.JSONField(null=True)
    # subject_acc_class = models.JSONField()
    # working_days = serializers.ListField()


class Timetable(models.Model):
    periods = models.IntegerField(default=10)
    uuid = models.UUIDField(default=uuid.uuid4(), unique=True)
    lunch_period = models.IntegerField(default=5)
    len_per_period = models.IntegerField(default=40)
    no_of_teachers = models.IntegerField(default=10)
    start_time = models.TimeField(blank=True,
                                  default=datetime.time(hour=9,
                                                        minute=0,
                                                        second=0))
    end_time = models.TimeField(blank=True,
                                default=datetime.time(hour=15,
                                                      minute=0,
                                                      second=0))
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return (f"Timetable {self.id}")

    def make_class_dict(self):
        # Takes the teachers taught and arranges them by grades which they teach
        g1 = []
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
        g13 = []
        for i in range(1, 13):
            for x, teach in enumerate(self.teachers.all()):
                x += 1
                n = teach.name
                print(teach.grades_taught[n])
                if i in teach.grades_taught[n]:
                    locals()[f'g{int(i)}'].append({n: teach.subject})
        self.grade_1 = g1
        self.grade_2 = g2
        self.grade_3 = g3
        self.grade_4 = g4
        self.grade_5 = g5
        self.grade_6 = g6
        self.grade_7 = g7
        self.grade_8 = g8
        self.grade_9 = g9
        self.grade_10 = g10
        self.grade_11 = g11
        self.grade_12 = g12
        return self.compile_classes()

    def sort(self):
        st = self.start_time
        p = self.periods
        np = self.lunch_period
        mins_per_period = self.len_per_period
        no_of_teachers = self.no_of_teachers
        # Capital G lists are for sorted order
        g1 = self.grade_1
        g2 = self.grade_2
        g3 = self.grade_3
        g4 = self.grade_4
        g5 = self.grade_5
        g6 = self.grade_6
        g7 = self.grade_7
        g8 = self.grade_8
        g9 = self.grade_9
        g10 = self.grade_10
        g11 = self.grade_11
        g12 = self.grade_12
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

        # Sorts the various classes into the groups and the
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
        self.sorted_grade_1 = G1
        self.sorted_grade_2 = G2
        self.sorted_grade_3 = G3
        self.sorted_grade_4 = G4
        self.sorted_grade_5 = G5
        self.sorted_grade_6 = G6
        self.sorted_grade_7 = G7
        self.sorted_grade_8 = G8
        self.sorted_grade_9 = G9
        self.sorted_grade_10 = G10
        self.sorted_grade_11 = G11
        self.sorted_grade_12 = G12
        return self.compile_timetable()

    def show_timetable(self):
        # return the object in a single nested dictionary of the format {"grade":{timetable}}
        pass

    def comparision_operator(self):
        # makes a comparable string so that the timetable can be compared with only a single parameter
        pass

    def make_other_case(self):
        # makes other case of timetable, other than the currently made timetable
        # each new case would have a new comparision operator too
        pass

    # Compiling methods

    def compile_timetable(self):
        a = {
            "grade_1": self.sorted_grade_1, "grade_2": self.sorted_grade_2, "grade_3": self.sorted_grade_3, "grade_4": self.sorted_grade_4, "grade_5": self.sorted_grade_5, "grade_6": self.sorted_grade_6, "grade_7": self.sorted_grade_7, "grade_8": self.sorted_grade_8, "grade_9": self.sorted_grade_9, "grade_10": self.sorted_grade_10, "grade_11": self.sorted_grade_11, "grade_12": self.sorted_grade_12}
        self.compiled_timetable = json.dumps(a, sort_keys=True, indent=4)
        return self.compiled_timetable

    def compile_classes(self):
        a = {
            "grade_1": self.grade_1, "grade_2": self.grade_2, "grade_3": self.grade_3, "grade_4": self.grade_4, "grade_5": self.grade_5, "grade_6": self.grade_6, "grade_7": self.grade_7, "grade_8": self.grade_8, "grade_9": self.grade_9, "grade_10": self.grade_10, "grade_11": self.grade_11, "grade_12": self.grade_12}
        return json.dumps(a, sort_keys=True, indent=4)
