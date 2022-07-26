from django.contrib import admin
from .models import Attendance,StudentExtra,TeacherExtra,Notice,PhcExtra,PanchayathsecretaryExtra
from .models import covidcase,covidoutbreaks,futurecovid
# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

class PhcAdmin(admin.ModelAdmin):
    pass
admin.site.register(PhcExtra, PhcAdmin)

class PanchayathsecretaryAdmin(admin.ModelAdmin):
    pass
admin.site.register(PanchayathsecretaryExtra, PanchayathsecretaryAdmin)



admin.site.register(covidcase)
admin.site.register(covidoutbreaks)
admin.site.register(futurecovid)