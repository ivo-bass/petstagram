from django.shortcuts import render, redirect

from petstagram.pets.models import Pet, Like


def pet_all(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'pets/pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        "pet": pet,
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet
    )
    like.save()
    return redirect('pet detail', pet.id)