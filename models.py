from django.db import models
from django.forms import ModelForm

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

SPEED=(
    (float(1),'m/s'),
    (float(5/18),'km/hr')
)
TIME=(
    (float(1),'s'),
    (float(60),'min'),
    (float(3600),'hr')
)
ACCEL=(
    (float(1),'m/s²'),
    (0.27777777777778,'km/hr²')
)

class Question(models.Model):
    u=models.DecimalField(max_digits=5,decimal_places=2)
    Uunit=models.FloatField(max_length=3, choices=SPEED)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    Tunit=models.FloatField(max_length=3, choices=TIME)
    a=models.DecimalField(max_digits=5,decimal_places=2)
    Aunit=models.FloatField(max_length=3, choices=ACCEL)
    #unit=
class InputForm(ModelForm):
    class Meta:
        model=Question
        fields = ['u','Uunit','t','Tunit','a','Aunit']

TIME=(
    (float(0.001),'ms'),
    (float(1),'s'),
    (float(60),'min'),
    (float(3600),'hr')
)
CHARGE=(
    (float(1),'C'),
    (float(1000),'KC')
)

class Question2(models.Model):
    q=models.DecimalField(max_digits=5,decimal_places=2)
    Qunit=models.FloatField(max_length=10, choices=CHARGE)
    t=models.DecimalField(max_digits=5,decimal_places=2)
    Tunit=models.FloatField(max_length=10, choices=TIME)
#i=Q/t
class InputForm2(ModelForm):
    class Meta:
        model=Question2
        fields = "__all__"        

ACCEL=(
    (float(1),'m/s²'),
    (0.27777777777778,'km/hr²')
)
SPEED=(
    (float(1),'m/s'),
    (float(5/18),'km/hr')
)
DISP=(
    (float(1),'m'),
    (float(1000),'km'),
    (0.01,'cm')
)

class Question3(models.Model):    
    u=models.DecimalField(max_digits=5,decimal_places=2)
    Uunit=models.FloatField(max_length=3, choices=SPEED)
    a=models.DecimalField(max_digits=5,decimal_places=2)
    Aunit=models.FloatField(max_length=3, choices=ACCEL)
    s=models.DecimalField(max_digits=5,decimal_places=2)
    Sunit=models.FloatField(choices=DISP)
class InputForm3(ModelForm):
    class Meta:
        model=Question3
        fields = "__all__"  

MASS=(
    (float(1),'kg'),
    (float(100),'tonne'),
    (float(.001),'g')
)

DISP=(
    (float(1),'m'),
    (float(1000),'km'),
    (float(0.01),'cm')
)

class Question4(models.Model):
    m=models.DecimalField(max_digits=5,decimal_places=2)
    Munit=models.FloatField(max_length=7, choices=MASS)
    r=models.DecimalField(max_digits=5,decimal_places=2)
    Runit=models.FloatField(max_length=7, choices=DISP)
#v= sqrt(2*G*m/r)
class InputForm4(ModelForm):
    class Meta:
        model=Question4
        fields = "__all__"

ACCEL=(
    (float(1),'m/s²'),
    (0.27777777777778,'km/hr²')
)

MASS=(
    (float(1),'kg'),
    (float(100),'tonne'),
    (float(.001),'g')
)
class Question5(models.Model):
    m=models.DecimalField(max_digits=5,decimal_places=2)
    Munit=models.FloatField(max_length=7, choices=MASS)
    a=models.DecimalField(max_digits=5,decimal_places=2)
    Aunit=models.FloatField(max_length=7, choices=ACCEL)
class InputForm5(ModelForm):
    class Meta:
        model=Question5
        fields = "__all__"

MASS=(
    (float(1),'kg'),
    (float(100),'tonne'),
    (float(.001),'g')
)

DISP=(
    (float(1),'m'),
    (float(1000),'km'),
    (float(0.01),'cm')
)
class Question6(models.Model):
    m1=models.DecimalField(max_digits=5,decimal_places=2)
    M1unit=models.FloatField(max_length=3, choices=MASS)
    m2=models.DecimalField(max_digits=5,decimal_places=2)
    M2unit=models.FloatField(max_length=3, choices=MASS)
    r=models.DecimalField(max_digits=5,decimal_places=2)
    Runit=models.FloatField(max_length=3, choices=DISP)
#Fg=-Gm1m2/(r^2)
class InputForm6(ModelForm):
    class Meta:
        model=Question6
        fields = "__all__"   

MASS=(
    (float(1),'kg'),
    (float(100),'tonne'),
    (float(.001),'g')
)

DISP=(
    (float(1),'m'),
    (float(1000),'km'),
    (float(0.01),'cm')
)

class Question7(models.Model):
    m=models.DecimalField(max_digits=7,decimal_places=2)
    Munit=models.FloatField(max_length=7, choices=MASS)
    r=models.DecimalField(max_digits=7,decimal_places=2)
    Runit=models.FloatField(max_length=7, choices=DISP)
#g=-Gm/r^2
class InputForm7(ModelForm):
    class Meta:
        model=Question7
        fields = "__all__"   

MASS = (
    (1, 'g'),
    (1000, 'kg'),
)

VELOCITY = (
    (1, 'm/s'),
    (0.27777, 'km/h')
)

# Create your models here.

class Question8(models.Model):
    m=models.DecimalField(max_digits=5,decimal_places=2)
    munit=models.FloatField(max_length=10,choices=MASS)
    v=models.DecimalField(max_digits=5,decimal_places=2)
    vunit=models.FloatField(max_length=10,choices=VELOCITY)
#e=0.5mv^2
class InputForm8(ModelForm):
    class Meta:
        model=Question8
        fields = "__all__"      

MASS=(
    (float(1),'kg'),
    (float(100),'tonne'),
    (float(.001),'g')
)

DISP=(
    (float(1),'m'),
    (float(1000),'km'),
    (float(0.01),'cm')
)

class Question9(models.Model):
    m=models.DecimalField(max_digits=5,decimal_places=2)
    Munit=models.FloatField(max_length=10, choices=MASS)
    h=models.DecimalField(max_digits=5,decimal_places=2)
    Hunit=models.FloatField(max_length=10, choices=DISP)
#e=mgh
class InputForm9(ModelForm):
    class Meta:
        model=Question9
        fields = "__all__"     

