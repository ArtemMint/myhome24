"""
Views of site data
"""

# from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView


from .. import models
from .. import forms


class IndexUpdate(SuccessMessageMixin, View):
    """
    Index page view class
    """
    template_name = 'admin_panel/manage_site/index.html'

    def get_object(self):
        """
        Get index page data
        """
        obj = models.IndexPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
        return obj

    def get(self, request, *args, **kwargs):
        """
        GET method logic
        """
        index_page = self.get_object()
        index_form = forms.IndexPageForm(
            instance=index_page
        )
        slider_formset = forms.IndexSliderFormset(
            instance=index_page,
        )
        block_formset = forms.IndexBlockFormset(
            instance=index_page,
        )
        seo_form = forms.SEOForm(
            instance=index_page.seo,
        )
        return render(
            request,
            self.template_name,
            {
                'index_page': index_page,
                'slider_formset': slider_formset,
                'index_form': index_form,
                'block_formset': block_formset,
                'seo_form': seo_form,
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Post method logic
        """
        index_page = self.get_object()
        index_form = forms.IndexPageForm(
            request.POST,
            instance=index_page,
        )
        slider_formset = forms.IndexSliderFormset(
            request.POST,
            request.FILES,
            instance=index_page,
        )
        block_formset = forms.IndexBlockFormset(
            request.POST,
            request.FILES,
            instance=index_page,
        )
        seo_form = forms.SEOForm(
            request.POST,
            instance=index_page.seo,
        )
        if (
                index_form.is_valid() and
                slider_formset.is_valid() and
                block_formset.is_valid() and
                seo_form.is_valid()
        ):
            index_form.save()
            slider_formset.save()
            block_formset.save()
            seo_form.save()
            return redirect('admin_panel:index')
        return render(
            request,
            self.template_name,
            {
                'index_page': index_page,
                'slider_formset': slider_formset,
                'index_form': index_form,
                'block_formset': block_formset,
                'seo_form': seo_form,
            }
        )


class AboutSettings(TemplateView):
    template_name = 'admin_panel/manage_site/about.html'

    def get_object(self):
        """
        Get about page data
        """
        obj = models.AboutPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
        return obj

    def get(self, request, *args, **kwargs):
        about_page: models.AboutPage = self.get_object()
        about_form = forms.AboutPageForm(
            instance=about_page,
        )
        gallery_formset = forms.AboutGalleryFormset(
            instance=about_page,
        )
        extra_info_formset = forms.AboutExtraInfoFormset(
            instance=about_page,
        )
        extra_gallery_formset = forms.AboutExtraGalleryFormset(
            instance=about_page,
        )
        extra_document_formset = forms.AboutDocumentFormset(
            instance=about_page,
        )
        seo_form = forms.SEOForm(
            instance=about_page.seo,
        )
        return render(
            request,
            self.template_name,
            {
                'about_page': about_page,
                'about_form': about_form,
                'gallery_formset': gallery_formset,
                'extra_info_formset': extra_info_formset,
                'extra_gallery_formset': extra_gallery_formset,
                'extra_document_formset': extra_document_formset,
                'documents': models.AboutDocument.objects.all(),
                'seo_form': seo_form,
            }
        )

    def post(self, request, *args, **kwargs):
        about_page = self.get_object()
        about_form = forms.AboutPageForm(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        gallery_formset = forms.AboutGalleryFormset(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        extra_info_formset = forms.AboutExtraInfoFormset(
            request.POST,
            instance=about_page,
        )
        extra_gallery_formset = forms.AboutExtraGalleryFormset(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        document_formset = forms.AboutDocumentFormset(
            request.POST,
            request.FILES,
            instance=about_page,
        )
        seo_form = forms.SEOForm(
            request.POST,
            instance=about_page.seo,
        )
        if (
                about_form.is_valid() and
                gallery_formset.is_valid() and
                extra_info_formset.is_valid() and
                extra_gallery_formset.is_valid() and
                document_formset.is_valid() and
                seo_form.is_valid()
        ):
            about_form.save()
            gallery_formset.save()
            extra_info_formset.save()
            extra_gallery_formset.save()
            document_formset.save()
            seo_form.save()
            return redirect('admin_panel:about')
        return render(
            request,
            self.template_name,
            {
                'about_page': about_page,
                'about_form': about_form,
                'gallery_formset': gallery_formset,
                'extra_info_formset': extra_info_formset,
                'extra_gallery_formset': extra_gallery_formset,
                'extra_document_formset': document_formset,
                'documents': models.AboutDocument.objects.all(),
                'seo_form': seo_form,
            }
        )


class ServicesSettings(SuccessMessageMixin, UpdateView):
    """
    Services page settings
    """
    model = models.ServicesPage
    form_class = forms.ServicesForm
    formset_class = forms.ServicesFormset
    second_form_class = forms.SEOForm
    success_url = reverse_lazy('admin_panel:services')
    success_message = 'All data successfully updated!'
    template_name = 'admin_panel/manage_site/services.html'

    def __init__(self):
        super(ServicesSettings, self).__init__()
        self.object = self.get_object()

    def get_object(self, queryset=None):
        """
        Get services page data
        """
        obj = models.ServicesPage.get_solo()
        if not obj.seo:
            obj.seo = models.SEO.objects.create()
            obj.save()
        return obj

    def get_context_data(self, **kwargs):
        """
        Get context to render forms in page
        """
        context = super(ServicesSettings, self).get_context_data(**kwargs)
        context['services_formset'] = self.formset_class()
        context['seo_form'] = self.second_form_class(
            instance=self.object.seo,
        )
        return context

    def form_valid(self, formset, form):
        """
        If form valid
        """
        formset.save()
        form.save()
        return super(ServicesSettings, self).form_valid(form)

    def form_invalid(self, form):
        """
        If form invalid
        """
        return self.render_to_response(
            self.get_context_data(
                services_formset=self.formset_class,
                seo_form=self.second_form_class,
            )
        )

    def get(self, request, *args, **kwargs):
        """
        GET method
        """
        super(ServicesSettings, self).get(request, *args, **kwargs)
        return self.render_to_response(
            self.get_context_data(
                object=self.object,
                services_formset=self.formset_class,
                seo_form=self.second_form_class,
            )
        )

    def post(self, request, *args, **kwargs):
        """
        POST method
        """
        formset = self.formset_class(
            request.POST,
            request.FILES,
        )
        form = self.second_form_class(
            request.POST,
            instance=self.object.seo,
        )
        if formset.is_valid() and form.is_valid():
            return self.form_valid(formset, form)
        else:
            return self.form_invalid(*args)


class TariffsSettings(TemplateView):
    template_name = 'admin_panel/manage_site/tariffs.html'


class ContactsSettings(TemplateView):
    template_name = 'admin_panel/manage_site/contacts.html'
