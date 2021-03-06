import datetime
from django.db import models
from django.core.urlresolvers import reverse

class Paste(models.Model):
    SYNTAX_CHOICES = (
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    )

    content = models.TextField()
    title = models.CharField(blank=True, max_length=30)
    syntax = models.IntegerField(choices=SYNTAX_CHOICES, default=0)
    poster = models.CharField(blank=True, max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return "%s (%s)" % (self.title or "#%s" % self.id, self.get_syntax_display())

    def get_absolute_url(self):
        return reverse('object_detail', kwargs={'object_id':self.id})

