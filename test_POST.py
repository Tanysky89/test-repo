from YougileApi import yougileApi

api = yougileApi("https://ru.yougile.com")


def test_positive_new_project():
    login = "e"
    password = ""
    companyId = "2e7b21df-b05c-4784-8a3e-d191134a21e0"

    #Получаем количество проектов до добавления нового проекта
    projects_before = api.get_project_list(login=login, password=password, companyId=companyId)
    len_projects_before = len(projects_before)
    
    #Добавляем новый проект
    random_users = api.get_random_users(login=login, password=password, companyId=companyId)
    new_project_id = api.create_project("My_new_test_project", random_users, login=login, password=password, companyID=companyId)
   
    #Получаем количество проектов после добавления нового
    projects_after = api.get_project_list(login=login, password=password, companyId=companyId)
    len_projects_after = len(projects_after)
    assert len_projects_after-len_projects_before == 1,"Ошибка! Новый проект не был добавлен"


def test_negative_new_project():
    login = ""
    password = ""
    companyId = "2e7b21df-b05c-4784-8a3e-d191134a21e0"

    #Получаем количество проектов до добавления нового проекта
    projects_before = api.get_project_list(login=login, password=password, companyId=companyId)
    len_projects_before = len(projects_before)
   
    #Добавляем новый проект без указания названия (ошибка - "title should not be empty")
    random_users = api.get_random_users(login=login, password=password, companyId=companyId)
    new_project_id = api.create_project("", random_users, login=login, password=password, companyID=companyId)
    
    #Получаем количество проектов после добавления нового
    projects_after = api.get_project_list(login=login, password=password, companyId=companyId)
    len_projects_after = len(projects_after)
    assert len_projects_after-len_projects_before == 1,"Ошибка! Новый проект не был добавлен"