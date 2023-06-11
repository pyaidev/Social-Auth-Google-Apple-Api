from django.conf import settings
from django.contrib import admin
from django.core.cache import cache
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from modeltranslation.translator import translator


class ViewCountMixin:
    """Work only with retrieve"""

    view_count_field = "view_count"

    def _count_view(self):
        instance = self.get_object()
        prefix = "view_count"
        model_name = instance.__class__.__name__
        key = f"{prefix}:{model_name}:{instance.pk}:{self.request.fingerprint}"
        data = cache.get(key)
        if not data:
            setattr(instance, self.view_count_field, F(self.view_count_field) + 1)
            instance.save(update_fields=[self.view_count_field])
            cache.set(key, True, settings.VIEW_COUNT_MIN_VIEW_PERIOD)

    def get(self, request, *args, **kwargs):
        self._count_view()
        return super().get(request, *args, **kwargs)


class TabbedTranslationMixin:
    def get_fieldsets(self, request, obj=None):
        if self.model not in translator._registry:
            return super().get_fieldsets(request, obj)
        non_translated_fields = []
        translated_fields = []
        excludes = self.get_exclude(request, obj) or tuple()
        for field in self.get_fields(request, obj):
            if field in excludes:
                continue
            if field in translator._registry[self.model].fields:
                translated_fields.append(field)
            elif all(not field.endswith(lang[0]) for lang in settings.LANGUAGES):
                non_translated_fields.append(field)
        fieldsets = tuple()
        if non_translated_fields:
            fieldsets += ((_("General 💼"), {"fields": non_translated_fields}),)
        for language in settings.LANGUAGES:
            fieldsets += ((language[1], {"fields": list(map(lambda x: x + "_" + language[0], translated_fields))}),)
        return fieldsets


class TabbedTranslationAdmin(TabbedTranslationMixin, admin.ModelAdmin):
    pass


class TranslationRequiredMixin:
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        for value in form.base_fields:
            if value[-2::] in settings.LANGUAGES:
                form.base_fields[value].required = True
        return form
