"""Generated from Smithy shape ``com.amazonaws.glue#GetSchemaByDefinitionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.schema_definition_string
    import capo_glue.types.schema_id


class GetSchemaByDefinitionInput(TypedDict, closed=True):
    schema_id: "capo_glue.types.schema_id.SchemaId"
    """<p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> </ul>"""
    schema_definition: "capo_glue.types.schema_definition_string.SchemaDefinitionString"
    """<p>The definition of the schema for which schema details are required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSchemaByDefinitionInput) -> dict:
    out: dict = {}
    import capo_glue.types.schema_id

    out["SchemaId"] = capo_glue.types.schema_id.serialize_aws_json_1_1(
        value["schema_id"]
    )
    out["SchemaDefinition"] = value["schema_definition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSchemaByDefinitionInput:
    out: GetSchemaByDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("SchemaId") is not None:
        import capo_glue.types.schema_id

        out["schema_id"] = capo_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    else:
        raise DeserializationError("GetSchemaByDefinitionInput.schema_id required")
    if data.get("SchemaDefinition") is not None:
        out["schema_definition"] = data["SchemaDefinition"]
    else:
        out["schema_definition"] = ""
    return out
