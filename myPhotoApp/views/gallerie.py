from django.views.generic import ListView
from myPhotoApp.models.categorie import Categorie
from myPhotoApp.models.photo import Photo
from django.contrib.auth.mixins import LoginRequiredMixin


class GallerieView(LoginRequiredMixin, ListView):
    template_name = 'photos/gallerie.html'
    model = Categorie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categorie = self.request.GET.get('categorie')
        if categorie is None:
            context['photos'] = Photo.objects.all()
        else:
            context['photos'] = Photo.objects.filter(categorie__categorie=categorie)
        return context
