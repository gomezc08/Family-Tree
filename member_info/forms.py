# member_info/forms.py
from django import forms
from common.models import Person

class MemberInfoForm(forms.ModelForm):
    FirstName = forms.CharField(label='First Name', max_length=40)
    LastName = forms.CharField(label='Last Name', max_length=40)
    Birthday = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={'type': 'date'}))
    Nickname = forms.CharField(label='Nickname', max_length=40, required=False)
    YearDied = forms.IntegerField(label='Year Died', required=False)
    Pronouns = forms.CharField(label='Pronouns', max_length=20, required=False)
    Email = forms.EmailField(label='Email', max_length=100, required=False)
    Cell = forms.CharField(label='Cell', max_length=20, required=False)
    CityBorn = forms.CharField(label='City Born', max_length=30, required=False)
    StateBorn = forms.CharField(label='State Born', max_length=30, required=False)
    CountryBorn = forms.CharField(label='Country Born', max_length=30, required=False)
    CityCurrent = forms.CharField(label='City Current', max_length=30, required=False)
    StateCurrent = forms.CharField(label='State Current', max_length=30, required=False)
    CountryCurrent = forms.CharField(label='Country Current', max_length=30, required=False)
    Photo = forms.ImageField(label='Photo', required=False)
    Parent = forms.ModelChoiceField(queryset=Person.objects.all(), label='Parent', required=False, empty_label="Select Parent")
    Sibiling = forms.ModelChoiceField(queryset=Person.objects.all(), label='Sibiling', required=False, empty_label="Select Sibiling")
    Children = forms.ModelChoiceField(queryset=Person.objects.all(), label='Children', required=False, empty_label="Select Children")


    class Meta:
        model = Person
        fields = '__all__'  # Ensures all fields are included; adjust if some fields should not be on the form

    def __init__(self, *args, **kwargs):
        super(MemberInfoForm, self).__init__(*args, **kwargs)
        self.fields['Parent'].queryset = Person.objects.all()
