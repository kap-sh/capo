"""Generated from Smithy shape ``com.amazonaws.glue#CreateSchemaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.compatibility
    import capo_glue.types.data_format
    import capo_glue.types.description_string
    import capo_glue.types.registry_id
    import capo_glue.types.schema_definition_string
    import capo_glue.types.schema_registry_name_string
    import capo_glue.types.tags_map


class CreateSchemaInput(TypedDict, closed=True):
    registry_id: NotRequired["capo_glue.types.registry_id.RegistryId"]
    """<p> This is a wrapper shape to contain the registry identity fields. If this is not provided, the default registry will be used. The ARN format for the same will be: <code>arn:aws:glue:us-east-2:<customer id>:registry/default-registry:random-5-letter-id</code>.</p>"""
    schema_name: "capo_glue.types.schema_registry_name_string.SchemaRegistryNameString"
    """<p>Name of the schema to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.</p>"""
    data_format: "capo_glue.types.data_format.DataFormat"
    """<p>The data format of the schema definition. Currently <code>AVRO</code>, <code>JSON</code> and <code>PROTOBUF</code> are supported.</p>"""
    compatibility: NotRequired["capo_glue.types.compatibility.Compatibility"]
    """<p>The compatibility mode of the schema. The possible values are:</p> <ul> <li> <p> <i>NONE</i>: No compatibility mode applies. You can use this choice in development scenarios or if you do not know the compatibility mode that you want to apply to schemas. Any new version added will be accepted without undergoing a compatibility check.</p> </li> <li> <p> <i>DISABLED</i>: This compatibility choice prevents versioning for a particular schema. You can use this choice to prevent future versioning of a schema.</p> </li> <li> <p> <i>BACKWARD</i>: This compatibility choice is recommended as it allows data receivers to read both the current and one previous schema version. This means that for instance, a new schema version cannot drop data fields or change the type of these fields, so they can't be read by readers using the previous version.</p> </li> <li> <p> <i>BACKWARD_ALL</i>: This compatibility choice allows data receivers to read both the current and all previous schema versions. You can use this choice when you need to delete fields or add optional fields, and check compatibility against all previous schema versions. </p> </li> <li> <p> <i>FORWARD</i>: This compatibility choice allows data receivers to read both the current and one next schema version, but not necessarily later versions. You can use this choice when you need to add fields or delete optional fields, but only check compatibility against the last schema version.</p> </li> <li> <p> <i>FORWARD_ALL</i>: This compatibility choice allows data receivers to read written by producers of any new registered schema. You can use this choice when you need to add fields or delete optional fields, and check compatibility against all previous schema versions.</p> </li> <li> <p> <i>FULL</i>: This compatibility choice allows data receivers to read data written by producers using the previous or next version of the schema, but not necessarily earlier or later versions. You can use this choice when you need to add or remove optional fields, but only check compatibility against the last schema version.</p> </li> <li> <p> <i>FULL_ALL</i>: This compatibility choice allows data receivers to read data written by producers using all previous schema versions. You can use this choice when you need to add or remove optional fields, and check compatibility against all previous schema versions.</p> </li> </ul>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>An optional description of the schema. If description is not provided, there will not be any automatic default value for this.</p>"""
    tags: NotRequired["capo_glue.types.tags_map.TagsMap"]
    """<p>Amazon Web Services tags that contain a key value pair and may be searched by console, command line, or API. If specified, follows the Amazon Web Services tags-on-create pattern.</p>"""
    schema_definition: NotRequired[
        "capo_glue.types.schema_definition_string.SchemaDefinitionString"
    ]
    """<p>The schema definition using the <code>DataFormat</code> setting for <code>SchemaName</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSchemaInput) -> dict:
    out: dict = {}
    if "registry_id" in value:
        import capo_glue.types.registry_id

        out["RegistryId"] = capo_glue.types.registry_id.serialize_aws_json_1_1(
            value["registry_id"]
        )
    out["SchemaName"] = value["schema_name"]
    import capo_glue.types.data_format

    out["DataFormat"] = capo_glue.types.data_format.serialize_aws_json_1_1(
        value["data_format"]
    )
    if "compatibility" in value:
        import capo_glue.types.compatibility

        out["Compatibility"] = capo_glue.types.compatibility.serialize_aws_json_1_1(
            value["compatibility"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_glue.types.tags_map

        out["Tags"] = capo_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    if "schema_definition" in value:
        out["SchemaDefinition"] = value["schema_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSchemaInput:
    out: CreateSchemaInput = {}  # type: ignore[typeddict-item]
    if data.get("RegistryId") is not None:
        import capo_glue.types.registry_id

        out["registry_id"] = capo_glue.types.registry_id.deserialize_aws_json_1_1(
            data["RegistryId"]
        )
    if data.get("SchemaName") is not None:
        out["schema_name"] = data["SchemaName"]
    else:
        out["schema_name"] = ""
    if data.get("DataFormat") is not None:
        import capo_glue.types.data_format

        out["data_format"] = capo_glue.types.data_format.deserialize_aws_json_1_1(
            data["DataFormat"]
        )
    else:
        import typing

        out["data_format"] = typing.cast("capo_glue.types.data_format.DataFormat", "")
    if data.get("Compatibility") is not None:
        import capo_glue.types.compatibility

        out["compatibility"] = capo_glue.types.compatibility.deserialize_aws_json_1_1(
            data["Compatibility"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_glue.types.tags_map

        out["tags"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    if data.get("SchemaDefinition") is not None:
        out["schema_definition"] = data["SchemaDefinition"]
    return out
