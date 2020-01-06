from django.core.files import File as File
from django.db import models

import ffmpy

import uuid


class FileInstance(models.Model):

    file = models.FileField(upload_to='upload_files')

    def __str__(self):
        return f'File № {self.pk}'

    def save(self, *args, **kwargs):

        if 'mp4' in self.file.name:

            if self.file.size / 1024 / 1024 > 2.5:

                file_name = uuid.uuid4()

                ff = ffmpy.FFmpeg(
                    inputs={
                        self.file.file.file.name: None
                    },
                    outputs={
                        f'upload_files/{file_name}.gif': None
                    }
                )
                ff.run()

                self.file = File(open(f'upload_files/{file_name}.gif', 'rb'), f'{file_name}.gif')

        else:

            self.file = File(open(f'upload_files/default.mp4', 'rb'), 'default.mp4')

        super().save(*args, **kwargs)
