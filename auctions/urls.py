from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create, name="create"),
    path("listing:<int:listing_id>", views.listing, name="listing"),
    path("watchlist:<int:user_id>", views.watchlist, name="wl"),
    path("category:<str:category_id>", views.category, name = 'category')


]
