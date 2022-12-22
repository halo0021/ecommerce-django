from .models import Category

# esta funcion para   listar las categorias directamente
#desde la base dedatos
def menu_links(request):
    links =Category.objects.all()
    return dict(links=links)
