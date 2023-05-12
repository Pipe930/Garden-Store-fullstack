from django.db import models
from os.path import join
import uuid
from datetime import datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Category Model
class Category(models.Model):

    # Atributtes
    name_category = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True, null=True, default="(Without description)")

    class Meta:

        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name_category',]

    def __str__(self) -> str:
        return self.name_category

# Category Model
class Offer(models.Model):

    # Atributtes
    name_offer = models.CharField(max_length=100, unique=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    discount = models.PositiveSmallIntegerField(default=0)

    class Meta:

        db_table = 'offers'
        verbose_name = 'offer'
        verbose_name_plural = 'offers'
        ordering = ['start_date',]

    def __str__(self) -> str:
        return self.name_offer

# Function to name images
def nameImage(request, name_image):
    old_name = name_image
    current_date = datetime.now().strftime('%Y%m%d%H:%M:%S')
    name_image = '%s%s' % (current_date, old_name)
    return join('images/', name_image)

class Product(models.Model):

    name_product = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to=nameImage)
    description = models.TextField(blank=True, null=True, default="(Without description)")
    slug = models.SlugField(unique=True)
    condition = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    id_offer = models.ForeignKey(Offer, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:

        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['name_product', 'create', 'price', 'stock']

    def __str__(self) -> str:
        return self.name_product

def set_slug(sender, instance, *args, **kwargs):
    if instance.slug:
        return

    id = str(uuid.uuid4())
    instance.slug= slugify('{}-{}'.format(
        instance.name_product, id[:8]
    ))

pre_save.connect(set_slug, sender = Product)
