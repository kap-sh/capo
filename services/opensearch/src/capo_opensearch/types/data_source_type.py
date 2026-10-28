"""Generated from Smithy shape ``com.amazonaws.opensearch#DataSourceType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError, SerializationError
from capo_opensearch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearch.types.s3_glue_data_catalog


class DataSourceTypeS3GlueDataCatalogMember(TypedDict, closed=True):
    S3GlueDataCatalog: "capo_opensearch.types.s3_glue_data_catalog.S3GlueDataCatalog"


DataSourceType: TypeAlias = DataSourceTypeS3GlueDataCatalogMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DataSourceType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "S3GlueDataCatalog" in value:
        import capo_opensearch.types.s3_glue_data_catalog

        return {
            "S3GlueDataCatalog": capo_opensearch.types.s3_glue_data_catalog.serialize_json(
                value["S3GlueDataCatalog"]
            )
        }
    else:
        raise SerializationError("DataSourceType: no variant present")


def deserialize_json(data: dict) -> DataSourceType:
    if data.get("S3GlueDataCatalog") is not None:
        import capo_opensearch.types.s3_glue_data_catalog

        return {
            "S3GlueDataCatalog": capo_opensearch.types.s3_glue_data_catalog.deserialize_json(
                data["S3GlueDataCatalog"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DataSourceType: no recognized variant key")
