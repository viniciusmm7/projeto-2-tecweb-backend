# from json import loads

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Game
from .serializers import GameSerializer


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