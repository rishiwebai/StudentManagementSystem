from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'phone',
            'course',
            'age',
            'address',
        ]

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if len(name) < 3:
            raise forms.ValidationError(
                'Name must be at least 3 characters long.'
            )

        return name

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(phone) != 9:
            raise forms.ValidationError(
                'Phone number must be exactly 9 digits.'
            )

        return phone

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 5 or age > 100:
            raise forms.ValidationError(
                'Age must be between 5 and 100.'
            )

        return age