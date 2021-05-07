from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from admin_panel.models.transaction_purpose import \
    TransactionPurpose
from admin_panel.forms.transaction_purpose import \
    TransactionPurposeForm


class TransactionPurposeList(ListView):
    model = TransactionPurpose
    context_object_name = 'transaction_purpose_list'
    template_name = 'admin_panel/transaction-purpose/index.html'


class TransactionPurposeCreate(SuccessMessageMixin, CreateView):
    model = TransactionPurpose
    form_class = TransactionPurposeForm
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    success_message = 'Все успешно сохранено!'
    template_name = 'admin_panel/transaction-purpose/create.html'


class TransactionPurposeUpdate(SuccessMessageMixin, UpdateView):
    model = TransactionPurpose
    form_class = TransactionPurposeForm
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    success_message = 'Все успешно сохранено!'
    template_name = 'admin_panel/transaction-purpose/update.html'


class TransactionPurposeDelete(DeleteView):
    model = TransactionPurpose
    success_url = reverse_lazy('admin_panel:transaction_purpose_list')
    template_name = 'admin_panel/transaction-purpose/delete.html'
