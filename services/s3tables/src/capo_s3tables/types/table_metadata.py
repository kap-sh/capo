"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3tables.errors import DeserializationError, SerializationError
from capo_s3tables.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_metadata


class TableMetadataIcebergMember(TypedDict, closed=True):
    iceberg: "capo_s3tables.types.iceberg_metadata.IcebergMetadata"


TableMetadata: TypeAlias = TableMetadataIcebergMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TableMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TableMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "iceberg" in value:
        import capo_s3tables.types.iceberg_metadata

        return {
            "iceberg": capo_s3tables.types.iceberg_metadata.serialize_json(
                value["iceberg"]
            )
        }
    else:
        raise SerializationError("TableMetadata: no variant present")


def deserialize_json(data: dict) -> TableMetadata:
    if data.get("iceberg") is not None:
        import capo_s3tables.types.iceberg_metadata

        return {
            "iceberg": capo_s3tables.types.iceberg_metadata.deserialize_json(
                data["iceberg"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TableMetadata: no recognized variant key")
