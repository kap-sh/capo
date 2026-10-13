"""Generated from Smithy shape ``com.amazonaws.qconnect#WhatsAppMessageTemplateSourceConfigurationSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_unlimited_string
    import capo_qconnect.types.whats_app_business_account_id
    import capo_qconnect.types.whats_app_message_template_components
    import capo_qconnect.types.whats_app_message_template_id
    import capo_qconnect.types.whats_app_message_template_language
    import capo_qconnect.types.whats_app_message_template_name
    import capo_qconnect.types.whats_app_source_configuration_status


class WhatsAppMessageTemplateSourceConfigurationSummary(TypedDict, closed=True):
    business_account_id: (
        "capo_qconnect.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    )
    """<p>The ID of the End User Messaging WhatsApp Business Account to associate with this template.</p>"""
    template_id: (
        "capo_qconnect.types.whats_app_message_template_id.WhatsAppMessageTemplateId"
    )
    """<p>The ID of WhatsApp template.</p>"""
    name: NotRequired[
        "capo_qconnect.types.whats_app_message_template_name.WhatsAppMessageTemplateName"
    ]
    """<p>The name of the WhatsApp template.</p>"""
    language: NotRequired[
        "capo_qconnect.types.whats_app_message_template_language.WhatsAppMessageTemplateLanguage"
    ]
    """<p>The language of the WhatsApp template.</p>"""
    components: NotRequired[
        "capo_qconnect.types.whats_app_message_template_components.WhatsAppMessageTemplateComponents"
    ]
    """<p>The list of component mapping from WhatsApp template parameters to Message Template attributes.</p>"""
    status: NotRequired[
        "capo_qconnect.types.whats_app_source_configuration_status.WhatsAppSourceConfigurationStatus"
    ]
    """<p>The status of the message template.</p>"""
    status_reason: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The status reason of the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppMessageTemplateSourceConfigurationSummary) -> dict:
    out: dict = {}
    out["businessAccountId"] = value["business_account_id"]
    out["templateId"] = value["template_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "language" in value:
        out["language"] = value["language"]
    if "components" in value:
        import capo_qconnect.types.whats_app_message_template_components

        out["components"] = (
            capo_qconnect.types.whats_app_message_template_components.serialize_json(
                value["components"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> WhatsAppMessageTemplateSourceConfigurationSummary:
    out: WhatsAppMessageTemplateSourceConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("businessAccountId") is not None:
        out["business_account_id"] = data["businessAccountId"]
    else:
        raise DeserializationError(
            "WhatsAppMessageTemplateSourceConfigurationSummary.business_account_id required"
        )
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError(
            "WhatsAppMessageTemplateSourceConfigurationSummary.template_id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("components") is not None:
        import capo_qconnect.types.whats_app_message_template_components

        out["components"] = (
            capo_qconnect.types.whats_app_message_template_components.deserialize_json(
                data["components"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out


def redact_sensitive(
    value: WhatsAppMessageTemplateSourceConfigurationSummary,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "status_reason" in value:
        out["status_reason"] = "*** Sensitive Data Redacted ***"
    return out
