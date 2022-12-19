
from django.db import models
# # from django.contrib.auth.models import User
# from django.conf import settings
# # from django.contrib.auth import get_user_model
from django.urls import reverse


class Jkks8(models.Model):
    """
    _summary_ Sealer line periodjkk

    """
    PERIOD = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
    )
    period_sel = models.CharField(
        max_length=4,
        choices=PERIOD,
        help_text='Period select')
    created = models.DateTimeField(auto_now_add=True)
    jkk_teammember = models.ForeignKey('teamMember', on_delete=models.SET_NULL, null=True)
    jkk_auditor = models.ForeignKey('teamLeader', on_delete=models.SET_NULL, null=True)
    periodadh = models.FloatField(null=True, blank=True)
    sumelemtime = models.FloatField(null=True, blank=True)
    # step_1 = models.CharField(max_length=300)
    # step_2 = models.CharField(max_length=300)
    # step_3= models.CharField(max_length=300)
    # step_4 = models.CharField(max_length=300)
    # step_5 = models.CharField(max_length=300)
    steptime_1 = models.FloatField(null=True, blank=True)
    steptime_2 = models.FloatField(null=True, blank=True)
    steptime_3 = models.FloatField(null=True, blank=True)
    steptime_4 = models.FloatField(null=True, blank=True)
    steptime_5 = models.FloatField(null=True, blank=True)
    steptime_6 = models.FloatField(null=True, blank=True)
    # steptime_7 = models.FloatField(null=True, blank=True)
    # steptime_8 = models.FloatField(null=True, blank=True)
    # steptime_9 = models.FloatField(null=True, blank=True)
    # steptime_10 = models.FloatField(null=True, blank=True)
    # steptime_11 = models.FloatField(null=True, blank=True)
    # steptime_12 = models.FloatField(null=True, blank=True)
    # steptime_13 = models.FloatField(null=True, blank=True)
    # steptime_14 = models.FloatField(null=True, blank=True)
    # steptime_15 = models.FloatField(null=True, blank=True)
    # steptol_1 = models.FloatField(null=True, blank=True)
    # steptol_2 = models.FloatField(null=True, blank=True)
    # steptol_3 = models.FloatField(null=True, blank=True)
    # steptol_4 = models.FloatField(null=True, blank=True)
    # steptol_5 = models.FloatField(null=True, blank=True)
    checkstatus_1 = models.BooleanField(null=True)
    checkstatus_2 = models.BooleanField(null=True)
    checkstatus_3 = models.BooleanField(null=True)
    checkstatus_4 = models.BooleanField(null=True)
    checkstatus_5 = models.BooleanField(null=True)
    checkstatus_6 = models.BooleanField(null=True)
    # checkstatus_7 = models.BooleanField(null=True)
    # checkstatus_8 = models.BooleanField(null=True)
    # checkstatus_9 = models.BooleanField(null=True)
    # checkstatus_10 = models.BooleanField(null=True)
    # checkstatus_11 = models.BooleanField(null=True)
    # checkstatus_12 = models.BooleanField(null=True)
    # checkstatus_13 = models.BooleanField(null=True)
    # checkstatus_14 = models.BooleanField(null=True)
    # checkstatus_15 = models.BooleanField(null=True)
    step_number = models.IntegerField(null=True)
    comment = models.CharField(max_length=200, null=True)


    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('jkks8')

    def __str__(self):
            """String for representing the Model object."""
            return "JKK S8 Created on " + self.created.strftime("%m/%d/%Y, %H:%M:%S")


class teamMember(models.Model):
    """
    _summary_ Sealer 
    """
    employeeid = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class teamLeader(models.Model):
    """
    _summary_ Sealer 

    """
    employeeid = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    def __str__(self):
        """String for representing the Model object."""
        return self.name



# class Process(models.Model):

#     """
#     _summary_ Sealer line Process with Elements as Foreng keys

#     """
#     PROCESS = (
#         ('S1', 'S1'),
#         ('S2', 'S2'),
#         ('S3', 'S3'),
#         ('S4', 'S4'),
#         ('S5', 'S5'),
#         ('S6', 'S6'),
#         ('S7', 'S7'),
#         ('S8', 'S8'),
#         ('S9', 'S9'),
#         ('S10', 'S10'),
#         ('S11', 'S11'),
#         ('S12', 'S12'),
#         ('RSCS', 'RSCS'),
#         ('LSCS', 'LSCS'),
#     )
#     name = models.CharField(
#         max_length=4,
#         choices=PROCESS,
#         help_text='Sealer Process list')
#     # elements= models.ForeignKey('elements', on_delete=models.SET_NULL, null=False)
#     def __str__(self):
#         """String for representing the Model object."""
#         return self.name

class s8elements(models.Model):
    """
    _summary_ Sealer s8 jjk line Elements

    """
    
    step = models.CharField(max_length=2)
    mayor_element = models.CharField(max_length=300, null= False)
    keypoint = models.CharField(max_length=300)
    worktime = models.FloatField()
    walktime = models.FloatField()
    tolerance = models.FloatField()
    
    def __str__(self):
        """String for representing the Model object."""
        return self.mayor_element


# class stopwatch(models.Model):
#     """
#     _summary_ Sealer line Elements

#     """
#     element= models.CharField(max_length=300, null= False)
#     timeelement = models.CharField(max_length=300, null= True)

# # class jkkDay(models.Model):
# #     """
# #     Table to add new daily jkks with created date, process and finalAdherence


# #     """
# #     created = models.DateField(auto_now_add=True)
# #     process = models.ForeignKey('Process', on_delete=models.SET_NULL, null=False)
# #     adherence = models.FloatField(null=True)  


# class Jkk(models.Model):
#     """
#     _summary_ Sealer line day jkk

#     """
    
#     created = models.DateTimeField(auto_now_add=True)
#     dailyprocess = models.ForeignKey('Process', on_delete=models.CASCADE, null=False)
#     dayadh = models.FloatField(null=True)

#     # def get_absolute_url(self):
#     #     return reverse('jkk', kwargs={"pk": self.pk})
    
#     def __str__(self):
#         """String for representing the Model object."""
#         return self.dailyprocess.name

    
#     auditor= models.ForeignKey('teamMember', on_delete=models.SET_NULL, null=False)
#     teammember = models.ForeignKey('teamMember', on_delete=models.SET_NULL, null=False)
#     timerecord = models.FloatField()
#     JKK_STATUS = (
#         ('a', 'approved'),
#         ('r', 'reproves'),
#     )

#     status = models.CharField(
#         max_length=1,
#         choices=JKK_STATUS,
#         blank=True,
#         default='m',
#         help_text='element time check',
#     )


