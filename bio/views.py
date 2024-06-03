from django.shortcuts import render, get_object_or_404
from .models import Person, Household, Spouse, Interests

def get_member_info(request, PersonID):
    person = get_object_or_404(Person, Id=PersonID)

    # Retrieve spouse relationships
    spouse_relationships = Spouse.objects.filter(Spouse1ID=person) | Spouse.objects.filter(Spouse2ID=person)

    # Retrieve parent relationships
    parents = Person.objects.filter(child_relationships__ChildID=person)

    # Retrieve child relationships
    children = Person.objects.filter(parent_relationships__ParentsID=person)

    # Retrieve interests
    interests = Interests.objects.filter(PersonID=person)

    context = {
        'person': person,
        'spouse_relationships': spouse_relationships,
        'parents': parents,
        'children': children,
        'interests': interests,
    }
    return render(request, 'bio/member_info.html', context)
