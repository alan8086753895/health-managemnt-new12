from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

dos = [('first','first'),('second','second')]
vac = [('covishield','covishield'),('covaxin','covaxin'),('sputnik','sputnik')]
preg = [('yes','yes'),('no','no')]
classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=40,null=True)
    age=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
class Preganancy(models.Model):
    pregnancy=models.CharField(max_length=500)
class Kids(models.Model):
    kids=models.CharField(max_length=500)
class Vaccination(models.Model):
    vacctype = models.CharField(max_length=10,choices=vac,default='covishield')
    vaccdate = models.CharField(max_length=40,null=True)
    dose = models.CharField(max_length=10,choices=dos,default='first')

class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)

class PhcExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name


class PanchayathsecretaryExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40)
    message=models.CharField(max_length=500)




class covidcase(models.Model):
    date = models.DateField(max_length=200,null=True)
    #day = models.CharField(max_length=200,null=True)
    dis=(('Alappuzha','Alappuzha'),('Wayanad','Wayanad'),('Ernakulam','Ernakulam'),('Thrissur','Thrissur'),('Thiruvananthapuram','Thiruvananthapuram'),('Pathanamthitta','Pathanamthitta'),('Palakkad','Palakkad'),('Malappuram','Malappuram'),('Kozhikode','Kozhikode'),('Kottayam','Kottayam'),('Kollam','Kollam'),('Kasaragod','Kasaragod'),('Kannur','Kannur'),('Idukki','Idukki'))
    district = models.CharField(max_length=50,choices=dis)
    covidcases = models.CharField(max_length=40,null=True)
    numberofvaccination=models.CharField(max_length=40,null=True)
class covidoutbreaks(models.Model):
    date = models.DateField(max_length=200,null=True)
    #day = models.CharField(max_length=200,null=True)
    dis=(('Alappuzha','Alappuzha'),('Wayanad','Wayanad'),('Ernakulam','Ernakulam'),('Thrissur','Thrissur'),('Thiruvananthapuram','Thiruvananthapuram'),('Pathanamthitta','Pathanamthitta'),('Palakkad','Palakkad'),('Malappuram','Malappuram'),('Kozhikode','Kozhikode'),('Kottayam','Kottayam'),('Kollam','Kollam'),('Kasaragod','Kasaragod'),('Kannur','Kannur'),('Idukki','Idukki'))
    district = models.CharField(max_length=50,choices=dis)
    covidcases = models.CharField(max_length=40,null=True)

class futurecovid(models.Model):
    date = models.DateField(max_length=200,null=True)
    #day = models.CharField(max_length=200,null=True)
    dis=(('Alappuzha','Alappuzha'),('Wayanad','Wayanad'),('Ernakulam','Ernakulam'),('Thrissur','Thrissur'),('Thiruvananthapuram','Thiruvananthapuram'),('Pathanamthitta','Pathanamthitta'),('Palakkad','Palakkad'),('Malappuram','Malappuram'),('Kozhikode','Kozhikode'),('Kottayam','Kottayam'),('Kollam','Kollam'),('Kasaragod','Kasaragod'),('Kannur','Kannur'),('Idukki','Idukki'))
    district = models.CharField(max_length=50,choices=dis)
    covidcases = models.CharField(max_length=40,null=True)
   # numberofvaccination=models.CharField(max_length=40,null=True)
