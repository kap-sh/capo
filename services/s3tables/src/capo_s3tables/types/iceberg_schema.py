"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.schema_field_list


class IcebergSchema(TypedDict, closed=True):
    fields: "capo_s3tables.types.schema_field_list.SchemaFieldList"
    """<p>The schema fields for the table</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSchema) -> dict:
    out: dict = {}
    import capo_s3tables.types.schema_field_list

    out["fields"] = capo_s3tables.types.schema_field_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> IcebergSchema:
    out: IcebergSchema = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_s3tables.types.schema_field_list

        out["fields"] = capo_s3tables.types.schema_field_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    return out
