from django.contrib import admin

from . import models


admin.site.register(models.ReservationTarget)
admin.site.register(models.ReservationDefault)
admin.site.register(models.Reservation)
