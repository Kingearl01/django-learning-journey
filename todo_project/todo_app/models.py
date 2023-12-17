from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
