from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("accounts/", hello.views.accounts, name= "accounts"),
    path("slides/", hello.views.slides, name= "slides"),
    path("login/", hello.views.login, name= "login"),
    path("home-c/", hello.views.home_c, name= "home-c"),
    path("despesas/", hello.views.despesas, name= "despesas"),
    path("metas/", hello.views.metas, name= "metas"),
    path("faq/", hello.views.faq, name= "faq"),
    path("home-p/", hello.views.home_p, name= "home-p"),
    path("conta-corrente/", hello.views.conta_corrente, name= "conta-corrente"),
    path("inner-page/", hello.views.inner_page, name= "inner-page"),
    path("plan-mensal/", hello.views.plan_mensal, name= "plan-mensal"),
    path("planejamento/", hello.views.planejamento, name= "planejamento"),
    path("despesas/", hello.views.despesas, name= "despesas"),
    path("portfolio-details/", hello.views.portfolio_details, name= "portfolio-details"),
    path("pagamento/", hello.views.pagamento, name= "pagamento"),
    path("cash-invest/", hello.views.cash_invest, name= "cash-invest"),


]
