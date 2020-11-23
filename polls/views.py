from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import connections 
from polls.models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question' : question, 
            'error_message' : 'You didnt select a choice',
        })
    else :
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=([question.id])))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})


def db(request):
    with connections["default"].cursor() as cursor:
        sql = "select * from mydb.users"
        cursor.execute(sql)
        row = cursor.fetchall()
        datas = []
        for data in row:
            r = {'user_id' : data[0], 'user_name' : data[1], 'user_age':data[2]}
            datas.append(r)
        #cursor.commit()
        cursor.close()
        print(row)
    return render(request, 'polls/db.html', {'results':datas})


def db_insert(request):
    with connections["default"].cursor() as cursor:
        sql = "insert mydb.users values ('104','lsll',12)"
        cursor.execute(sql)
        row = cursor.fetchone()        
        #cursor.commit()
        cursor.close()
    return HttpResponseRedirect(reverse('polls:db'))