from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        "Cleans the entire form data"
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email_clean = all_clean_data['verify_email']

        if email != verify_email_clean :
            raise forms.ValidationError('MAKE SURE EMAIL IS CORRECT AND IT MATCHES')



    ## THIS BLOCK OF CODE HAS BEEN COMMENTED AND SERVES NO PUPOSE
    ## RIGHT NOW. IT EXISTS JUST FOR PERSONAL REFERENCE.
    
    ##=============================================================
                        # CUSTOM VAILDATOR EXAMPLES
    ##=============================================================

    #-------------------------------------------------------
    # EG: 1) SIMPLE BOTCATCHER

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0 :
    #         raise forms.ValidationError("Heil Botcatcher!")
    #         print("Botcatcher wins!")
    #     return botcatcher

    #---------------------------------------------------------
    # EG: 2) A CUSTOM VALIDATOR THAT CHECKS FOR 'Z'
    # def check_for_z(value):
    #     if value[0].lower() != 'z':
    #         raise forms.ValidationError("Name needs to start with 'Z'")

    #---------------------------------------------------------
    ##=============================================================
