from django.urls import path
from . import  views
urlpatterns =[
    path('',views.index,name='index'),
    path('/choose',views.index2,name='index2'),
    path('showtou',views.get_tour,name = 'showtour'),
    path('showmem',views.get_mem,name = 'showmem'),
    path('showplay',views.get_player,name = 'showplay'),
    path('showmat',views.get_match,name = 'showmat'),
    path('goto',views.gotoin1,name='gototou'),
    path('goto1',views.gotoin2,name='gotoplay'),
    path('goto2',views.gotoin3,name='gotomem'),
    path('goto3',views.gotoin4,name='gotomat'),
    path('inserttou/',views.inserttou,name='insert'),
    path('insertmem/',views.insertmem,name='insert1'),
    path('insertplay/',views.insertplay,name='insert2'),
    path('insertmat/',views.insertmat,name='insert3'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('deletetou/<int:id>/', views.deletetou, name='delete'),
    path('deletepla/<int:id>/', views.deletepla, name='delete'),
    path('deletemat/<int:id>/', views.deletemat, name='delete'),

    path('update/<int:id>/', views.update, name='update'),
    path('update/uprec/<int:id>/', views.uprec, name="uprec"),

    path('updatemem/<int:id>/', views.updatemem, name='updatemem'),
    path('updatemem/uprecmem/<int:id>/', views.uprecmem, name="uprecmem"),

    path('updateplay/<int:id>/', views.updateplay, name='updatepaly'),
    path('updateplay/uprecplay/<int:id>/', views.uprecplay, name="uprecplay"),

]