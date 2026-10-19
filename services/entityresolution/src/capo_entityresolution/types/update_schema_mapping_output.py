"""Generated from Smithy shape ``com.amazonaws.entityresolution#UpdateSchemaMappingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.schema_input_attributes
    import capo_entityresolution.types.schema_mapping_arn


class UpdateSchemaMappingOutput(TypedDict, closed=True):
    schema_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema.</p>"""
    schema_arn: "capo_entityresolution.types.schema_mapping_arn.SchemaMappingArn"
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>SchemaMapping</code>.</p>"""
    description: NotRequired["capo_entityresolution.types.description.Description"]
    """<p>A description of the schema.</p>"""
    mapped_input_fields: (
        "capo_entityresolution.types.schema_input_attributes.SchemaInputAttributes"
    )
    """<p>A list of <code>MappedInputFields</code>. Each <code>MappedInputField</code> corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSchemaMappingOutput) -> dict:
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
    return out


def deserialize_json(data: dict) -> UpdateSchemaMappingOutput:
    out: UpdateSchemaMappingOutput = {}  # type: ignore[typeddict-item]
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
    return out
