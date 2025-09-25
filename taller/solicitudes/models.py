from django.db import models

class Solicitud(models.Model):
    TIPO_SOLICITUD_CHOICES = [
        ("academica", "Académica"),
        ("administrativa", "Administrativa"),
        ("tecnica", "Técnica"),
        ("otra", "Otra"),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    telefono_contacto = models.BigIntegerField()
    tipo_solicitud = models.CharField(max_length=20, choices=TIPO_SOLICITUD_CHOICES)
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to="adjuntos/", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"
    
created_at = models.DateTimeField(auto_now_add=True)
