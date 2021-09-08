from django.db import models

from dataclasses import dataclass

from account.models import *

__all__ = (
    "Time",
    "TimeRange",
    "Days",
    "ReservationTarget",
    "ReservationDefault",
    "Reservation")


@dataclass
class Time:
    """Represents a time in the day, timezone agnostic."""

    hours: int
    minutes: int

    def serialize(self) -> int:
        return self.hours * 60 + self.minutes

    def deserialize(self, value: int) -> "Time":
        return Time(value // 60, value % 60)


@dataclass
class TimeRange:
    """Inclusive range of times."""

    start: Time
    duration: int


class Days(models.IntegerChoices):
    """Day enum."""

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class ReservationTarget(models.Model):
    """Gym, pool, tennis court, etc."""

    uid = models.CharField(max_length=50)


class ReservationDefault(models.Model):
    """Used if there is no custom reservation."""

    target = models.ForeignKey(to=ReservationTarget, on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(choices=Days.choices)
    slot = models.PositiveSmallIntegerField()


class Reservation(models.Model):
    """A custom reservation time."""

    target = models.ForeignKey(to=ReservationTarget, on_delete=models.CASCADE)
    date = models.DateField()
    slot = models.PositiveSmallIntegerField()
    booked = models.BooleanField(default=False)
