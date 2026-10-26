"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelDataSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.s3_data_source


class _ModelDataSource_s3DataSource(TypedDict, closed=True):
    s3DataSource: "capo_bedrock.types.s3_data_source.S3DataSource"


ModelDataSource: TypeAlias = _ModelDataSource_s3DataSource | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ModelDataSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ModelDataSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3DataSource" in value:
        import capo_bedrock.types.s3_data_source

        return {
            "s3DataSource": capo_bedrock.types.s3_data_source.serialize_json(
                value["s3DataSource"]
            )
        }
    else:
        raise SerializationError("ModelDataSource: no variant present")


def deserialize_json(data: dict) -> ModelDataSource:
    if data.get("s3DataSource") is not None:
        import capo_bedrock.types.s3_data_source

        return {
            "s3DataSource": capo_bedrock.types.s3_data_source.deserialize_json(
                data["s3DataSource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ModelDataSource: no recognized variant key")
