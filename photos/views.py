from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.
def gallery(request):
    category = request.GET.get('category')# getting category field from form
    # print("category: ", category)
    if category == None:
        photos = Photo.objects.all() # getting all photos from database
    else:
        photos = Photo.objects.filter(category__name = category) # getting filtered photos based on category from database

    catagories = Category.objects.all() # getting objects list from database
    
    context = {'catagories': catagories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def add_photo(request):
    catagories = Category.objects.all() # getting objects list from database

    if request.method == 'POST':
        data = request.POST            # getting data from form
        image = request.FILES.get('image') # getting image from form

        if data['category'] != 'none':   # if category is selected in form
            category = Category.objects.get(id=data['category']) # getting id of that category from database
        elif data['category_new'] != '': # if new category is created in form
            category, created = Category.objects.get_or_create(name=data['category_new']) #The method returns a tuple where the first element is the retrieved or created category object, and the second element is a boolean indicating whether the category was newly created. thats why we use multiple assgiment category for object, created for boolen
        else:  #if not category is selected or created in form                                                                         #get_or_create method gets object or create object it does not exist in database
            category = None

        photo = Photo.objects.create(  # creates a object in database to store photo with fallowing attributes
            category = category,
            description = data['description'],
            image = image,
        )

        return redirect('gallery') # after succession of adding photo in to database we redirected to gallery page automatically
        
        # print("data:", data)   # these are just testing Purpose
        # print("image:", image)
    context = {'catagories': catagories}
    return render(request, 'photos/add_photo.html', context)

def view_photo(request, pk):
    photo = Photo.objects.get(id=pk) # getting photo from database based on primary key provided via link when button is clicked. 
    return render(request, 'photos/view_photo.html', {'photo': photo})