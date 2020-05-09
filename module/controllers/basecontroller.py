from rest_framework.views import APIView


class BaseController(APIView):
    def get(self, request):
        raise NotImplementedError

    def post(self, request):
        raise NotImplementedError
