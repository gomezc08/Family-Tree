from django.shortcuts import render, get_object_or_404
from .models import Person, Household, Spouse, Interests

def get_member_info(request, PersonID):
    person = get_object_or_404(Person, Id=PersonID)

    # Retrieve spouse relationships
    spouse_relationships = Spouse.objects.filter(Spouse1ID=PersonID) | Spouse.objects.filter(Spouse2ID=PersonID)

    # Retrieve households (parents or children)
    households = Household.objects.filter(ParentsID=PersonID) | Household.objects.filter(ChildID=PersonID)

    # Retrieve interests
    interests = Interests.objects.filter(PersonID=PersonID)

    context = {
        'person': person,
        'spouse_relationships': spouse_relationships,
        'households': households,
        'interests': interests,
    }
    return render(request, 'bio/member_info.html', context)

