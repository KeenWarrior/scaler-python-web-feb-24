from dependency_injector.wiring import inject, Provide
from rest_framework.views import APIView
from rest_framework.response import Response
from logging import Logger


users = [{
        "id": 1,
        "name": "Ravi",
        "hobbies": ["Coding", "Dancing"]
    }, {
        "id": 2,
        "name": "Amit",
        "hobbies": ["Gliding", "Dancing"]
    }]


class UserGetView(APIView):

    @inject
    def get(
            self,
            request,
            user_id,
            logger: Logger = Provide["logger"]
    ):
        logger.info("We are asking for user {}".format(user_id))
        for user in users:
            if user.get("id") == user_id:
                return Response(user)

        return Response(status=404)
