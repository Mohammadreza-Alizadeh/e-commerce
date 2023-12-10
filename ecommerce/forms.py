from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AddToCartForm(forms.Form):

    quantity = forms.IntegerField(min_value=1, max_value=10)

    def __init__(self, *args, **kwargs):
        # Receive additional parameters in the constructor
        action_url = kwargs.pop('action_url', None)
        super(AddToCartForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # Set the form action dynamically
        if action_url:
            self.helper.form_action = action_url

        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


class DeleteFromCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10)

    def __init__(self, *args, **kwargs):
        # Receive additional parameters in the constructor
        action_url = kwargs.pop('action_url', None)
        super(DeleteFromCartForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # Set the form action dynamically
        if action_url:
            self.helper.form_action = action_url

        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
