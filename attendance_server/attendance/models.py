from django.db import models

class AttendanceRecord(models.Model):
    image = models.ImageField(upload_to='attendance_images/')
    # Add other fields as needed

    def __str__(self):
        return f"Record {self.id}"