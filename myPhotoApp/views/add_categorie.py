from django.urls import reverse
from django.views.generic import CreateView
from myPhotoApp.forms.add_categorie import AddFormCategorie
from myPhotoApp.models.categorie import Categorie
from django.contrib.auth.mixins import LoginRequiredMixin


class AddCategorieView(LoginRequiredMixin, CreateView):
    template_name = 'Photos/add_categorie.html'
    form_class = AddFormCategorie
    model = Categorie

    def form_valid(self, form):

        try:
            categorie = form.cleaned_data['categorie'].upper()
            form.cleaned_data['categorie'] = categorie
            # update the instance value.
            form.instance.categorie = categorie
            return super().form_valid(form)

        except Exception as e:
            form.add_error(None, "Un objet Category avec ce champ Categorie existe déjà.")
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('add_photo')