from myPhotoApp.models.photo import Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class DeletePhotoView(LoginRequiredMixin, DeleteView):
    template_name = "photos/photo_confirm_delete.html"
    model = Photo
    success_url = reverse_lazy('user_gallerie')









