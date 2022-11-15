
from django.db import models
# # from django.contrib.auth.models import User
# from django.conf import settings
# # from django.contrib.auth import get_user_model
from django.urls import reverse




class teamMember(models.Model):
    """
    _summary_ Sealer 

    """
    employeeid = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class teamoff(models.Model):
    """
    _summary_ Sealer 

    """
    employeeid = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    def __str__(self):
        """String for representing the Model object."""
        return self.name



class dailyJkk(models.Model):
    """
    _summary_ Sealer line day jkk

    """
    
    created = models.DateTimeField(auto_now_add=True)
    dailyprocess = models.ForeignKey('Process', on_delete=models.CASCADE, null=False)
    dayadh = models.FloatField(null=True)

    def get_absolute_url(self):
        return reverse('periodjkk', kwargs={"pk": self.pk})
    
    # def __str__(self):
    #     """String for representing the Model object."""
    #     return self.dailyprocess

class periodJkk(models.Model):
    """
    _summary_ Sealer line periodjkk

    """
    
    created = models.DateTimeField(auto_now_add=True)
    jkk_dayly_process = models.ForeignKey('dailyJkk', on_delete=models.CASCADE, null=False)
    jkk_dayly_tm = models.ForeignKey('teamMember', on_delete=models.CASCADE, null=False)
    auditor = models.ForeignKey('teamoff', on_delete=models.CASCADE, null=False)
    periodadh = models.FloatField(null=True)



# class checkJkk(models.Model):
#     """
#     _summary_ Sealer line periodjkk

#     """
    
#     created = models.DateTimeField(auto_now_add=True)
#     periodjkkcheck = models.ForeignKey('dailyJkk', on_delete=models.CASCADE, null=False)
#     checkelements = models.ForeignKey('elements', on_delete=models.CASCADE, null=False)
#     timecheck = models.FloatField()
#     checkstatus = models.BooleanField(null=True)

    


    
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



class Process(models.Model):

    """
    _summary_ Sealer line Process with Elements as Foreng keys

    """
    PROCESS = (
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
        ('S8', 'S8'),
        ('S9', 'S9'),
        ('S10', 'S10'),
        ('S11', 'S11'),
        ('S12', 'S12'),
        ('RSCS', 'RSCS'),
        ('LSCS', 'LSCS'),
    )
    name = models.CharField(
        max_length=4,
        choices=PROCESS,
        help_text='Sealer Process list')
    # elements= models.ForeignKey('elements', on_delete=models.SET_NULL, null=False)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class elements(models.Model):
    """
    _summary_ Sealer line Elements

    """
    stepnumber = models.IntegerField(null = False)
    mayor_element= models.CharField(max_length=300, null= False)
    keypoint = models.CharField(max_length=300)
    worktime = models.IntegerField()
    walktime = models.IntegerField()
    tolerance = models.FloatField()
    process = models.ForeignKey('Process', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.mayor_element


class stopwatch(models.Model):
    """
    _summary_ Sealer line Elements

    """
    element= models.CharField(max_length=300, null= False)
    timeelement = models.CharField(max_length=300, null= True)

# class jkkDay(models.Model):
#     """
#     Table to add new daily jkks with created date, process and finalAdherence


#     """
#     created = models.DateField(auto_now_add=True)
#     process = models.ForeignKey('Process', on_delete=models.SET_NULL, null=False)
#     adherence = models.FloatField(null=True)  

