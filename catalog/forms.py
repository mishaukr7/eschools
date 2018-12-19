from django import forms


class FeedBackForm(forms.Form):
    parent_feedback = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )
    feedback_area = forms.CharField(
        label='',
        widget=forms.Textarea
    )

