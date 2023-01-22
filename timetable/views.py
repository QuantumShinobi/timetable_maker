from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Timetable, Teacher
import json

# Create Login page view


class MainView(View):
    def get(self, request):
        return render(request, "index.html")


def main(request):
    return render(request, "index.html")


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
        print(periods, len_per_period, lunch_period, no_of_teachers,
              start_time, end_time)
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
        resp.set_cookie("Timetable_identity", timetable.uuid)
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
                return render(
                    request,
                    "teacher_info_form.html",
                    context={
                        "no_of_teachers":
                        [f"{str(x+1)}"
                         for x in range(timetable.no_of_teachers)]
                    })
                pass

    def post(self, request):
        Teacher.objects.all().delete()
        timetable = Timetable.objects.get(
            uuid=request.COOKIES['Timetable_identity'])
        teachers = {}
        for i in range(1, timetable.no_of_teachers+1):
            name = request.POST[f"teacher_{i}_name"]
            grades = {name: [int(x) for x in (
                request.POST[f"teacher_{i}_grades"].split(','))]}
            subj = request.POST[f"teacher_{i}_subj"]
            globals()[f'teacher_{i}_info'] = {}
            globals()[
                f'teacher_{i}_info']['name'] = name
            globals()[
                f'teacher_{i}_info']['grades'] = grades
            globals()[
                f'teacher_{i}_info']['subj'] = subj
            # Create teacher model for each teacher
            teach = Teacher.objects.create(
                name=name, subject=subj, grades_taught=grades)
            teach.save()
            timetable.teachers.add(teach)
            teachers[f"teacher_{i}_info"] = globals()[f'teacher_{i}_info']
        print(timetable.teachers)
        comp = timetable.make_class_dict()
        # compiled_timetable = timetable.sort()
        print(comp)
        return HttpResponse(json.dumps(comp, indent=4), content_type="application/json")
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
                pass
                timetable_dict = timetable.show_timetable()
                # timeable dict is a dictionary with everyclass as the key and then it's timetable as the Value
                return render(request,
                              "timetable.html",
                              context={
                                  "timetable_dict": timetable_dict,
                                  "timetable_obj": timetable
                              })
