from sqlalchemy import create_engine, text
from Table import Table


db = Table("postgresql://postgres:123@localhost:5432/postgres")


def test_get_add():
    #Шаг1: получить список из БД:
    db_result_bef = db.get_places()
    len_projects_before = len(db_result_bef)
    
    #Шаг2: добавить новую позицию
    max_id = db.get_max_id()    #автоматически заполняем айди значением больше мексимального, чтоб избежать ошибки повторения айди при повторном запуске
    place_id = max_id + 1 
    place_name = "яма"
    place_size = 100 
    place_date_start = '1989-01-01 00:00:00'
    
    db.new_places(place_id, place_name, place_size, place_date_start)
    
    #Шаг3: проверить обновленный список на наличие новой позиции
    db_result_af = db.get_places()
    len_projects_after = len(db_result_af)
    
    assert len_projects_after-len_projects_before == 1,"Ошибка! Новый объект не был добавлен"
    
    #Шаг4: удалить тестовые данные
    pl_id = place_id
    db.del_places(pl_id)
    
    #Шаг5: проверка наличия удаленного ID
    db_result_aft = db.get_by_id(pl_id)
    assert len(db_result_aft) == 0, "ОШИБКА!!! Строка с указанным ID не была удалена!"

    
def test_get_del():
    place_id = 28
    pl_id = place_id
    db.del_places(pl_id)
    
    #Шаг2: проверка наличия удаленного ID
    db_result_aft = db.get_by_id(pl_id)
    assert len(db_result_aft) == 0, "ОШИБКА!!! Строка с указанным ID не была удалена!"
    
    
def test_edit():
    #Шаг1: получить список из БД:
    db_result_bef = db.get_places()
    len_projects_before = len(db_result_bef)
    
    #Шаг2: добавить новую позицию
    max_id = db.get_max_id()    #автоматически заполняем айди значением больше мексимального, чтоб избежать ошибки повторения айди при повторном запуске
    place_id = max_id + 1 
    place_name = "колодец"
    place_size = 100 
    place_date_start = '1989-01-01 00:00:00'
    
    db.new_places(place_id, place_name, place_size, place_date_start)
    
    #Шаг3: проверить обновленный список на наличие новой позиции
    db_result_af = db.get_places()
    len_projects_after = len(db_result_af)
    
    assert len_projects_after-len_projects_before == 1,"Ошибка! Новый объект не был добавлен"
    
    #шаг5: Изменить тестовые данные
    place_name = 'ров'
    place_size = 100 
    place_date_start = '1989-01-01 00:00:00'
    db.ed_places(place_id, place_name, place_size, place_date_start)
    pl_id = place_id
    db_result_ed = db.get_by_id(pl_id)
    
    assert db_result_ed [0][1] == 'ров'
    assert db_result_ed [0][2] == 100
    
    #Шаг4: удалить тестовые данные
    pl_id = place_id
    db.del_places(pl_id)
    
    #Шаг5: проверка наличия удаленного ID
    db_result_aft = db.get_by_id(pl_id)
    assert len(db_result_aft) == 0, "ОШИБКА!!! Строка с указанным ID не была удалена!"