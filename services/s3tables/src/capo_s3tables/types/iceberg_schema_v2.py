"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSchemaV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3tables.types.integer_list
    import capo_s3tables.types.schema_v2_field_list
    import capo_s3tables.types.schema_v2_field_type


class IcebergSchemaV2(TypedDict, closed=True):
    type: "capo_s3tables.types.schema_v2_field_type.SchemaV2FieldType"
    """<p>The type of the top-level schema, which is always a <code>struct</code> type as defined in the <a href="https://iceberg.apache.org/spec/#schemas-and-data-types">Apache Iceberg specification</a>. This value must be <code>struct</code>.</p>"""
    fields: "capo_s3tables.types.schema_v2_field_list.SchemaV2FieldList"
    """<p>The schema fields for the table. Each field defines a column in the table, including its name, type, and whether it is required.</p>"""
    schema_id: NotRequired["int"]
    """<p>An optional unique identifier for the schema. Schema IDs are used by Apache Iceberg to track schema evolution.</p>"""
    identifier_field_ids: NotRequired["capo_s3tables.types.integer_list.IntegerList"]
    """<p>A list of field IDs that are used as the identifier fields for the table. Identifier fields uniquely identify a row in the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSchemaV2) -> dict:
    out: dict = {}
    import capo_s3tables.types.schema_v2_field_type

    out["type"] = capo_s3tables.types.schema_v2_field_type.serialize_json(value["type"])
    import capo_s3tables.types.schema_v2_field_list

    out["fields"] = capo_s3tables.types.schema_v2_field_list.serialize_json(
        value["fields"]
    )
    if "schema_id" in value:
        out["schema-id"] = value["schema_id"]
    if "identifier_field_ids" in value:
        import capo_s3tables.types.integer_list

        out["identifier-field-ids"] = capo_s3tables.types.integer_list.serialize_json(
            value["identifier_field_ids"]
        )
    return out


def deserialize_json(data: dict) -> IcebergSchemaV2:
    out: IcebergSchemaV2 = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_s3tables.types.schema_v2_field_type

        out["type"] = capo_s3tables.types.schema_v2_field_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("IcebergSchemaV2.type required")
    if data.get("fields") is not None:
        import capo_s3tables.types.schema_v2_field_list

        out["fields"] = capo_s3tables.types.schema_v2_field_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("IcebergSchemaV2.fields required")
    if data.get("schema-id") is not None:
        out["schema_id"] = data["schema-id"]
    if data.get("identifier-field-ids") is not None:
        import capo_s3tables.types.integer_list

        out["identifier_field_ids"] = capo_s3tables.types.integer_list.deserialize_json(
            data["identifier-field-ids"]
        )
    return out
