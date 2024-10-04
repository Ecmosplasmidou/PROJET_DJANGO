from django import forms
from listing.models import Band, Listing

class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False,  max_length=50)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
class BandForm(forms.ModelForm):
    class Meta:
        model=Band
        exclude = ('active',)
        
class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        exclude = ('sold',)
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Listing.objects.filter(title=title).exists():
            raise forms.ValidationError('Ce titre existe déjà')
        return title