# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from .models import Bd

def index(request):
    bbs = Bd.objects.all()
    return render(request, 'bboard/index.html', {'bbs':bbs})

    # template = loader.get_template('bboard/index.html')
    # bbs = Bd.objects.order_by('-published')
    # context = {'bbs':bbs}

    # s = 'Объявления\r\n\r\n\r\n'
    # for bb in Bd.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(template.render(context, request))



