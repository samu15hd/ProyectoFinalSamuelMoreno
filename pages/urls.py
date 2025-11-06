from django.urls import path
from . import views
from .views import PageListView, about, detalle_pagina, editar_pagina, eliminar_pagina, mis_paginas


urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear_pagina, name='crear_pagina'),
    path('pages/', PageListView.as_view(), name='listar_paginas'),
    path('about/', about, name='about'),
    path('paginas/<int:id>/', detalle_pagina, name='detalle_pagina'),
    path('paginas/<int:id>/editar/', editar_pagina, name='editar_pagina'),
    path('paginas/<int:id>/eliminar/', eliminar_pagina, name='eliminar_pagina'),
    path('mis-paginas/', mis_paginas, name='mis_paginas'),
]
