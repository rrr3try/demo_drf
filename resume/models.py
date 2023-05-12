from django.conf import settings
from django.db import models


class SpecialityChoices(models.TextChoices):
    backend = "backend", "Backend"
    frontend = "frontend", "Frontend"
    gamedev = "gamedev", "Gamedev"
    devops = "devops", "Devops"
    design = "design", "Design"


class Resume(models.Model):
    class StatusChoices(models.TextChoices):
        draft = "draft", "Черновик"
        published = "published", "Опубликовано"
        archived = "archived", "В архиве"

    class EducationChoices(models.TextChoices):
        school = "school", "Среднее"
        college = "college", "Средне-специальное"
        university = "university", "Высшее"

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="resumes")
    status = models.CharField(max_length=32, choices=StatusChoices.choices, default=StatusChoices.draft)
    grade = models.CharField(max_length=32, default="junior")
    specialty = models.CharField(max_length=32, choices=SpecialityChoices.choices)
    salary = models.IntegerField("зарплата \"от\"")
    experience = models.PositiveIntegerField("опыт работы в месяцах")
    education = models.CharField(max_length=32, choices=EducationChoices.choices)
    title = models.CharField(max_length=128)
    portfolio = models.TextField()
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
