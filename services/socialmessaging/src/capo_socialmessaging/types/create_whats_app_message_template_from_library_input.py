"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppMessageTemplateFromLibraryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_library_template


class CreateWhatsAppMessageTemplateFromLibraryInput(TypedDict, closed=True):
    meta_library_template: (
        "capo_socialmessaging.types.meta_library_template.MetaLibraryTemplate"
    )
    """<p>The template configuration from Meta's library, including customizations for buttons and body text.</p>"""
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to associate with this template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppMessageTemplateFromLibraryInput) -> dict:
    out: dict = {}
    import capo_socialmessaging.types.meta_library_template

    out["metaLibraryTemplate"] = (
        capo_socialmessaging.types.meta_library_template.serialize_json(
            value["meta_library_template"]
        )
    )
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppMessageTemplateFromLibraryInput:
    out: CreateWhatsAppMessageTemplateFromLibraryInput = {}  # type: ignore[typeddict-item]
    if data.get("metaLibraryTemplate") is not None:
        import capo_socialmessaging.types.meta_library_template

        out["meta_library_template"] = (
            capo_socialmessaging.types.meta_library_template.deserialize_json(
                data["metaLibraryTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWhatsAppMessageTemplateFromLibraryInput.meta_library_template required"
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
