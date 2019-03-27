from django.shortcuts import render, redirect
from status_board.models import bridgeTable, Escalators, Elevators, message
from .forms import bridgeTableForm, elevatorForm, escalatorForm, messageForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def home(request):
	# Display all systems ie user is authenticated
	# if request.user.is_authenticated:
		bridgeTableData = bridgeTable.objects.order_by('bridgeTableID')
		elevatorData = Elevators.objects.order_by('elevatorID')
		#escalatorData = Escalators.object.order_by('escalatorID')
		context = {
			'bridges': bridgeTableData,
			'elevators': elevatorData,
			#'escalators': escalatorData,
		}
		return render(request, 'status_board/home.html', context)


	# Display only bridgeTable, elevaotrData, escalatorData ie view for airline employees
	# else:
	# 	bridgeTableData = bridgeTable.objects.order_by('bridgeTableID')
# 		elevatorData = Elevators.objects.order_by('elevatorID')
# 		escalatorData = Escalators.object.order_by('escalatorID')
	#
	#
	# 	context = {
	# 		'bridges': bridgeTableData,
	# 		'elevators': elevatorData,
	#		'escalators': escalatorData,
	# 	}
	# 	return render(request, 'status_board/home.html', context)



#Update the bridge table
def bridgeTableUpdate(request, btID):
	btID = int(btID)
	tableID = bridgeTable.objects.filter(bridgeTableID=btID).first()
	form = bridgeTableForm(request.POST or None, instance=tableID)
	path = 'fromBridgeTable'

	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

#Update the elevator table
def elevatorUpdate(request, btID):
	#btID = int(btID)
	tableID = Elevators.objects.filter(elevatorID=btID).first()
	form = elevatorForm(request.POST or None, instance=tableID)
	path = 'fromElevator'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)

#Update the elevator table
def escalatorUpdate(request, btID):
	btID = int(btID)
	tableID = Escalators.objects.filter(escalatorID=btID).first()
	form = escalatorForm(request.POST or None, instance=tableID)
	path = 'fromEscalator'
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
		'path': path,
	}
	return render(request, 'status_board/forms.html', context)



#Update the escalator table
def messageUpdate(request):

	tableID = message.objects.first()
	form = messageForm(request.POST or None, instance=tableID)
	if form.is_valid():
		form.save()
		return redirect('status-board-home') #need to change redirect
	context = {
		'form': form,
		'obj': tableID,
	}
	return render(request, 'status_board/forms.html', context)