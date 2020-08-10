"""Defines URL patterns for student_portals."""

from django.urls import path

from . import views

app_name = 'student_portals'
urlpatterns = [
	# Home page.
	path('', views.index, name='index'),
	# Page that shows all topics.
	path('topics/', views.topics, name='topics'),
	# Detail page for a single topic.
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	# Page for adding a new topic.
	path('new_topic/', views.new_topic, name='new_topic'),
	# Page for editing a topic
	path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
	# Page for adding a new entry.
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Page for editing an entry.
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	# Page accessing grades.
	path('grade_book/', views.grade_book, name='grade_book'),
	# Page accessing Mathematics grades.
	path('grade_book/mathematics_grades', views.mathematics_grades, name='mathematics_grades'),
	# Page accessing Mathematics grades.
	path('grade_book/physics_grades', views.physics_grades, name='physics_grades'),
	# Page accessing Mathematics grades.
	path('grade_book/chemistry_grades', views.chemistry_grades, name='chemistry_grades'),
	# Page accessing Mathematics grades.
	path('grade_book/biology_grades', views.biology_grades, name='biology_grades'),
	# Page accessing assignment grades.
	path('grade_book/class_grades/', views.class_grades, name='class_grades'),
	# Page for submitting homework.
	path('assignment_submission/', views.assignment_submission, name='assignment_submission'),
]