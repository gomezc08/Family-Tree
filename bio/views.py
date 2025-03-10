from django.shortcuts import render, get_object_or_404
from .models import Person, Household, Spouse, Interests
from django.db.models import Q


def get_member_info(request, PersonID):
    person = get_object_or_404(Person, Id=PersonID)

    # Retrieve spouse relationships
    spouse_relationships = Spouse.objects.filter(Spouse1ID=person) | Spouse.objects.filter(Spouse2ID=person)
    
    # Retrieve parent relationships
    parents = Person.objects.filter(
        Q(parent1_relationships__ChildID=person) | Q(parent2_relationships__ChildID=person)
    )


    # Retrieve child relationships
    children = Person.objects.filter(
        Q(child_relationships__Parent1ID=person) | Q(child_relationships__Parent2ID=person)
    )

    siblings = Person.objects.filter(
        Q(child_relationships__Parent1ID__in=parents) | Q(child_relationships__Parent2ID__in=parents)
    ).exclude(Id=PersonID).distinct()
    
    # Retrieve interests
    interests = Interests.objects.filter(PersonID=person)

    context = {
        'person': person,
        'spouse_relationships': spouse_relationships,
        'parents': parents,
        'children': children,
        'interests': interests,
        'siblings': siblings,
    }
    return render(request, 'bio/member_info.html', context)
