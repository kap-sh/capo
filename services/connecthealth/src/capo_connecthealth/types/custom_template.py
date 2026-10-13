"""Generated from Smithy shape ``com.amazonaws.connecthealth#CustomTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.custom_template_base
    import capo_connecthealth.types.template_instructions


class CustomTemplate(TypedDict, closed=True):
    template_type: "capo_connecthealth.types.custom_template_base.CustomTemplateBase"
    """<p>The base template type to customize</p>"""
    template_instructions: (
        "capo_connecthealth.types.template_instructions.TemplateInstructions"
    )
    """<p>Custom instructions for each section of the template</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomTemplate) -> dict:
    out: dict = {}
    import capo_connecthealth.types.custom_template_base

    out["templateType"] = capo_connecthealth.types.custom_template_base.serialize_json(
        value["template_type"]
    )
    import capo_connecthealth.types.template_instructions

    out["templateInstructions"] = (
        capo_connecthealth.types.template_instructions.serialize_json(
            value["template_instructions"]
        )
    )
    return out


def deserialize_json(data: dict) -> CustomTemplate:
    out: CustomTemplate = {}  # type: ignore[typeddict-item]
    if data.get("templateType") is not None:
        import capo_connecthealth.types.custom_template_base

        out["template_type"] = (
            capo_connecthealth.types.custom_template_base.deserialize_json(
                data["templateType"]
            )
        )
    else:
        raise DeserializationError("CustomTemplate.template_type required")
    if data.get("templateInstructions") is not None:
        import capo_connecthealth.types.template_instructions

        out["template_instructions"] = (
            capo_connecthealth.types.template_instructions.deserialize_json(
                data["templateInstructions"]
            )
        )
    else:
        raise DeserializationError("CustomTemplate.template_instructions required")
    return out


def redact_sensitive(value: CustomTemplate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template_instructions" in value:
        import capo_connecthealth.types.template_instructions

        out["template_instructions"] = (
            capo_connecthealth.types.template_instructions.redact_sensitive(
                value["template_instructions"]
            )
        )
    return out
