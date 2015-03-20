# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'



from quiz.quiz import Quiz

Q = Quiz('BFI48')

for qid, q in Q.questions.iteritems():
    print q.qid, q.title, q.tag

# Create your models here.
