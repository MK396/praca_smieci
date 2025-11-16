from django.shortcuts import render

def main_page_games(request):
    return render(request, 'main_page_games.html')