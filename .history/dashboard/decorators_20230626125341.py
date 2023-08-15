from django.http import HttpResponse
from django.shortcuts import redirect


# Only unauthenticated users can access the login/register page
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


# Check groups and figure out whether or not a user is allowed to access a page
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
                # todo: redirect user to log-page, and render a message that tells the user they are not authorized
        return wrapper_func
    return decorator

def return_user(): 
    def wrapper_func(request, *args, **kwargs): 
        return request.user
    return wrapper_func 
