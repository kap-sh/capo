"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppMessageTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.meta_template_definition


class CreateWhatsAppMessageTemplateInput(TypedDict, closed=True):
    template_definition: (
        "capo_socialmessaging.types.meta_template_definition.MetaTemplateDefinition"
    )
    """<p>The complete template definition as a JSON blob.</p>"""
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to associate with this template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppMessageTemplateInput) -> dict:
    out: dict = {}
    import capo_socialmessaging.types.meta_template_definition

    out["templateDefinition"] = (
        capo_socialmessaging.types.meta_template_definition.serialize_json(
            value["template_definition"]
        )
    )
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppMessageTemplateInput:
    out: CreateWhatsAppMessageTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("templateDefinition") is not None:
        import capo_socialmessaging.types.meta_template_definition

        out["template_definition"] = (
            capo_socialmessaging.types.meta_template_definition.deserialize_json(
                data["templateDefinition"]
            )
        )
    else:
        out["template_definition"] = b""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
