urlpatterns = [
    # URLs Funcionales - Autor
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),
    
    # URLs Genéricas - Libro
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/crear/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/editar/<int:pk>/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/eliminar/<int:pk>/', views.LibroDeleteView.as_view(), name='libro_delete'),
]