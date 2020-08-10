from django.db import models
from account.models import Student, Tutor

class Topic(models.Model):
	"""A topic the user wants to note down."""
	text = models.CharField(max_length=200) # Set the number maximum of words to 200
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
	 	"""Return a string representation of the model."""	
	 	return self.text

class Entry(models.Model):
	"""Something you learned about regarding the topic."""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField() # Has no limit to the number of words
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		return f"{self.text[:50]}..."

class MathematicsAssignmentGrades(models.Model):
	"""The weekly Assignment grades to be recorderd."""
	math_mark = models.DecimalField(max_digits=5, decimal_places=2)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a decimal representation of the model."""
		return self,math_mark

class PhysicsAssignmentGrades(models.Model):
	"""The weekly Assignment grades to be recorderd."""
	physics_mark = models.DecimalField(max_digits=3, decimal_places=2)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a decimal representation of the model."""
		return self,math_mark

class ChemistryAssignmentGrades(models.Model):
	"""The weekly Assignment grades to be recorderd."""
	chemistry_mark = models.DecimalField(max_digits=3, decimal_places=2)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a decimal representation of the model."""
		return self,math_mark

class BiologyAssignmentGrades(models.Model):
	"""The weekly Assignment grades to be recorderd."""
	biology_mark = models.DecimalField(max_digits=3, decimal_places=2)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(Student, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a decimal representation of the model."""
		return self,math_mark