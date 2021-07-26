from django.db import models

NAME_PREFIXES = {
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
}


class Profile(models.Model):  # uppercase 'profile' == the CLASS; lowercase 'profile' == an INSTANCE/OBJECT of the class
    namePrefixes = models.CharField(
        max_length=4, default="", choices=NAME_PREFIXES)
    firstName = models.CharField(
        max_length=60, default="", blank=False, null=False)  # 'blank' = form / 'null' = db
    lastName = models.CharField(
        max_length=60, default="", blank=False, null=False)
    email = models.EmailField(
        max_length=120, default="", blank=False, null=False)
    userName = models.CharField(
        max_length=60, default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):  # invokes python's builtin 'string' dunder method (returns a string representation of an object, instead of just the object's class)
        return "{} {}".format(self.firstName, self.lastName)
