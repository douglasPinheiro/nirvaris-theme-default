
from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .forms import FormStyleForm

from .classes import TagImage

class HorizontalThumbsView(View):
    
    def get(self, request):

        images = []
        images.append(TagImage('image_1.jpg','Space Cruiser'))
        images.append(TagImage('image_2.jpg','Sky Battle'))
        images.append(TagImage('image_3.jpg','Game shoot'))
        images.append(TagImage('image_4.jpg','Tatooine Band'))
        images.append(TagImage('image_5.jpg','Jaba Agent'))
        images.append(TagImage('image_6.jpg','Death Star'))
        images.append(TagImage('image_7.jpg','Guy from Tatooine'))
        images.append(TagImage('image_8.jpg','Master Yoda'))
        images.append(TagImage('image_9.jpg','Ground battle game shoot'))
        images.append(TagImage('image_10.jpg','Milenium Falcon'))
        images.append(TagImage('image_11.jpg','Game Play'))
        images.append(TagImage('image_12.jpg','Rebels Fighter Game Play'))
        images.append(TagImage('image_13.jpg','Jedi Knights'))
        images.append(TagImage('image_14.jpg','Darth Vader'))
        images.append(TagImage('image_15.jpg','Darth Vader Game Play'))
        images.append(TagImage('image_16.jpg','Darth Vader Applying the Force'))
        images.append(TagImage('image_17.jpg','Master Youda Again'))
        images.append(TagImage('image_18.jpg','Imperial Fighters'))

        
        request_context = RequestContext(request,{'images':images})
        return render_to_response('horizontal-thumbs.html', request_context)

class HomeView(TemplateView):
    template_name = "theme-home.html"

class FormStyleView(FormView):
    template_name = 'test-form-style.html'
    form_class = FormStyleForm
    success_url = 'form-style'
    
class MessagesStyleView(TemplateView):
    template_name = 'test-messages-style.html'
    
    def get(self, request):
        
        if not 'message_type' in request.GET:
            messages.error(request, _('You must set a parameter "message_type with the stype: success, info or error"'))
            return super(MessagesStyleView,self).get(request)
            
        message_type = request.GET['message_type']
        
        if 'success' in message_type: 
            messages.success(request, _('This is a SUCCESS message test'))
        if 'info' in message_type:             
            messages.info(request, _('This is a INFO message test'))
        if 'error' in message_type: 
            messages.error(request, _('This is a ERROR message test'))                
        
        return super(MessagesStyleView,self).get(request)