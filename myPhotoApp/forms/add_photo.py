from django import forms
from myPhotoApp.models.photo import Photo


class AddFormPhoto(forms.ModelForm):

    class Meta:
        model = Photo
        fields = [
            'categorie',
            'description',
            'image',

        ]

    def clean(self):
        pass

    def clean_categorie(self):
        if self.cleaned_data['categorie'] == '':
           self.add_error('categorie', "categorie can't be empty!")
        return self.cleaned_data['categorie']

    def clean_description(self):
        if self.cleaned_data['description'] == '':
            self.add_error('description', "description can't be empty!")
        return self.cleaned_data['description']

    def clean_image(self):
        if self.cleaned_data['image'] == '':
            self.add_error('image', "image name can't be empty!")
        return self.cleaned_data['image']