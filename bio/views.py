from django.shortcuts import render, get_object_or_404
from .models import Person, Household, Spouse, Interests

def get_member_info(request, person_id):
    # Step 1: Retrieve person information
    person = get_object_or_404(Person, id=person_id)

    # Step 2: Retrieve household relationships
    households = Household.objects.filter(parents=person) | Household.objects.filter(child=person)

    # Step 3: Retrieve spouse relationships
    spouse_relationships = Spouse.objects.filter(spouse1=person) | Spouse.objects.filter(spouse2=person)

    # Step 4: Retrieve interests
    interests = Interests.objects.filter(person=person)

    context = {
        'person': person,
        'households': households,
        'spouse_relationships': spouse_relationships,
        'interests': interests,
    }

    return render(request, 'bio/member_info.html', context)
