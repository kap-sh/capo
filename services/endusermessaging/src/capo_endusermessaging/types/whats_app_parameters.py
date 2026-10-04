"""Generated from Smithy shape ``com.amazonaws.endusermessaging#WhatsAppParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.language_code
    import capo_endusermessaging.types.whats_app_template_name


class WhatsAppParameters(TypedDict, closed=True):
    whats_app_template_name: NotRequired[
        "capo_endusermessaging.types.whats_app_template_name.WhatsAppTemplateName"
    ]
    """<p>The name of the Meta-approved WhatsApp authentication template.</p>"""
    language_code: NotRequired["capo_endusermessaging.types.language_code.LanguageCode"]
    """<p>The BCP 47 language code used to render the template. This value is required for the WhatsApp channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppParameters) -> dict:
    out: dict = {}
    if "whats_app_template_name" in value:
        out["whatsAppTemplateName"] = value["whats_app_template_name"]
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    return out


def deserialize_json(data: dict) -> WhatsAppParameters:
    out: WhatsAppParameters = {}  # type: ignore[typeddict-item]
    if data.get("whatsAppTemplateName") is not None:
        out["whats_app_template_name"] = data["whatsAppTemplateName"]
    if data.get("languageCode") is not None:
        out["language_code"] = data["languageCode"]
    return out
