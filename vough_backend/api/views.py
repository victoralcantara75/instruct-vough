from rest_framework import viewsets, status
from rest_framework.views import Response

from api import models, serializers
from api.integrations.github import GithubApi
import json
# TODOS:
# 1 - Buscar organização pelo login através da API do Github
# 2 - Armazenar os dados atualizados da organização no banco
# 3 - Retornar corretamente os dados da organização
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = models.Organization.objects.all().order_by('-score')
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"

    def retrieve(self, request, login=None):

        api = GithubApi()

        try:
            org = models.Organization.objects.get(login=login)
        except:
            org = api.get_organization(login)
            model = models.Organization(login=login, name=org.get('name'), score=org.get('score'))
            model.save()
            return Response(org)

        org_serialized = self.serializer_class(org)
        return Response(org_serialized.data)
