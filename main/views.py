from django.shortcuts import render
import requests
from .movie_request import api_results

# Create your views here.
def home(request):
  popular_movies=api_results('popular')
  upcoming_movies=api_results('upcoming')
  current_movies=api_results('now_playing')
  context={"popular":popular_movies,"upcoming":upcoming_movies,"current_movies":current_movies}
  return render(request, 'main/index.html',context)
