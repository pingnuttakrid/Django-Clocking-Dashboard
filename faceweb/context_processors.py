from faceweb.models import Status

def menu_links(request):
    links=Status.objects.all()
    return dict(links=links)