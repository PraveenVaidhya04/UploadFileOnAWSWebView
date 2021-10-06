from django.db import models
import uuid
from django.utils.translation import ugettext_lazy
from autoslug import AutoSlugField
import django
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save


class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(ugettext_lazy('Title'), max_length=100, db_column="title")
    slug = AutoSlugField(populate_from='title', always_update=True, unique_with='created_at__month', db_column="slug",
                         null=True, blank=True)
    file = models.FileField()
    url = models.CharField(ugettext_lazy('Post Url'), max_length=100, null=True, blank=True, db_column="url")
    status = models.BooleanField(ugettext_lazy('Status'), default=True, db_column="status")
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts_user")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Posts'
        db_table = 'Posts'


def post_save_create_url(sender, instance, *args, **kwargs):
    if not instance.url:
        instance.url = settings.BASE_URL + 'posts/view-posts/' + str(instance.id)


post_save.connect(post_save_create_url, sender=Posts)