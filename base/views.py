from django.shortcuts import render
from django.contrib import messages
from .models import (
        UserProfile,
        Blog,
        Portfolio,
        Testimonial,
        Certificate
)


from django.views import generic


from . forms import ContactForm

class IndexView(generic.TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)

        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blogs'] = blogs
        context['portfolio'] = portfolio
        return context


class ContactView(generic.FormView):
    template_name = 'base/contact.html'
    form_class = ContactForm
    sucess_url = "/"

    def form_valid(self, form):
        form.save()
        messages.sucess(self.request, 'Thank you. We will be in touch soon!')
        return super().form_valid(form)

        
