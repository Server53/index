from django import forms


class AddServerForm(forms.Form):
    # name = forms.CharField(max_length=256)
    # description = forms.CharField(max_length=4096)
    # modded = forms.BooleanField()
    client_json_file = forms.FileField()
