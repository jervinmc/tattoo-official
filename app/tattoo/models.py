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


class Tattoo(models.Model):
    category=models.CharField(_('category'),max_length=255,blank=True,null=True)
    tattoo_name=models.CharField(_('tattoo_name'),max_length=255,blank=True,null=True)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    numAvail = models.IntegerField(_('numAvail'),default=0)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    description=models.CharField(_('description'),max_length=255,blank=True,null=True)
    colored=models.CharField(_('colored'),max_length=255,blank=True,null=True)
    time_estimation=models.CharField(_('time_estimation'),max_length=255,blank=True,null=True)
    image = models.ImageField(
        _('image'), upload_to=nameFile, default="uploads/Cases.png")
    class Meta:
        ordering = ["-id"]
