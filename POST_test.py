from YougileApi import yougileApi

login = "tatyana@tpbay.site"
password = "12345qwerty"
companyId = "2e7b21df-b05c-4784-8a3e-d191134a21e0"
api = yougileApi("https://ru.yougile.com", login, password, companyId)


def test_positive_new_project():
    #если количество проектов при тестировании достигло ограничения в 50 - удалим 10 сиз них для возможности продолжать работу
    projects_count = len(api.get_project_list())
    if projects_count == 50:
        api.delete_projects(10)
        
    #Получаем количество проектов до добавления нового проекта
    projects_before = api.get_project_list()
    len_projects_before = len(projects_before)
    
    #Добавляем новый проект
    random_users = api.get_random_users()
    new_project_id = api.create_project("My_new_test_project2P", random_users)
   
    #Получаем количество проектов после добавления нового
    projects_after = api.get_project_list()
    len_projects_after = len(projects_after)
    assert len_projects_after-len_projects_before == 1,"Ошибка! Новый проект не был добавлен"


def test_negative_new_project():
    #Получаем количество проектов до добавления нового проекта
    projects_before = api.get_project_list()
    len_projects_before = len(projects_before)
   
    #Добавляем новый проект без указания названия (ошибка - "title should not be empty")
    random_users = api.get_random_users()
    new_project_id = api.create_project("", random_users)
    
    print(new_project_id)
    
    