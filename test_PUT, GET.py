from YougileApi import yougileApi

login = "tatyana@tpbay.site"
password = "12345qwerty"
companyId = "2e7b21df-b05c-4784-8a3e-d191134a21e0"
api = yougileApi("https://ru.yougile.com", login, password, companyId)


def test_positive_editing_project():
    #если количество проектов при тестировании достигло ограничения в 50 - удалим 10 сиз них для возможности продолжать работу
    projects_count = len(api.get_project_list())
    if projects_count == 50:
        api.delete_projects(10)
    
    random_users = api.get_random_users()
    new_project_id = api.create_project("My_new_test_project", random_users)
    editing_project = api.editing_project("My_ed_test_project", random_users, project_id=new_project_id, deleted=False)
    project = api.get_project(project_id=new_project_id)
    
    assert project['title'] == "My_ed_test_project"
    assert project['id'] == new_project_id

  
def test_negative_editing_project():
    
    #если количество проектов при тестировании достигло ограничения в 50 - удалим 10 сиз них для возможности продолжать работу
    projects_count = len(api.get_project_list())
    if projects_count == 50:
        api.delete_projects(10)
        
    #Добавляем новый проект
    random_users = api.get_random_users()
    new_project_id = api.create_project("My_project", random_users)

    #Удаляем созданный проект
    editing_project = api.editing_project("My_project", random_users, new_project_id, deleted=True)

    #Получение удаленного объекта по ID
    project = api.get_project(project_id=new_project_id)
    assert project['deleted'] == False
    
    
def test_negative_editing_project2():
    #Получение несуществующего объекта по ID
    project = api.get_project(project_id="2155489")
