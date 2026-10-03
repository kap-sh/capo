"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.iceberg_struct_field_list
    import capo_glue.types.iceberg_struct_type_enum
    import capo_glue.types.integer
    import capo_glue.types.integer_list


class IcebergSchema(TypedDict, closed=True):
    schema_id: "capo_glue.types.integer.Integer"
    """<p>The unique identifier for this schema version within the Iceberg table's schema evolution history.</p>"""
    identifier_field_ids: NotRequired["capo_glue.types.integer_list.IntegerList"]
    """<p>The list of field identifiers that uniquely identify records in the table, used for row-level operations and deduplication.</p>"""
    type: NotRequired["capo_glue.types.iceberg_struct_type_enum.IcebergStructTypeEnum"]
    """<p>The root type of the schema structure, typically "struct" for Iceberg table schemas.</p>"""
    fields: "capo_glue.types.iceberg_struct_field_list.IcebergStructFieldList"
    """<p>The list of field definitions that make up the table schema, including field names, types, and metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSchema) -> dict:
    out: dict = {}
    out["SchemaId"] = value.get("schema_id", 0)
    if "identifier_field_ids" in value:
        import capo_glue.types.integer_list

        out["IdentifierFieldIds"] = capo_glue.types.integer_list.serialize_aws_json_1_1(
            value["identifier_field_ids"]
        )
    if "type" in value:
        import capo_glue.types.iceberg_struct_type_enum

        out["Type"] = capo_glue.types.iceberg_struct_type_enum.serialize_aws_json_1_1(
            value["type"]
        )
    import capo_glue.types.iceberg_struct_field_list

    out["Fields"] = capo_glue.types.iceberg_struct_field_list.serialize_aws_json_1_1(
        value["fields"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergSchema:
    out: IcebergSchema = {}  # type: ignore[typeddict-item]
    if data.get("SchemaId") is not None:
        out["schema_id"] = data["SchemaId"]
    else:
        out["schema_id"] = 0
    if data.get("IdentifierFieldIds") is not None:
        import capo_glue.types.integer_list

        out["identifier_field_ids"] = (
            capo_glue.types.integer_list.deserialize_aws_json_1_1(
                data["IdentifierFieldIds"]
            )
        )
    if data.get("Type") is not None:
        import capo_glue.types.iceberg_struct_type_enum

        out["type"] = capo_glue.types.iceberg_struct_type_enum.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Fields") is not None:
        import capo_glue.types.iceberg_struct_field_list

        out["fields"] = (
            capo_glue.types.iceberg_struct_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("IcebergSchema.fields required")
    return out
