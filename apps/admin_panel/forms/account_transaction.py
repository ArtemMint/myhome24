from django import forms
import datetime

from admin_panel import models
from register import models as register_models


class AccountTransactionForm(forms.ModelForm):
    prefix = 'account_transaction'
    transaction = forms.ModelChoiceField(
        queryset=models.TransactionPurpose.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Статья',
    )
    manager = forms.ModelChoiceField(
        queryset=register_models.User.users_admin.get_queryset(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Менеджер',
    )
    owner = forms.ModelChoiceField(
        queryset=register_models.User.users.get_queryset(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Владелец',
    )

    class Meta:
        model = models.AccountTransaction
        fields = (
            'number',
            'created_date',
            'confirm',
            'owner',
            'account',
            'transaction',
            'total',
            'manager',
            'comment',
        )

        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер ведомости..',
                }
            ),
            'created_date': forms.DateInput(
                format=(
                    '%d-%m-%Y'
                ),
                attrs={
                    'type': 'date',
                    'class': 'form-control datepicker',
                    'value': datetime.datetime.now().strftime("%d/%m/%Y"),
                },
            ),
            'confirm': forms.CheckboxInput(),
            'total': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                    'step': "0.01",
                    'placeholder': 'Введите сумму..',
                }
            ),
            'account': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Напишите комментарий..',
                    'rows': 4,
                }
            ),
        }


class AccountTransactionIncomeForm(AccountTransactionForm):
    transaction = forms.ModelChoiceField(
        queryset=models.TransactionPurpose.get_income(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Статья',
    )


class AccountTransactionExpenditureForm(AccountTransactionForm):
    transaction = forms.ModelChoiceField(
        queryset=models.TransactionPurpose.get_expenditure(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Статья',
    )
