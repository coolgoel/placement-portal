from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
	return render(request, 'home/home.html')

def studentsList(request):
	students = Student.objects.all()
	context = {
		'students': students,
	}

	return render(request, 'home/studentsList.html', context)


def studentDetails(request, student_id):


	student = Student.objects.get(pk=int(student_id))

	if request.method == 'POST':
		form = StudentPlacedForm(request.POST)
		if form.is_valid():
			placed = form.cleaned_data.get('placed')
			company = form.cleaned_data.get('company')
			sector = form.cleaned_data.get('sector')
			profile = form.cleaned_data.get('profile')
			day = form.cleaned_data.get('day')
			slot = form.cleaned_data.get('slot')
			student.placed = True
			student.company = company
			student.sector = sector
			student.profile = profile
			student.branch.num+=1

			dobj = Day.objects.filter(dayNum=day, branch=student.branch)
			# print(dobj)
			# print("CCCCCCCCCCCCCCCCCCCC")
			if dobj.count()==0:

				Day.objects.create(dayNum=day, branch=student.branch)
				dobj = Day.objects.get(dayNum=day, branch=student.branch)
			else:
				dobj = dobj[0]

			dobj.num += 1
			dobj.save()
			# print (student.daynum)
			# print("check")
			student.save()
			student.branch.save()
			
		return redirect('home:students')
	else:
		form = StudentPlacedForm()
		if not student.placed:

			context = {
			'form':form,
			'student': student,
			}
		else:

			 context = {
			'form':form,
			'student': student,
			}


		return render(request, 'home/studentDetails.html', context)
