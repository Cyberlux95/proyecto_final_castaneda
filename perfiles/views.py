from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.




# esta funcion registra a los usuarios
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = {'form' : form}
	return render(request, 'twitter/register.html', context)


# esta funcion despliega el perfil del usuario

def profile(request, username):
	user = User.objects.get(username=username)
	posts = user.posts.all()
	context = {'user':user, 'posts':posts}
	return render(request, 'twitter/profile.html', context)




#esta funcion edita los perfiles
@login_required
def editar(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('home')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm()

	context = {'u_form' : u_form, 'p_form' : p_form}
	return render(request, 'twitter/editar.html', context)


# seccion aun no testeada


#_____________________________________________________________________________________________
# FOLLOW Y UNFOLLOW 
#@login_required
#def follow(request, username):
#	current_user = request.user
#	to_user = User.objects.get(username=username)
#	to_user_id = to_user
#	rel = Relationship(from_user=current_user, to_user=to_user_id)
#	rel.save()
#	return redirect('home')

#@login_required
#def unfollow(request, username):
#	current_user = request.user
#	to_user = User.objects.get(username=username)
#	to_user_id = to_user.id
#	rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user_id)
#	rel.delete()
#	return redirect('home')