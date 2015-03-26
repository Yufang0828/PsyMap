from django.contrib.admin import ModelAdmin, site

from PsyMap.models.quiz import *


class QuizAdmin(ModelAdmin):
    fields = Quiz.__slots__[1:]
site.register(Quiz, QuizAdmin)


class QGroupAdmin(ModelAdmin):
    fields = QGroup.__slots__[1:]
site.register(QGroup, QGroupAdmin)


class QGroupQuizAdmin(ModelAdmin):
    fields = QGroupQuiz.__slots__[1:]
site.register(QGroupQuiz, QGroupQuizAdmin)


class ExperimentAdmin(ModelAdmin):
    fields = Experiment.__slots__[1:]
site.register(Experiment, ExperimentAdmin)


class UserFillQuizAdmin(ModelAdmin):
    fields = UserFillQuiz.__slots__[1:]
site.register(UserFillQuiz, UserFillQuizAdmin)