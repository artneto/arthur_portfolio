from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    # Homepage
    path('', views.IndexView.as_view(), name='home'),
    
    # Contact page
    path('contact/', views.ContactView.as_view(), name='contact'),
    
    # Portfolio list page
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio_list'),
    
    # Portfolio detail page
    path('portfolio/<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
    
    # Blog list page
    path('blog/', views.BlogView.as_view(), name='blog_list'),
    
    # Blog detail page
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
]