"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetMatchIdInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.record_attribute_map


class GetMatchIdInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    record: "capo_entityresolution.types.record_attribute_map.RecordAttributeMap"
    """<p>The record to fetch the Match ID for.</p>"""
    apply_normalization: "bool"
    """<p>Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an <code>AttributeType</code> of <code>PHONE_NUMBER</code>, and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMatchIdInput) -> dict:
    out: dict = {}
    import capo_entityresolution.types.record_attribute_map

    out["record"] = capo_entityresolution.types.record_attribute_map.serialize_json(
        value["record"]
    )
    out["applyNormalization"] = value.get("apply_normalization", True)
    return out


def deserialize_json(data: dict) -> GetMatchIdInput:
    out: GetMatchIdInput = {}  # type: ignore[typeddict-item]
    if data.get("record") is not None:
        import capo_entityresolution.types.record_attribute_map

        out["record"] = (
            capo_entityresolution.types.record_attribute_map.deserialize_json(
                data["record"]
            )
        )
    else:
        raise DeserializationError("GetMatchIdInput.record required")
    if data.get("applyNormalization") is not None:
        out["apply_normalization"] = data["applyNormalization"]
    else:
        out["apply_normalization"] = True
    return out


def redact_sensitive(value: GetMatchIdInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "record" in value:
        out["record"] = "*** Sensitive Data Redacted ***"
    return out
