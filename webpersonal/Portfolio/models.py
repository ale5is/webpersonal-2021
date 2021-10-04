from django.db.models import Model, CharField, TextField, ImageField, URLField, DateTimeField

# Create your models here.

class Project(Model):
    title = CharField(verbose_name= 'Título', max_length=50)
    description = TextField(verbose_name= 'Descripción')
    img = ImageField(verbose_name= 'Imagen', upload_to='project')
    link = URLField(null=True, blank=True, verbose_name= 'Enlace')
    created = DateTimeField(auto_now_add=True, verbose_name= 'Fecha de creación')
    updated = DateTimeField(auto_now=True, verbose_name= 'Fecha de modificación')

    class Meta:
        verbose_name = 'Projecto'
        verbose_name_plural = 'Projectos'
        ordering = ["created"]
    
    def __str__(self) -> str:
        return self.title