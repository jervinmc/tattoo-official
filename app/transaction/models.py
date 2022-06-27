from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Transaction(models.Model):
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    artist_id=models.CharField(_('artist_id'),max_length=255,blank=True,null=True)
    design_id =models.CharField(_('design_id'),max_length=255,blank=True,null=True)
    image=models.CharField(_('image'),max_length=255,blank=True,null=True)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    allergy=models.CharField(_('allergy'),max_length=255,blank=True,null=True)
    estimated_time=models.CharField(_('estimated_time'),max_length=255,blank=True,null=True)
    transaction_date=models.DateTimeField(_('transaction_date'), default=timezone.now)
    paymentImage = models.ImageField(
        _('paymentImage'), upload_to=nameFile, default="uploads/Cases.png")
    class Meta:
        ordering = ["-id"]
