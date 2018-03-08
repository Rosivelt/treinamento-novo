#-*- coding: utf-8 -*-

class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def __init__(self, *args, **kwargs):
        super(Child,self).__init__(*args, **kwargs)

    def override(self):
        super(Child,self).override()
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()

