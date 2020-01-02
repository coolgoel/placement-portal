from django.shortcuts import HttpResponse, reverse, redirect, render

# The Sign In Url to redirect to Outlook Login
from authentication.authhelper import get_signin_url

# Outlook gives us authorization code, we ask for a token from it
from authentication.authhelper import get_token_from_code

# The helper to get data from outlook like roll number, email, name
from authentication.outlookservice import get_me

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

def home(request):

  # Redirecting to gettoken view after authenticating
  redirect_uri = request.build_absolute_uri(
      reverse('authentication:gettoken'))

  # Building the sign in url
  sign_in_url = get_signin_url(redirect_uri)

  return redirect(sign_in_url)


# Add import statement to include new function

def gettoken(request):

  #################################
  # Set redirect after saving token
  redirect_url = None
  ################################


  # get Token from code
  auth_code = request.GET['code']
  redirect_uri = request.build_absolute_uri(reverse('authentication:gettoken'))
  token = get_token_from_code(auth_code, redirect_uri)
  access_token = token['access_token']

  # Save the token in session
  request.session['access_token'] = access_token

  # redirect_url = request.session.get('redirect_url', None)
  
  if redirect_url is None:

    #####################
    # Get user from token
    
    outUser = get_me(access_token)
    username = outUser['displayName']
    password = outUser['surname']
    email = outUser['mail']

    try:
      user = User.objects.get(username=username)
    except User.DoesNotExist:
      user = User.objects.create_user(username, email, password)
      user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect("home:charts")
   
  else: 
    return redirect(redirect_url)

def logout2(request):
  
  logout(request)
  return redirect("authentication:home")
# return HttpResponse("Token: %s<br>Name: %s<br>Roll Number: %s<br> Mail: %s" % (access_token, user['displayName'], user['surname'], user['mail']))