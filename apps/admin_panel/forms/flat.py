from django import forms

from admin_panel import models
from register import models as reg_models


class FlatForm(forms.ModelForm):
    prefix = 'house_flat'
    # house = forms.ModelChoiceField(
    #     queryset=models.House.objects.all(),
    # )
    # section = forms.ModelChoiceField(
    #     queryset=models.HouseSection.objects.filter(house_id=house),
    # )
    owner = forms.ModelChoiceField(
        queryset=reg_models.User.get_active_users(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Владелец квартиры',
    )

    class Meta:
        model = models.Flat
        fields = (
            'number',
            'area',
            'house',
            'section',
            'floor',
            'owner',
            'tariff',
        )
        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'area': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'house': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'section': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'floor': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'tariff': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
