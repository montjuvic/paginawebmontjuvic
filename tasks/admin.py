from django.contrib import admin
from .models import Task

#ACA SE MODIFICA EL PANEL DE ADMINISTRADOR, SE PUEDEN AGREGAR MAS OPCIONES ETC.
# Register your models here.
class TaskAdmin(admin.ModelAdmin):

    readonly_fields = ("created", )




admin.site.register(Task, TaskAdmin) #ACA SE REGISTRAN, PASANDOSELO POR PARAMETRO
