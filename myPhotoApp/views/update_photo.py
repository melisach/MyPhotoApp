from django.urls import reverse_lazy
from django.views.generic import UpdateView
from myPhotoApp.forms.update_photo import UpdatePhoto
from myPhotoApp.models.photo import Photo


class UpdatePhotoView(UpdateView):
    model = Photo
    form_class = UpdatePhoto
    template_name = 'photos/update_photo.html'
    success_url = reverse_lazy('user_gallerie')









