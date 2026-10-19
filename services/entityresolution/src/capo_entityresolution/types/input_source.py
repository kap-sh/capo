"""Generated from Smithy shape ``com.amazonaws.entityresolution#InputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.input_source_arn


class InputSource(TypedDict, closed=True):
    input_source_arn: "capo_entityresolution.types.input_source_arn.InputSourceARN"
    """<p>An Glue table Amazon Resource Name (ARN) for the input source table.</p>"""
    schema_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema to be retrieved.</p>"""
    apply_normalization: NotRequired["bool"]
    """<p>Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an <code>AttributeType</code> of <code>PHONE_NUMBER</code>, and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSource) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    out["schemaName"] = value["schema_name"]
    if "apply_normalization" in value:
        out["applyNormalization"] = value["apply_normalization"]
    return out


def deserialize_json(data: dict) -> InputSource:
    out: InputSource = {}  # type: ignore[typeddict-item]
    if data.get("inputSourceARN") is not None:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        out["input_source_arn"] = ""
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    else:
        out["schema_name"] = ""
    if data.get("applyNormalization") is not None:
        out["apply_normalization"] = data["applyNormalization"]
    return out
