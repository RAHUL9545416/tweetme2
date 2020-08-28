from django.shortcuts import render
from django.http import HttpResponse , Http404, JsonResponse
# Create your views here.
from .models import Tweet

def home_view(request, *args,**kwargs):
   
    return HttpResponse("<h1> Hello world</h1>")



def tweet_detail_view(request, tweet_id, *args,**kwargs):

    """
    REST API VIEWS
    CONSUME BY JS OR SWIFT RETURN JSON
    
    """

    data ={

        "id": tweet_id,
        #"image_path": obj.image.url

    }

    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content']=obj.content

    except:
        data['massage'] ="Not found"
        status =400
    
    return JsonResponse(data, status=status) # json.dumps contetn_type ="1"