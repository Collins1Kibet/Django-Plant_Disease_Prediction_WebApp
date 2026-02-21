from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Image was Uploaded at', self.uploaded_at