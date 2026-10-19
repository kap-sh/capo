"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingWorkflowInputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.id_namespace_type
    import capo_entityresolution.types.input_source_arn


class IdMappingWorkflowInputSource(TypedDict, closed=True):
    input_source_arn: "capo_entityresolution.types.input_source_arn.InputSourceARN"
    """<p>An Glue table Amazon Resource Name (ARN) or a matching workflow ARN for the input source table.</p>"""
    schema_name: NotRequired["capo_entityresolution.types.entity_name.EntityName"]
    """<p>The name of the schema to be retrieved.</p>"""
    type: NotRequired["capo_entityresolution.types.id_namespace_type.IdNamespaceType"]
    """<p>The type of ID namespace. There are two types: <code>SOURCE</code> and <code>TARGET</code>. </p> <p>The <code>SOURCE</code> contains configurations for <code>sourceId</code> data that will be processed in an ID mapping workflow. </p> <p>The <code>TARGET</code> contains a configuration of <code>targetId</code> which all <code>sourceIds</code> will resolve to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingWorkflowInputSource) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    if "schema_name" in value:
        out["schemaName"] = value["schema_name"]
    if "type" in value:
        import capo_entityresolution.types.id_namespace_type

        out["type"] = capo_entityresolution.types.id_namespace_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> IdMappingWorkflowInputSource:
    out: IdMappingWorkflowInputSource = {}  # type: ignore[typeddict-item]
    if data.get("inputSourceARN") is not None:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        out["input_source_arn"] = ""
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    if data.get("type") is not None:
        import capo_entityresolution.types.id_namespace_type

        out["type"] = capo_entityresolution.types.id_namespace_type.deserialize_json(
            data["type"]
        )
    return out
