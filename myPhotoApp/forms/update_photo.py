from django import forms
from myPhotoApp.models.photo import Photo


class UpdatePhoto(forms.ModelForm):
    class Meta:
        model = Photo

        fields = ['description',
                  'categorie',
                  'image']