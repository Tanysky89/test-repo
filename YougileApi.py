import requests


class yougileApi:
    # Инициализация
    def __init__(self, url, login, password, companyId) -> None:
        self.url = url
        self.login = login
        self.password = password
        self.companyId = companyId
        self.auth_token = self.get_AuthToken(login=self.login, password=self.password,companyId=self.companyId)
        
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
        key_auth = res[-1]["key"]
        return key_auth

    # Получить список проектов
    def get_project_list(self):

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.auth_token
        }
        response = requests.get(self.url + '/api-v2/projects', headers=headers)
        result = response.json()["content"]
        return result

    #Получить случайный список пользователей по одному из проектов компании
    def get_random_users(self):
        project_list = self.get_project_list()
        random_users = project_list[0]["users"]
        return random_users

    # добавляем новый проект и получаем его айди
    def create_project(self, title, users):
        #random_users = self.get_random_users(login=login, password=password, companyId=companyID)
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.auth_token
        }
        payload = {
            "title": title,
            "users": users,
        }
        response = requests.post(self.url + '/api-v2/projects', json=payload, headers=headers)
        try:
            res = response.json()['id']
            return res
        except:
            res = response.json()["message"]
            raise ValueError(res[0])
            
    
    #изменение проекта
    def editing_project(self, title, users, project_id, deleted):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.auth_token
        }
        payload = {
            "title": title,
            "users": users,
            "deleted": deleted
        }
        response = requests.put(self.url + '/api-v2/projects/' + project_id, json=payload, headers=headers)
        res = response.json()
        return res
    
    #получение проекта по ID
    def get_project(self, project_id):

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.auth_token
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
            res = response.json()["message"]
            raise ValueError(res)
            #raise ValueError("Проект не найден")

    #Очистить список проектов
    def delete_projects(self, count_to_delete):
        prj_list = self.get_project_list()
        counter = 0
        for prj in prj_list:
            if counter <= count_to_delete:
                self.editing_project(title=prj["title"], users=prj["users"], project_id=prj["id"], deleted=True)
                counter = counter + 1
   