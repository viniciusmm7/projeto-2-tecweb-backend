# from json import loads

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Game
from .serializers import GameSerializer

# def index(request):
#     from api_keys import RAWG_API_KEY, RAPID_API_KEY
#     page = 1
#     try:
#         while True:
#             url = f'https://rawg-video-games-database.p.rapidapi.com/games?key={RAWG_API_KEY}&page={page}'
#             page += 1

#             headers = {
#                 'X-RapidAPI-Key': RAPID_API_KEY,
#                 'X-RapidAPI-Host': 'rawg-video-games-database.p.rapidapi.com'
#             }

#             response = req('GET', url, headers=headers)
#             response_dict = loads(response.text)
#             results = response_dict['results']

#             for i in range(len(results)):
#                 rawgID = results[i]['id']
#                 slug = results[i]['slug']
#                 title = results[i]['name']
#                 rating = results[i]['rating']
#                 ratingQty = results[i]['ratings_count']
#                 game = Game(rawgID=rawgID, slug=slug, title=title, rating=rating, ratingQty=ratingQty)
#                 game.save()
        
#     except Exception as e:
#         print(e)


@api_view(['GET', 'POST'])
def api_games(request):
    if request.method == 'POST':
        new_game_data = request.data

        rawgID = new_game_data['rawgID']
        title = new_game_data['title']

        if not title:
            all_games = Game.objects.all()
            serialized_game = GameSerializer(all_games, many=True)
            return Response(serialized_game.data)

        dbData = [str(i) for i in Game.objects.all()]

        for object in dbData:
            if title in object:
                serialized_game = GameSerializer(Game.objects.all(), many=True)
                return Response(serialized_game.data)

        game = Game(rawgID=rawgID, title=title)
        game.save()

    all_games = Game.objects.all()
    serialized_game = GameSerializer(all_games, many=True)
    return Response(serialized_game.data)


@api_view(['GET', 'DELETE'])
def api_game(request, rawgID):
    if request.method == 'GET':
        try:
            game = Game.objects.get(rawgID=rawgID)
            serialized_game = GameSerializer(game)
            return Response(serialized_game.data)
        except Game.DoesNotExist:
            raise Http404()

    if request.method == 'DELETE':
        game = Game.objects.get(rawgID=rawgID)
        game.delete()