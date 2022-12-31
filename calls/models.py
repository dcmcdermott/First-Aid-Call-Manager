from django.db import models


class Responder(models.Model):

    CERTIFICATIONS = (
        ('EMT-B', 'EMT-B'),
        ('EMT-P', 'EMT-P'),
        ('LPN', 'LPN'),
        ('RN', 'RN')
    )
    STATUS = (
        ('PT', 'PT'),
        ('PT-S', 'PT-S'),
        ('FT-S', 'FT-S')
    ) 
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    certification = models.CharField(max_length=200, null=True, choices=CERTIFICATIONS)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    license_scan = models.ImageField(null=True, blank=True)
    license_expiration = models.DateField(null=True, blank=True)
    cpr_scan = models.ImageField(null=True, blank=True)
    cpr_expiration = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.firstname


class Call(models.Model):

    CALL_TYPES = (
        ('A', 'A - ALLERGIC REACTION'),
        ('B', 'B - BITE/STING'),
        ('C', 'C - CARDIAC'),
        ('E', 'E - EXPOSURE'),
        ('F', 'F - FAINT'),
        ('G', 'G - GUEST ASSISTANCE'),
        ('H', 'H - HEAT RELATED'),
        ('I', 'I - ILLNESS'),
        ('R', 'R - RESPIRATORY'),
        ('T', 'T - TRAUMA'),
        ('U', 'U - UNKNOWN'),
        ('X', 'X - SEIZURE')
    )
    ZONES = (
        ('701', '701'),
        ('705', '705'),
        ('710', '710'),
        ('720', '720'),
        ('725', '725'),
        ('730', '730'),
        ('740', '740'),
        ('745', '745'),
    )
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    nature = models.CharField(max_length=100, null=True, choices=CALL_TYPES)
    responder = models.ForeignKey(Responder, on_delete=models.SET_NULL, null=True)
    red = models.BooleanField(default=False, blank=True, null=True)
    zone = models.CharField(max_length=100, choices=ZONES, default='701', null=True)
    location = models.CharField(max_length=100, null=True)
    caller = models.CharField(max_length=100,default="SECURITY", null=True)
    on_scene_time = models.TimeField(default=None, blank=True, null=True)
    upgrade_time = models.TimeField(default=None, blank=True, null=True)
    ems_on_scene_time = models.TimeField(default=None, blank=True, null=True)
    ems_clear_scene_time = models.TimeField(default=None, blank=True, null=True)
    cancel_time = models.TimeField(default=None, blank=True, null=True)

    def save(self):
        self.location = self.location.upper()
        super(Call, self).save()

    def __str__(self):
        return f"{self.id} -- {self.datetime.date()} -- {self.location} "



class Walkin(models.Model):
    DEPARTMENTS = (
        ('Culinary', 'Culinary'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Games', 'Games'),
        ('Grounds', 'Grounds'),
        ('Guest Relations', 'Guest Relations'),
        ('HR', 'HR'),
        ('Maintenance', 'Maintenance'),
        ('Merchandise', 'Merchandise'),
        ('Security', 'Security'),
        ('Traffic', 'Traffic'),
        ('Zoo', 'Zoo'),
    )
    datetime = models.DateTimeField(blank=True, auto_now_add=True, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, choices=DEPARTMENTS, null=True)
    reason = models.CharField(max_length=250, null=True)
    notes = models.TextField(max_length=500, blank=True, null=True)

    def save(self):
        self.firstname = self.firstname.upper()
        self.lastname = self.lastname.upper()
        super(Walkin, self).save()
    
    def __str__(self):
        return self.lastname


class Minor(models.Model):
    
    lastname = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    emp_id = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    consent_scan = models.ImageField(null=True, blank=True)

    def save(self):
        self.lastname = self.lastname.upper()
        self.firstname = self.firstname.upper()
        super(Minor, self).save()
    
    def __str__(self):
        return f"{self.lastname}, {self.firstname}"


class Schedule(models.Model):

    t_1 = models.CharField(blank=True, max_length=100, null=True)
    t_2 = models.CharField(blank=True, max_length=100, null=True)
    t_3 = models.CharField(blank=True, max_length=100, null=True)
    t_4 = models.CharField(blank=True, max_length=100, null=True)
    t_5 = models.CharField(blank=True, max_length=100, null=True)
    t_6 = models.CharField(blank=True, max_length=100, null=True)
    p5_1 = models.CharField(blank=True, max_length=100, null=True)
    p5_2 = models.CharField(blank=True, max_length=100, null=True)
    p5_3 = models.CharField(blank=True, max_length=100, null=True)
    p5_4 = models.CharField(blank=True, max_length=100, null=True)
    p5_5 = models.CharField(blank=True, max_length=100, null=True)
    p5_6 = models.CharField(blank=True, max_length=100, null=True)
    p10_1 = models.CharField(blank=True, max_length=100, null=True)
    p10_2 = models.CharField(blank=True, max_length=100, null=True)
    p10_3 = models.CharField(blank=True, max_length=100, null=True)
    p10_4 = models.CharField(blank=True, max_length=100, null=True)
    p10_5 = models.CharField(blank=True, max_length=100, null=True)
    p10_6 = models.CharField(blank=True, max_length=100, null=True)
    p20_1 = models.CharField(blank=True, max_length=100, null=True)
    p20_2 = models.CharField(blank=True, max_length=100, null=True)
    p20_3 = models.CharField(blank=True, max_length=100, null=True)
    p20_4 = models.CharField(blank=True, max_length=100, null=True)
    p20_5 = models.CharField(blank=True, max_length=100, null=True)
    p20_6 = models.CharField(blank=True, max_length=100, null=True)
    p30_1 = models.CharField(blank=True, max_length=100, null=True)
    p30_2 = models.CharField(blank=True, max_length=100, null=True)
    p30_3 = models.CharField(blank=True, max_length=100, null=True)
    p30_4 = models.CharField(blank=True, max_length=100, null=True)
    p30_5 = models.CharField(blank=True, max_length=100, null=True)
    p30_6 = models.CharField(blank=True, max_length=100, null=True)






