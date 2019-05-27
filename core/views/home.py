# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse


def home_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('desk:dashboard'))
    else:
        template = loader.get_template('core/home.html')
        context = {
            # 'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))
