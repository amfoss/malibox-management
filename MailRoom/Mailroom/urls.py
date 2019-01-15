from django.conf.urls import url
from . import views
from django.contrib.auth import views as  authViews
urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.login, name="login.html"),
    url(r'^logout/$', views.logout_view, name="logout.html"),
    url(r'^entry/$',views.Package_entry, name="entry.html"),
    url(r'^delivery/$',views.retrieve,name="delivery.html"),
    url(r'^verified/$',views.verified,name="verified.html"),
    url(r'^Home/$',views.Home,name="Home.html")
]
