"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UpdateWhatsAppMessageTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_parameter_format
    import capo_socialmessaging.types.meta_template_category
    import capo_socialmessaging.types.meta_template_components
    import capo_socialmessaging.types.meta_template_cta_link_tracking_opted_out
    import capo_socialmessaging.types.meta_template_id
    import capo_socialmessaging.types.meta_template_language
    import capo_socialmessaging.types.meta_template_name


class UpdateWhatsAppMessageTemplateInput(TypedDict, closed=True):
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this template.</p>"""
    meta_template_id: NotRequired[
        "capo_socialmessaging.types.meta_template_id.MetaTemplateId"
    ]
    """<p>The numeric ID of the template assigned by Meta.</p>"""
    template_name: NotRequired[
        "capo_socialmessaging.types.meta_template_name.MetaTemplateName"
    ]
    """<p>The name of the message template. Use together with <code>templateLanguageCode</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>"""
    template_language_code: NotRequired[
        "capo_socialmessaging.types.meta_template_language.MetaTemplateLanguage"
    ]
    """<p>The language code of the message template (for example, <code>en</code> or <code>en_US</code>). Use together with <code>templateName</code> as an alternative to <code>metaTemplateId</code> to identify a template.</p>"""
    parameter_format: NotRequired[
        "capo_socialmessaging.types.meta_parameter_format.MetaParameterFormat"
    ]
    """<p>The format specification for parameters in the template, this can be either 'named' or 'positional'.</p>"""
    template_category: NotRequired[
        "capo_socialmessaging.types.meta_template_category.MetaTemplateCategory"
    ]
    """<p>The new category for the template (for example, UTILITY or MARKETING).</p>"""
    template_components: NotRequired[
        "capo_socialmessaging.types.meta_template_components.MetaTemplateComponents"
    ]
    """<p>The updated components of the template as a JSON blob (maximum 3000 characters).</p>"""
    cta_url_link_tracking_opted_out: NotRequired[
        "capo_socialmessaging.types.meta_template_cta_link_tracking_opted_out.MetaTemplateCtaLinkTrackingOptedOut"
    ]
    """<p>When true, disables click tracking for call-to-action URL buttons in the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppMessageTemplateInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "meta_template_id" in value:
        out["metaTemplateId"] = value["meta_template_id"]
    if "template_name" in value:
        out["templateName"] = value["template_name"]
    if "template_language_code" in value:
        out["templateLanguageCode"] = value["template_language_code"]
    if "parameter_format" in value:
        out["parameterFormat"] = value["parameter_format"]
    if "template_category" in value:
        out["templateCategory"] = value["template_category"]
    if "template_components" in value:
        import capo_socialmessaging.types.meta_template_components

        out["templateComponents"] = (
            capo_socialmessaging.types.meta_template_components.serialize_json(
                value["template_components"]
            )
        )
    if "cta_url_link_tracking_opted_out" in value:
        out["ctaUrlLinkTrackingOptedOut"] = value["cta_url_link_tracking_opted_out"]
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppMessageTemplateInput:
    out: UpdateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("metaTemplateId") is not None:
        out["meta_template_id"] = data["metaTemplateId"]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    if data.get("templateLanguageCode") is not None:
        out["template_language_code"] = data["templateLanguageCode"]
    if data.get("parameterFormat") is not None:
        out["parameter_format"] = data["parameterFormat"]
    if data.get("templateCategory") is not None:
        out["template_category"] = data["templateCategory"]
    if data.get("templateComponents") is not None:
        import capo_socialmessaging.types.meta_template_components

        out["template_components"] = (
            capo_socialmessaging.types.meta_template_components.deserialize_json(
                data["templateComponents"]
            )
        )
    if data.get("ctaUrlLinkTrackingOptedOut") is not None:
        out["cta_url_link_tracking_opted_out"] = data["ctaUrlLinkTrackingOptedOut"]
    return out
