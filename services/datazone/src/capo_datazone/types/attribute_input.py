"""Generated from Smithy shape ``com.amazonaws.datazone#AttributeInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attribute_identifier
    import capo_datazone.types.form_input_list


class AttributeInput(TypedDict, closed=True):
    attribute_identifier: "capo_datazone.types.attribute_identifier.AttributeIdentifier"
    """<p>The ID of the attribute.</p>"""
    forms: "capo_datazone.types.form_input_list.FormInputList"
    """<p>The metadata forms as part of the attribute input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeInput) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    import capo_datazone.types.form_input_list

    out["forms"] = capo_datazone.types.form_input_list.serialize_json(value["forms"])
    return out


def deserialize_json(data: dict) -> AttributeInput:
    out: AttributeInput = {}  # type: ignore[typeddict-item]
    if data.get("attributeIdentifier") is not None:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        out["attribute_identifier"] = ""
    if data.get("forms") is not None:
        import capo_datazone.types.form_input_list

        out["forms"] = capo_datazone.types.form_input_list.deserialize_json(
            data["forms"]
        )
    else:
        out["forms"] = []
    return out


def redact_sensitive(value: AttributeInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "forms" in value:
        out["forms"] = "*** Sensitive Data Redacted ***"
    return out
