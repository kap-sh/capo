"""Generated from Smithy shape ``com.amazonaws.datazone#BatchGetAttributeOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.attribute_identifier
    import capo_datazone.types.form_output_list


class BatchGetAttributeOutput(TypedDict, closed=True):
    attribute_identifier: "capo_datazone.types.attribute_identifier.AttributeIdentifier"
    """<p>The attribute ID.</p>"""
    forms: NotRequired["capo_datazone.types.form_output_list.FormOutputList"]
    """<p>The metadata forms that are part of the results of the BatchGetAttribute action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttributeOutput) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    if "forms" in value:
        import capo_datazone.types.form_output_list

        out["forms"] = capo_datazone.types.form_output_list.serialize_json(
            value["forms"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetAttributeOutput:
    out: BatchGetAttributeOutput = {}  # type: ignore[typeddict-item]
    if data.get("attributeIdentifier") is not None:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        raise DeserializationError(
            "BatchGetAttributeOutput.attribute_identifier required"
        )
    if data.get("forms") is not None:
        import capo_datazone.types.form_output_list

        out["forms"] = capo_datazone.types.form_output_list.deserialize_json(
            data["forms"]
        )
    return out


def redact_sensitive(value: BatchGetAttributeOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "forms" in value:
        import capo_datazone.types.form_output_list

        out["forms"] = capo_datazone.types.form_output_list.redact_sensitive(
            value["forms"]
        )
    return out
