from django import forms 


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
                                                            'class' : 'form-control w-100',
                                                            'id' : 'contentsBox',
                                                            'rows' : '3'}))