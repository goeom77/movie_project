from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Title',
        })
    )

    audience = forms.IntegerField(
        widget= forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Audience',
        })
    )

    release_date = forms.DateField(
        widget = forms.DateInput(attrs={
            'class':'form-control',
            'placeholder':'연도-월-일',
            'type':'date',
        })
    )

    GENRE_COICES = (
        ('코미디','코미디'),
        ('공포','공포'),
        ('로맨스','로맨스'),
        ('19금','19금'),
        ('액션','액션'),
        ('애니매이션','애니매이션'),
        ('다큐멘터리','다큐멘터리'),
        ('드라마','드라마'),
    )
    genre = forms.ChoiceField(
        widget = forms.Select(attrs={
            'class':'form-control',
        }),
        choices = GENRE_COICES
    )

    score = forms.FloatField(
        widget = forms.NumberInput(attrs={
            'min':'0',
            'max':'10',
            'step':'0.1',
            'class':'form-control',
            'placeholder':'Score',
        })
    )

    poster_url = forms.CharField(
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Poster url',
        })
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':'Description',
        })
    )

    class Meta:
        model = Movie
        exclude = ('user',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('movie','user',)