from YougileApi import yougileApi

api = yougileApi("https://ru.yougile.com")


def test_positive_editing_project():
    login = ""
    password = ""
    companyId = "2e7b21df-b05c-4784-8a3e-d191134a21e0"

    #Добавляем новый проект
    random_users = api.get_random_users(login=login, password=password, companyId=companyId)
    new_project_id = api.create_project("My_new_test_project", random_users, login=login, password=password, companyID=companyId)

    #Изменяем созданный проект
    editing_project = api.editing_project("My_ed_test_project", random_users, login=login, password=password, companyID=companyId, project_id=new_project_id, deleted=False)

    #Получение объекта по ID
    project = api.get_project(login=login, password=password, companyId=companyId, project_id=new_project_id)
    assert project['title'] == "My_ed_test_project"
    assert project['id'] == new_project_id
  
  
def test_negative_editing_project():
    login = ""
    password = ""
    companyId = "2e7b21df-b05c-4784-8a3e-d191134a21e0"

    #Добавляем новый проект
    random_users = api.get_random_users(login=login, password=password, companyId=companyId)
    new_project_id = api.create_project("My_project", random_users, login=login, password=password, companyID=companyId)

    #Удаляем созданный проект
    editing_project = api.editing_project("My_project", random_users, login=login, password=password, companyID=companyId, project_id=new_project_id, deleted=True)

    #Получение удаленного объекта по ID
    project = api.get_project(login=login, password=password, companyId=companyId, project_id=new_project_id)
    assert project['deleted'] == False
    
    
def test_negative_editing_project2():
#Получение несуществующего объекта по ID
    login = ""
    password = ""
    companyId = "2e7b21df-b05c-4784-8a3e-d191134a21e0"
    project = api.get_project(login=login, password=password, companyId=companyId, project_id="2155489")
    