from django import forms
from myPhotoApp.models.categorie import Categorie


class AddFormCategorie(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['categorie']

        def clean(self):
            pass

        def clean_password(self):
            if self.cleaned_data['categorie'] == '':
                self.add_error('categorie', "categorie can't be empty!")
            return self.cleaned_data['categorie']