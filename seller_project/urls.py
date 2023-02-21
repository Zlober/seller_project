"""seller_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seller_project.orders import views
from seller_project.finance import views as fin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index_page'),
    path('<int:pk>/complete/', views.CompleteOrder.as_view(), name='complete_order'),
    path('<int:pk>/detail/', views.ViewOrder.as_view(), name='detail_order'),
    path('<int:pk>/canceled/', views.CancelOrder.as_view(), name='cancel_order'),
    path('<int:pk>/printed/', views.PrintedOrder.as_view(), name='printed_order'),
    path('allorders/', views.AllOrders.as_view(), name='all_orders'),
    path('finance/', fin_view.FinanceView.as_view(), name='finance'),
    path('finance/report/', fin_view.FinanceReport.as_view(), name='finance_report')
]
