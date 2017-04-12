from django.utils.encoding import force_text, iri_to_uri
from django.utils.http import quote, quote_plus
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore import blocks
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class AbstractLinkBlock(blocks.StructBlock):
    url_append = blocks.CharBlock(
        required=False,
        help_text=_(
            "Use this to optionally append a #hash"
            "or querystring to the above page's URL."
        ),
        max_length=255,
    )

    class Meta:
        icon = 'link'
        template = 'streammenu/link_block.html'


class CustomLinkBlock(AbstractLinkBlock):
    title = blocks.CharBlock(required=True)
    link = blocks.URLBlock()
    open_in_new_tab = blocks.BooleanBlock(required=False, default=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['value']['caption'] = value['title']
        if value['url_append']:
            context['value']['url'] = iri_to_uri(
                value['link'] + value['url_append']
            )
        else:
            context['value']['url'] = iri_to_uri(value['link'])
        return context


class PageLinkBlock(AbstractLinkBlock):
    title = blocks.CharBlock(required=False)
    page = blocks.PageChooserBlock()
    open_in_new_tab = blocks.BooleanBlock(required=False, default=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        if value['title']:
            context['value']['caption'] = value['title']
        else:
            context['value']['caption'] = value['page'].title
        if value['url_append']:
            context['value']['url'] = iri_to_uri(
                value['page'].url + value['url_append']
            )
        else:
            context['value']['url'] = value['page'].url
        return context


class DocumentLinkBlock(AbstractLinkBlock):
    title = blocks.CharBlock(required=False)
    document = DocumentChooserBlock()
    open_in_new_tab = blocks.BooleanBlock(required=False, default=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        if value['title']:
            context['value']['caption'] = value['title']
        else:
            context['value']['caption'] = value['document'].title
        if value['url_append']:
            context['value']['url'] = iri_to_uri(
                value['document'].url + value['url_append']
            )
        else:
            context['value']['url'] = value['document'].url
        return context
