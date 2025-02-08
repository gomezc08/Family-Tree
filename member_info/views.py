from django.shortcuts import render, redirect
from .forms import MemberInfoForm
from common.models import Person, Interests, Spouse, Household

def member_info_view(request):
    if request.method == 'POST':
        form = MemberInfoForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form instance to create or update the Person entry
            new_person = form.save()

            # Optionally handle relationships like children, siblings etc.
            # Here we assume that form.cleaned_data['Children'] and form.cleaned_data['Siblings']
            # are populated with the IDs of the children and siblings, respectively
            if 'Children' in form.cleaned_data and form.cleaned_data['Children']:
                for child_id in form.cleaned_data['Children']:
                    # Implement the logic to handle child relationships, depending on your model structure
                    Household.objects.create(Parent1ID=new_person, ChildID=child_id)
                    
            if 'Siblings' in form.cleaned_data and form.cleaned_data['Siblings']:
                for sibling_id in form.cleaned_data['Siblings']:
                    # Implement the logic to handle sibling relationships, depending on your model structure
                    Household.objects.create(Parent1ID=new_person, Parent2ID=sibling_id)
            
            if 'Parent' in form.cleaned_data and form.cleaned_data['Parent']:
                # Assume a model method or similar to create/update a household record
                Household.objects.create(Parent1ID=form.cleaned_data['Parent'], ChildID=new_person)
                    
            # Insert interests if any are provided
            if 'Interest' in form.cleaned_data and form.cleaned_data['Interest']:
                Interests.objects.create(PersonID=new_person, Interest=form.cleaned_data['Interest'])
            
            return redirect('form_success')
    else:
        form = MemberInfoForm()
    
    return render(request, 'member_info/index.html', {'form': form})

def form_success_view(request):
    return render(request, 'member_info/form_success.html')
