from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect, JsonResponse
import datetime as dt
from .models import Article, NewsLetterRecipients, MoringaMerch
from .forms import NewsLetterForm, NewsArticleForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer



# Create your views here.
def news_today(request):
  date = dt.date.today()
  news = Article.todays_news()
  form = NewsLetterForm()

  return render(request, 'all-news/today-news.html', {"date": date, "news": news, "letterForm":form}) 

def past_days_news(request, past_date):
  try:
     # converts data from the string url
     date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
  except ValueError:
      #raise 404 error when ValueError is thrown
      raise Http404()
      assert False
  if date == dt.date.today():
    return redirect(news_today)

  news = Article.days_news(date)    
  return render(request, 'all-news/past-news.html', {"date": date, "news":news})

def search_results(request):
  if 'article' in request.GET and request.GET["article"]:
    search_term = request.GET.get("article")
    searched_articles = Article.search_by_title(search_term)
    message = f"{search_term}"

    return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})
  else:
     message = "You haven't searched for any term"
     return render(request, 'all-news/search.html',{"message":message}) 

@login_required(login_url='/accounts/login/')
def article(request,article_id):
  try:
    article = Article.objects.get(id = article_id)
  except:
    raise Http404()
  return render(request,'all-news/article.html', {"article":article})

@login_required(login_url='/accounts/login/')
def new_article(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewsArticleForm(request.POST, request.FILES)
    if form.is_valid():
      article = form.save(commit=False)
      article.editor = current_user
      article.save()
    return redirect('newsToday')
  else:
    form = NewsArticleForm()
  return render(request, 'new_article.html',{"form":form})   

def newsletter(request):
  name = request.POST.get('your_name')
  email = request.POST.get('email')

  recipient = NewsLetterRecipients(name =  name, email = email)
  recipient.save()
  send_welcome_email(name, email)
  data = {'Success': 'You have been successfully added to mailing list'}
  return JsonResponse(data)

class MerchList(APIView):
  def get(self, request, format=None):
    all_merch = MoringaMerch.objects.all()
    serializers = MerchSerializer(all_merch, many=True)
    return Response(serializers.data)
