from django.db import models
from account.models import Account

class Topic(models.Model):
	"""A topic the user wants to note down."""
	text = models.CharField(max_length=200) # Set the number maximum of words to 200
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(Account, on_delete=models.CASCADE)

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