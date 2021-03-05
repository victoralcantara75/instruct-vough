import os
import requests

class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):

        response = requests.get(self.API_URL + "/orgs/" + login)

        if response.staus_code == 403:
            return "Numero de requisições máximas alcançado!"

        org = response.json()
        public_members = self.get_organization_public_members(login)

        object = {
            'name': org.get("name"),
            'login': login,
            'score': public_members + org.get("public_repos")
        }

        return object

    def get_organization_public_members(self, login: str) -> int:

        response = requests.get(self.API_URL + "/orgs/" + login + "/public_members")
        members = response.json()

        return len(members)
