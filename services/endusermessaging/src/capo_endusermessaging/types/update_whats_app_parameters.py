"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateWhatsAppParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.update_language_code
    import capo_endusermessaging.types.update_whats_app_template_name


class UpdateWhatsAppParameters(TypedDict, closed=True):
    whats_app_template_name: NotRequired[
        "capo_endusermessaging.types.update_whats_app_template_name.UpdateWhatsAppTemplateName"
    ]
    """<p>The updated name of the Meta-approved WhatsApp authentication template. An empty string clears the previously stored value.</p>"""
    language_code: NotRequired[
        "capo_endusermessaging.types.update_language_code.UpdateLanguageCode"
    ]
    """<p>The updated BCP 47 language code. An empty string clears the previously stored value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWhatsAppParameters) -> dict:
    out: dict = {}
    if "whats_app_template_name" in value:
        out["whatsAppTemplateName"] = value["whats_app_template_name"]
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    return out


def deserialize_json(data: dict) -> UpdateWhatsAppParameters:
    out: UpdateWhatsAppParameters = {}  # type: ignore[typeddict-item]
    if data.get("whatsAppTemplateName") is not None:
        out["whats_app_template_name"] = data["whatsAppTemplateName"]
    if data.get("languageCode") is not None:
        out["language_code"] = data["languageCode"]
    return out
