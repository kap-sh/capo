"""Generated from Smithy shape ``com.amazonaws.qconnect#WhatsAppMessageTemplateSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.whats_app_business_account_id
    import capo_qconnect.types.whats_app_message_template_components
    import capo_qconnect.types.whats_app_message_template_id


class WhatsAppMessageTemplateSourceConfiguration(TypedDict, closed=True):
    business_account_id: (
        "capo_qconnect.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    )
    """<p>The ID of the End User Messaging WhatsApp Business Account to associate with this template.</p>"""
    template_id: (
        "capo_qconnect.types.whats_app_message_template_id.WhatsAppMessageTemplateId"
    )
    """<p>The WhatsApp template ID.</p>"""
    components: NotRequired[
        "capo_qconnect.types.whats_app_message_template_components.WhatsAppMessageTemplateComponents"
    ]
    """<p>The list of component mapping from WhatsApp template parameters to Message Template attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppMessageTemplateSourceConfiguration) -> dict:
    out: dict = {}
    out["businessAccountId"] = value["business_account_id"]
    out["templateId"] = value["template_id"]
    if "components" in value:
        import capo_qconnect.types.whats_app_message_template_components

        out["components"] = (
            capo_qconnect.types.whats_app_message_template_components.serialize_json(
                value["components"]
            )
        )
    return out


def deserialize_json(data: dict) -> WhatsAppMessageTemplateSourceConfiguration:
    out: WhatsAppMessageTemplateSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("businessAccountId") is not None:
        out["business_account_id"] = data["businessAccountId"]
    else:
        out["business_account_id"] = ""
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        out["template_id"] = ""
    if data.get("components") is not None:
        import capo_qconnect.types.whats_app_message_template_components

        out["components"] = (
            capo_qconnect.types.whats_app_message_template_components.deserialize_json(
                data["components"]
            )
        )
    return out
