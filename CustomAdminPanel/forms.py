from django import forms

from CustomAdminPanel.models import Departments


class DateInput(forms.DateInput):
    input_type = "date"


class AddDoctorForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(label="Designation", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    department_list = []
    try:
        departments = Departments.objects.all()
        for department in departments:
            small_department = (department.id, department.department_name)
            department_list.append(small_department)
    except:
        department_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    department = forms.ChoiceField(label="Department", choices=department_list,
                                   widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    degree = forms.CharField(label="Degree", widget=forms.TextInput(attrs={"class": "form-control "}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


# class EditDoctorForm(forms.Form):
#     email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
#     first_name = forms.CharField(label="First Name", max_length=50,
#                                  widget=forms.TextInput(attrs={"class": "form-control"}))
#     last_name = forms.CharField(label="Last Name", max_length=50,
#                                 widget=forms.TextInput(attrs={"class": "form-control"}))
#     username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
#     address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
#
#     department_list = []
#     try:
#         departments = Departments.objects.all()
#         for department in departments:
#             small_department = (department.id, department.department_name)
#             department_list.append(small_department)
#     except:
#         department_list = []
#
#     gender_choice = (
#         ("Male", "Male"),
#         ("Female", "Female")
#     )
#
#     department = forms.ChoiceField(label="Department", choices=department_list,
#                                    widget=forms.Select(attrs={"class": "form-control"}))
#     sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
#     degree = forms.CharField(label="SDegre", widget=forms.TextInput(attrs={"class": "form-control "}))
#     profile_pic = forms.FileField(label="Profile Pic", max_length=50,
#                                   widget=forms.FileInput(attrs={"class": "form-control"}))
