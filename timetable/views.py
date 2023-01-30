from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Timetable, Teacher
import json

# Create Login page view


class MainView(View):
    def get(self, request):
        return render(request, "index.html")


def html(request):
    return render(request, "timetable.html")


def test(request):
    try:
        timetable_uuid = request.COOKIES['Timetable_identity']
    except (KeyError, AttributeError):
        return render(request, "main_form.html")
    else:
        try:
            timetable = Timetable.objects.get(uuid=timetable_uuid)
        except Timetable.DoesNotExist:
            resp = render(request, "main_form.html")
            resp.delete_cookie("Timetable_identity")
            return resp
        else:
            pass


class InputView(View):
    def get(self, request):
        try:
            timetable_uuid = request.COOKIES['Timetable_identity']
        except (KeyError, AttributeError):
            return render(request, "main_form.html")
        else:
            try:
                timetable = Timetable.objects.get(uuid=timetable_uuid)
            except Timetable.DoesNotExist:
                resp = render(request, "main_form.html")
                resp.delete_cookie("Timetable_identity")
                return resp
            else:
                return redirect("timetable:teacher_form")

    def post(self, request):
        periods = request.POST['no_of_periods']
        len_per_period = request.POST['period_duration']
        # teachers = request.POST['teachers']
        lunch_period = request.POST['lunch_period']
        no_of_teachers = request.POST['no_of_teachers']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        # print(periods, len_per_period, lunch_period, no_of_teachers,
        #       start_time, end_time)
        # convert time to datetime format so that it can be put in the database object
        # to get the information of teachers depending on the number of teachers and then assigning that information to the timetable class so that the timetable can be made
        # the information should be a dictionary and the number of dictionaries will be equal to the number of teachers
        timetable = Timetable.objects.create(periods=periods,
                                             len_per_period=len_per_period,
                                             lunch_period=lunch_period,
                                             no_of_teachers=no_of_teachers,
                                             start_time=start_time,
                                             end_time=end_time)
        timetable.save()
        resp = redirect("timetable:teacher_form")
        resp.set_cookie("Timetable_identity", timetable.uuid, max_age=31556952)
        # teachers should be a dictionary of the form -> teacher:subject
        return resp


class TeacherInput(View):
    def get(self, request):
        try:
            timetable_uuid = request.COOKIES['Timetable_identity']
        except (KeyError, AttributeError):
            return redirect("timetable:main_form")
        else:
            try:
                timetable = Timetable.objects.get(uuid=timetable_uuid)
            except Timetable.DoesNotExist:
                return redirect("timetable:main_form")
            else:
                if timetable.used_once == True:
                    return redirect("timetable:show_timetable")
                return render(request,
                              "teacher_info_form.html",
                              context={
                                  "no_of_teachers": [
                                      f"{str(x+1)}"
                                      for x in range(timetable.no_of_teachers)
                                  ]
                              })
                pass

    def post(self, request):
        Teacher.objects.all().delete()
        timetable = Timetable.objects.get(
            uuid=request.COOKIES['Timetable_identity'])
        teachers = {}
        for i in range(1, timetable.no_of_teachers + 1):
            name = request.POST[f"teacher_{i}_name"]
            grades = {
                name: [
                    int(x)
                    for x in (request.POST[f"teacher_{i}_grades"].split(','))
                ]
            }
            subj = request.POST[f"teacher_{i}_subj"]
            globals()[f'teacher_{i}_info'] = {}
            globals()[f'teacher_{i}_info']['name'] = name
            globals()[f'teacher_{i}_info']['grades'] = grades
            globals()[f'teacher_{i}_info']['subj'] = subj
            # Create teacher model for each teacher
            teach = Teacher.objects.create(name=name,
                                           subject=subj,
                                           grades_taught=grades)
            teach.save()
            timetable.teachers.add(teach)
            teachers[f"teacher_{i}_info"] = globals()[f'teacher_{i}_info']
        # print(timetable.teachers)
        comp = timetable.make_class_dict()
        compiled_timetable = timetable.sort()
        # print(compiled_timetable)
        timetable.period_wise()
        return redirect("timetable:show_timetable")
        # adding teachers to grade_list


class TimetableView(View):
    def get(self, request):
        try:
            timetable_uuid = request.COOKIES['Timetable_identity']
        except (KeyError, AttributeError):
            return redirect("timetable:input")
        else:
            try:
                timetable = Timetable.objects.get(uuid=timetable_uuid)
            except Timetable.DoesNotExist:
                return redirect("timetable:input")
            else:
                a = timetable.output_format()

                # timeable dict is a dictionary with everyclass as the key and then it's timetable as the Value
                return render(request,
                              "timetable.html",
                              context={
                                  "timetable_obj": timetable,
                                  'period_1': timetable.t_1,
                                  'period_2': timetable.t_2,
                                  'period_3': timetable.t_3,
                                  'period_4': timetable.t_4,
                                  'period_5': timetable.t_5,
                                  'period_6': timetable.t_6,
                                  'period_7': timetable.t_7,
                                  'period_8': timetable.t_8,
                                  'period_9': timetable.t_9,
                                  'period_10': timetable.t_10,
                                  'period_11': timetable.t_11,
                                  'period_12': timetable.t_12,
                              })


def clear_cookie(request):
    resp = redirect("timetable:main_form")
    resp.delete_cookie("Timetable_identity")
    return resp
