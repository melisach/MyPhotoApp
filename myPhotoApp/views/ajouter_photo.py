from django.urls import reverse
from django.views.generic import CreateView
from myPhotoApp.forms.add_photo import AddFormPhoto
from myPhotoApp.models.photo import Photo
from django.contrib.auth.mixins import LoginRequiredMixin


class AddPhotoView(LoginRequiredMixin, CreateView):
    template_name = 'Photos/ajouter_photo.html'
    form_class = AddFormPhoto
    model = Photo

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('gallerie')









