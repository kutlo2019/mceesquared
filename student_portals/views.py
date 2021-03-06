from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry, MathematicsAssignmentGrades
from .forms import TopicForm, EntryForm

def check_topic_owner(topic, request):
	"""Check whether the topic matches the user logged in."""
	if topic.owner != request.user:
		raise Http404

def index(request):
	"""The home page for student portal."""
	return render(request, 'student_portals/index.html')

@login_required
def topics(request):
	"""Show all topics."""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'student_portals/topics.html', context)

@login_required
def topic(request, topic_id):
	"""Show a single topic and all its entries."""
	topic = Topic.objects.get(id=topic_id)
	# Make sure the topic belongs to the current user.
	check_topic_owner(topic, request)

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'student_portals/topic.html', context)

@login_required
def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted; process data.
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return redirect('student_portals:topics')

	# Display a blank or invalid form.
	context = {'form': form}
	return render(request, 'student_portals/new_topic.html', context)

@login_required
def edit_topic(request, topic_id):
	"""Edit an existing topic."""
	topic = Topic.objects.get(id=topic_id)
	check_topic_owner(topic, request)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = TopicForm(instance=topic)
	else:
		# POST data submitted; process data.
		form = TopicForm(instance=topic, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('student_portals:topic', topic_id=topic.id)

	context = {'topic': topic, 'form': form}
	return render(request, 'student_portals/edit_topic.html', context)
	
@login_required
def new_entry(request, topic_id):
	"""Add a new entry for a particular topic."""
	topic = Topic.objects.get(id=topic_id)
	check_topic_owner(topic, request)

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = EntryForm()
	else:
		# POST data submitted; process data.
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('student_portals:topic', topic_id=topic_id)
	# Display a blank or invalid form.
	context = {'topic': topic, 'form': form}
	return render(request, 'student_portals/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	check_topic_owner(topic, request)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
	else:
		# POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('student_portals:topic', topic_id=topic.id)

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'student_portals/edit_entry.html', context)

@login_required
def grade_book(request):
	"""Access student grades"""
	return render(request, 'student_portals/grade_book.html')

@login_required
def assignment_submission(request):
	"""Submit assignment."""
	return render(request, 'student_portals/assignment_submission.html')

@login_required
def class_grades(request):
	"""Submit assignment."""
	return render(request, 'student_portals/class_grades.html')

@login_required
def mathematics_grades(request):
	"""Show all Mathematics grades."""
	grades = MathematicsAssignmentGrades.objects.filter(owner=request.user).order_by('date_added')
	context = {'grades': grades}
	return render(request, 'student_portals/mathematics_grades.html', context)

@login_required
def physics_grades(request):
	"""Show all Mathematics grades."""
	grades = MathematicsAssignmentGrades.objects.filter(owner=request.user).order_by('date_added')
	context = {'grades': grades}
	return render(request, 'student_portals/physics_grades.html', context)

@login_required
def chemistry_grades(request):
	"""Show all Mathematics grades."""
	grades = MathematicsAssignmentGrades.objects.filter(owner=request.user).order_by('date_added')
	context = {'grades': grades}
	return render(request, 'student_portals/chemistry_grades.html', context)

@login_required
def biology_grades(request):
	"""Show all Mathematics grades."""
	grades = MathematicsAssignmentGrades.objects.filter(owner=request.user).order_by('date_added')
	context = {'grades': grades}
	return render(request, 'student_portals/biology_grades.html', context)