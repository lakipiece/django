from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import connections 

# Create your views here.
def index(request):    
    return render(request, 'home/index.html')

def login(request):    
    try : 
        s_id = request.POST['SignID']
        s_pw = request.POST['SignPW']
    except (KeyError):
        return render(request, 'home/index.html')
    else :
        with connections["default"].cursor() as cursor:      
            sql = "select signid, signpw from django.crm_user where signid=%s"
            cursor.execute(sql, s_id)
            row = cursor.fetchall()
            cursor.close()

            datas = []
            print (row)
            print (row[0][1])
            print (s_pw)
            if row[0][1] == s_pw :
                for data in row:
                    r = {'signid' : data[0]}
                    datas.append(r)
                return render(request, 'home/main.html', {'datas':datas})
                #cursor.commit()
            else : 
                return render(request, 'home/index.html')
            request.session['SignID'] = s_id
            request.session.save()
            print(row)
            print(type(datas[0]))
            print(datas[0])
            print(request.session['SignID'])
