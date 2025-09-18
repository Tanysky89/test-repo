import requests


class yougileApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    #Получить токен авторизации
    def get_AuthToken(self, login, password, companyId): 
        payload = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.url + '/api-v2/auth/keys/get', json=payload, headers=headers)
        res = response.json()
        key_auth = res[0]["key"]
        return key_auth

    # Получить список проектов
    def get_project_list(self, login, password, companyId):

        my_key = self.get_AuthToken(login=login, password=password, companyId=companyId)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_key
        }
        response = requests.get(self.url + '/api-v2/projects', headers=headers)
        result = response.json()["content"]
        return result

    #Получить случайный список пользователей по одному из проектов компании
    def get_random_users(self, login, password, companyId):
        project_list = self.get_project_list(login=login, password=password, companyId=companyId)
        random_users = project_list[0]["users"]
        return random_users

    # добавляем новый проект и получаем его айди
    def create_project(self, title, users, login, password, companyID):
        my_token = self.get_AuthToken(login=login, password=password, companyId=companyID)
        random_users = self.get_random_users(login=login, password=password, companyId=companyID)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        payload = {
            "title": title,
            "users": random_users,
        }
        response = requests.post(self.url + '/api-v2/projects', json=payload, headers=headers)
        res = response.json()['id']
        return res
    
    #изменение проекта
    def editing_project(self, title, users, login, password, companyID, project_id, deleted):
        my_token = self.get_AuthToken(login=login, password=password, companyId=companyID)
        random_users = self.get_random_users(login=login, password=password, companyId=companyID)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        payload = {
            "title": title,
            "users": random_users,
            "deleted": deleted
        }
        response = requests.put(self.url + '/api-v2/projects/' + project_id, json=payload, headers=headers)
        res = response.json()
        return res
    
    #получение проекта по ID
    def get_project(self, login, password, companyId, project_id):

        my_key = self.get_AuthToken(login=login, password=password, companyId=companyId)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_key
        }
        response = requests.get(self.url + '/api-v2/projects/'+ project_id, headers=headers)
        responce_data = response.json()
        if 'title' in responce_data:
            result_title = responce_data['title']
            result_id = responce_data['id']
            result_deleted = responce_data['deleted']
            res = {
                "title": result_title,
                "id": result_id,
                "deleted": result_deleted
            }
            return res
        else:
            raise ValueError("Проект не найден")