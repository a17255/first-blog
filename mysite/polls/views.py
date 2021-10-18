from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.


def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def viewArticle(request, month, year):
   text = "Displaying articles of : %s/%s"%(year, month)
   return HttpResponse(text)