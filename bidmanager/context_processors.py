from django.template import Context

def user(request):
    user = request.user if request.user.is_authenticated() else None    
    return {'user2': 'teststst', }