from rest_framework.views import APIView
from ..databaseaction.databaseaction import DatabaseActions

class BaseController(APIView):
    _databaseObject = DatabaseActions()
    def get(self, request):
        raise NotImplementedError

    def post(self, request):
        raise NotImplementedError
