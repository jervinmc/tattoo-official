from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class User(models.Model):
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    firstname=models.CharField(_('firstname'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('lastname'),max_length=255,blank=True,null=True)
    account_type=models.CharField(_('account_type'),max_length=255,blank=True,null=True)
    password=models.CharField(_('password'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    allergy=models.CharField(_('allergy'),max_length=255,blank=True,null=True)
    gcash=models.CharField(_('gcash'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/Cases.png")
    class Meta:
        ordering = ["-id"]
