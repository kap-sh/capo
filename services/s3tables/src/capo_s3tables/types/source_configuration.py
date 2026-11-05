"""Generated from Smithy shape ``com.amazonaws.s3tables#SourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError, SerializationError
from capo_s3tables.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3tables.types.glue_table_source


class SourceConfigurationGlueTableMember(TypedDict, closed=True):
    glueTable: "capo_s3tables.types.glue_table_source.GlueTableSource"


SourceConfiguration: TypeAlias = SourceConfigurationGlueTableMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "glueTable" in value:
        import capo_s3tables.types.glue_table_source

        return {
            "glueTable": capo_s3tables.types.glue_table_source.serialize_json(
                value["glueTable"]
            )
        }
    else:
        raise SerializationError("SourceConfiguration: no variant present")


def deserialize_json(data: dict) -> SourceConfiguration:
    if data.get("glueTable") is not None:
        import capo_s3tables.types.glue_table_source

        return {
            "glueTable": capo_s3tables.types.glue_table_source.deserialize_json(
                data["glueTable"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SourceConfiguration: no recognized variant key")
