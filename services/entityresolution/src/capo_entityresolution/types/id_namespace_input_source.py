"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceInputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.input_source_arn


class IdNamespaceInputSource(TypedDict, closed=True):
    input_source_arn: "capo_entityresolution.types.input_source_arn.InputSourceARN"
    """<p>An Glue table Amazon Resource Name (ARN) or a matching workflow ARN for the input source table.</p>"""
    schema_name: NotRequired["capo_entityresolution.types.entity_name.EntityName"]
    """<p>The name of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceInputSource) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    return out


def deserialize_json(data: dict) -> IdNamespaceInputSource:
    out: IdNamespaceInputSource = {}  # type: ignore[typeddict-item]
    if data.get("inputSourceARN") is not None:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        out["input_source_arn"] = ""
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    return out
