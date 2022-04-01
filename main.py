from __future__ import print_function	
import eel
from models.bd_task import saveTask_py, update_task, acceptingAnId_py, retuuurnLineId, updateLineTask_py, retuuurnStatusId, f_nNum
from models.bd_contact import saveContact_py, update_contact, accepting_nNum_S6M_py, accepting_id_ED_py 
eel.init('web')

#- Заметеки ----------------------------------------------------------------------------------------------------------------------------------------------------------

@eel.expose 
def taskValue(index_t, condition_t, queue_t, text_t, date_t, time_t, koment_t, dopKoment_t, reglament_t, dopReglament_t, osobennosti_t, dapOsobennosti_t):
    msg = saveTask_py(index_t, condition_t, queue_t, text_t, date_t, time_t, koment_t, dopKoment_t, reglament_t, dopReglament_t, osobennosti_t, dapOsobennosti_t)
    up = updateLineTask_py(index_t, condition_t, queue_t, text_t, date_t, time_t, koment_t, dopKoment_t, reglament_t, dopReglament_t, osobennosti_t, dapOsobennosti_t)

@eel.expose 
def creatingLineId():
    get_line = retuuurnLineId()
    eel.retuuurnLineId_js(get_line)
    print("Строка передалась в JS, для дальнейшего её редактирования")
    print("")
    print("-"*130)

@eel.expose 
def creatingStatusId():
    get_status = retuuurnStatusId()
    eel.retuuurnStatusId_js(get_status)
    print("Строка передалась в JS, для дальнейшего её редактирования")
    print("")
    print("-"*130)

@eel.expose 
def idTransfer_SED(index,nNum):
    int(index)
    int(nNum)
    print("")
    print( "id строки = ", index, "| номер строки = ", nNum, " | переданы для проверки в базе данных" )
    msg = acceptingAnId_py(index,nNum)

@eel.expose 
def creating_SL_Id():
    nNum = f_nNum()
    if (nNum == '1'):
        get_status = retuuurnStatusId()
        eel.retuuurnStatusId_js(get_status)
    elif (nNum == '2'):
        get_line = retuuurnLineId()
        eel.retuuurnLineId_js(get_line)


@eel.expose 
def update_all_task():
    get_tasks = update_task()
    eel.get_update_task_js(get_tasks)
    print("-"*130)
    print( "Заметки в базе данных")
    print("-"*130)
    for i in get_tasks:
        print(i)
    print("-"*130)

#- Контакты ----------------------------------------------------------------------------------------------------------------------------------------------------------

@eel.expose 
def contactValue(save_C_Id, save_C_name, save_C_organiz, save_C_address, save_C_tel, save_C_mail, save_C_ICQ):
    msg = saveContact_py(save_C_Id, save_C_name, save_C_organiz, save_C_address, save_C_tel, save_C_mail, save_C_ICQ)

@eel.expose 
def update_all_contact():
    get_contacts = update_contact()
    eel.get_update_contact_js(get_contacts)
    print("-"*130)
    print( "Контакты в базе данных")
    print("-"*130)
    for i in get_contacts:
        print(i)
    print("-"*130)

@eel.expose 
def nNumTransfer_S6M(nNum):
    int(nNum)
    print("")
    print( " номер сортировки = ", nNum, " | передан для сортировки в базы данных" )
    msg = accepting_nNum_S6M_py(nNum)

@eel.expose 
def idTransfer_ED(index, nNum):
    int(index)
    int(nNum)
    print("")
    print( "id контакта = ", index, "| номер= ", nNum, " | переданы для проверки в базе данных" )
    msg = accepting_id_ED_py(index, nNum)




eel.start('main.html') 