def refreshPA(uname,passw):
    import requests
    response = requests.get('https://www.pythonanywhere.com/login/', params={'next':'/user/{}/webapps/'.format(uname)}.items())
    csrft=response.text[response.text.find("value='",response.text.find("csrfmiddlewaretoken"))+7:response.text.find("'",response.text.find("value='",response.text.find("csrfmiddlewaretoken"))+7)]
    cookies = response.cookies.get_dict()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.pythonanywhere.com/login/?next=/user/{}/webapps/'.format(uname),
    }
    params={'next':'/user/{}/webapps/'.format(uname)}.items()
    data = {
      'csrfmiddlewaretoken': csrft,
      'auth-username': '{}'.format(uname),
      'auth-password': '{}'.format(passw),
      'login_view-current_step': 'auth'
    }
    response2 = requests.post('https://www.pythonanywhere.com/login/', headers=headers, params=params, cookies=cookies, data=data, allow_redirects = 1)
    csrft=response2.text[response2.text.find("value='",response2.text.find("csrfmiddlewaretoken"))+7:response2.text.find("'",response2.text.find("value='",response2.text.find("csrfmiddlewaretoken"))+7)]
    cookies=response2.history[0].cookies.get_dict()
    #cookies['web_app_tab_type']='%23tab_id_{}_pythonanywhere_com'.format(uname)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.pythonanywhere.com/user/{}/webapps/'.format(uname),
    }
    data = {'csrfmiddlewaretoken': csrft}
    response3 = requests.post('https://www.pythonanywhere.com/user/{0}/webapps/{0}.pythonanywhere.com/extend'.format(uname), headers=headers, cookies=cookies, data=data)
    success=response3.request.url.count(uname)
    return bool(success)

def refreshTask(uname,passw):
    import requests
    response = requests.get('https://www.pythonanywhere.com/login/', params={'next':'/user/{}/tasks_tab/'.format(uname)}.items())
    csrft=response.text[response.text.find("value='",response.text.find("csrfmiddlewaretoken"))+7:response.text.find("'",response.text.find("value='",response.text.find("csrfmiddlewaretoken"))+7)]
    cookies = response.cookies.get_dict()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.pythonanywhere.com/login/?next=/user/{}/tasks_tab/'.format(uname),
    }
    params={'next':'/user/{}/tasks_tab/'.format(uname)}.items()
    data = {
      'csrfmiddlewaretoken': csrft,
      'auth-username': '{}'.format(uname),
      'auth-password': '{}'.format(passw),
      'login_view-current_step': 'auth'
    }
    response2 = requests.post('https://www.pythonanywhere.com/login/', headers=headers, params=params, cookies=cookies, data=data, allow_redirects = 1)
    csrft=response2.text[response2.text.find("value='",response2.text.find("csrfmiddlewaretoken"))+7:response2.text.find("'",response2.text.find("value='",response2.text.find("csrfmiddlewaretoken"))+7)]
    cookies=response2.history[0].cookies.get_dict()
    #cookies['web_app_tab_type']='%23tab_id_{}_pythonanywhere_com'.format(uname)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://www.pythonanywhere.com/user/{}/tasks_tab/'.format(uname),
    }
    data = {'csrfmiddlewaretoken': csrft}
    response22 = requests.get('https://www.pythonanywhere.com/api/v0/user/{}/schedule/'.format(uname), cookies=cookies)
    taskid=response22.json()[0]['id']
    response3 = requests.post('https://www.pythonanywhere.com/user/{0}/schedule/task/{1}/extend'.format(uname,taskid), headers=headers, cookies=cookies, data=data)
    success=response3.text.count("success")
    return bool(success)


def loopMain(uname,passw,interval=60*60*24*30,count=-1,logTimeZone='Asia/Kolkata'):#seconds
    import time
    ind=0
    while int(count)!=0:
        ind,count=ind+1,int(count)-1
        print("Log:{}: AttemptTask({}) Success={}".format(str(__import__("datetime").datetime.now(__import__("pytz").timezone(logTimeZone))),ind,refreshTask(uname,passw)))
        print("Log:{}: AttemptWeb({}) Success={}".format(str(__import__("datetime").datetime.now(__import__("pytz").timezone(logTimeZone))),ind,refreshPA(uname,passw)))
        if count:time.sleep(int(interval))
if __name__=="__main__":
    if len(__import__('sys').argv)<3:print("Usage: python script.py username password [interval(seconds)=1month] [count=-1] [logtimestamp-timezone=Asia/Kolkata]")
    else:loopMain(*__import__('sys').argv[1:6])
