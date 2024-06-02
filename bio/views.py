from django.shortcuts import render, get_object_or_404
from .models import Person, Household, Spouse, Interests

def get_member_info(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    # Retrieve spouse relationships
    spouse_relationships = Spouse.objects.filter(spouse1=person) | Spouse.objects.filter(spouse2=person)

    # Retrieve households (parents or children)
    households = Household.objects.filter(parents=person) | Household.objects.filter(child=person)

    # Retrieve interests
    interests = Interests.objects.filter(person=person)

    context = {
        'person': person,
        'spouse_relationships': spouse_relationships,
        'households': households,
        'interests': interests,
    }

    return render(request, 'bio/member_info.html', context)
