"""Generated from Smithy shape ``com.amazonaws.glue#GetSchemaVersionsDiffInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.schema_diff_type
    import capo_glue.types.schema_id
    import capo_glue.types.schema_version_number


class GetSchemaVersionsDiffInput(TypedDict, closed=True):
    schema_id: "capo_glue.types.schema_id.SchemaId"
    """<p>This is a wrapper structure to contain schema identity fields. The structure contains:</p> <ul> <li> <p>SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> <li> <p>SchemaId$SchemaName: The name of the schema. One of <code>SchemaArn</code> or <code>SchemaName</code> has to be provided.</p> </li> </ul>"""
    first_schema_version_number: (
        "capo_glue.types.schema_version_number.SchemaVersionNumber"
    )
    """<p>The first of the two schema versions to be compared.</p>"""
    second_schema_version_number: (
        "capo_glue.types.schema_version_number.SchemaVersionNumber"
    )
    """<p>The second of the two schema versions to be compared.</p>"""
    schema_diff_type: "capo_glue.types.schema_diff_type.SchemaDiffType"
    """<p>Refers to <code>SYNTAX_DIFF</code>, which is the currently supported diff type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSchemaVersionsDiffInput) -> dict:
    out: dict = {}
    import capo_glue.types.schema_id

    out["SchemaId"] = capo_glue.types.schema_id.serialize_aws_json_1_1(
        value["schema_id"]
    )
    import capo_glue.types.schema_version_number

    out["FirstSchemaVersionNumber"] = (
        capo_glue.types.schema_version_number.serialize_aws_json_1_1(
            value["first_schema_version_number"]
        )
    )
    import capo_glue.types.schema_version_number

    out["SecondSchemaVersionNumber"] = (
        capo_glue.types.schema_version_number.serialize_aws_json_1_1(
            value["second_schema_version_number"]
        )
    )
    import capo_glue.types.schema_diff_type

    out["SchemaDiffType"] = capo_glue.types.schema_diff_type.serialize_aws_json_1_1(
        value["schema_diff_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSchemaVersionsDiffInput:
    out: GetSchemaVersionsDiffInput = {}  # type: ignore[typeddict-item]
    if data.get("SchemaId") is not None:
        import capo_glue.types.schema_id

        out["schema_id"] = capo_glue.types.schema_id.deserialize_aws_json_1_1(
            data["SchemaId"]
        )
    else:
        raise DeserializationError("GetSchemaVersionsDiffInput.schema_id required")
    if data.get("FirstSchemaVersionNumber") is not None:
        import capo_glue.types.schema_version_number

        out["first_schema_version_number"] = (
            capo_glue.types.schema_version_number.deserialize_aws_json_1_1(
                data["FirstSchemaVersionNumber"]
            )
        )
    else:
        raise DeserializationError(
            "GetSchemaVersionsDiffInput.first_schema_version_number required"
        )
    if data.get("SecondSchemaVersionNumber") is not None:
        import capo_glue.types.schema_version_number

        out["second_schema_version_number"] = (
            capo_glue.types.schema_version_number.deserialize_aws_json_1_1(
                data["SecondSchemaVersionNumber"]
            )
        )
    else:
        raise DeserializationError(
            "GetSchemaVersionsDiffInput.second_schema_version_number required"
        )
    if data.get("SchemaDiffType") is not None:
        import capo_glue.types.schema_diff_type

        out["schema_diff_type"] = (
            capo_glue.types.schema_diff_type.deserialize_aws_json_1_1(
                data["SchemaDiffType"]
            )
        )
    else:
        import typing

        out["schema_diff_type"] = typing.cast(
            "capo_glue.types.schema_diff_type.SchemaDiffType", ""
        )
    return out
