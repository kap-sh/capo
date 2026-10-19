"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetSchemaMappingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.schema_input_attributes
    import capo_entityresolution.types.schema_mapping_arn
    import capo_entityresolution.types.tag_map


class GetSchemaMappingOutput(TypedDict, closed=True):
    schema_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema.</p>"""
    schema_arn: "capo_entityresolution.types.schema_mapping_arn.SchemaMappingArn"
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the SchemaMapping.</p>"""
    description: NotRequired["capo_entityresolution.types.description.Description"]
    """<p>A description of the schema.</p>"""
    mapped_input_fields: (
        "capo_entityresolution.types.schema_input_attributes.SchemaInputAttributes"
    )
    """<p>A list of <code>MappedInputFields</code>. Each <code>MappedInputField</code> corresponds to a column the source data table, and contains column name plus additional information Entity Resolution uses for matching.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the <code>SchemaMapping</code> was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the <code>SchemaMapping</code> was last updated.</p>"""
    tags: NotRequired["capo_entityresolution.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    has_workflows: "bool"
    """<p>Specifies whether the schema mapping has been applied to a workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaMappingOutput) -> dict:
    out: dict = {}
    out["schemaName"] = value["schema_name"]
    out["schemaArn"] = value["schema_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_entityresolution.types.schema_input_attributes

    out["mappedInputFields"] = (
        capo_entityresolution.types.schema_input_attributes.serialize_json(
            value["mapped_input_fields"]
        )
    )
    import capo_entityresolution.types._prelude.timestamp

    out["createdAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_entityresolution.types._prelude.timestamp

    out["updatedAt"] = capo_entityresolution.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "tags" in value:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.serialize_json(value["tags"])
    out["hasWorkflows"] = value["has_workflows"]
    return out


def deserialize_json(data: dict) -> GetSchemaMappingOutput:
    out: GetSchemaMappingOutput = {}  # type: ignore[typeddict-item]
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    else:
        out["schema_name"] = ""
    if data.get("schemaArn") is not None:
        out["schema_arn"] = data["schemaArn"]
    else:
        out["schema_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("mappedInputFields") is not None:
        import capo_entityresolution.types.schema_input_attributes

        out["mapped_input_fields"] = (
            capo_entityresolution.types.schema_input_attributes.deserialize_json(
                data["mappedInputFields"]
            )
        )
    else:
        out["mapped_input_fields"] = []
    if data.get("createdAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["created_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_entityresolution.types._prelude.timestamp

        out["updated_at"] = (
            capo_entityresolution.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("tags") is not None:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.deserialize_json(data["tags"])
    if data.get("hasWorkflows") is not None:
        out["has_workflows"] = data["hasWorkflows"]
    else:
        out["has_workflows"] = False
    return out
