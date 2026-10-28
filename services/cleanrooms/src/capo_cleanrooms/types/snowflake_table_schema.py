"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SnowflakeTableSchema``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.snowflake_table_schema_list


class SnowflakeTableSchemaV1Member(TypedDict, closed=True):
    v1: "capo_cleanrooms.types.snowflake_table_schema_list.SnowflakeTableSchemaList"


SnowflakeTableSchema: TypeAlias = SnowflakeTableSchemaV1Member | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeTableSchema) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SnowflakeTableSchema: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "v1" in value:
        import capo_cleanrooms.types.snowflake_table_schema_list

        return {
            "v1": capo_cleanrooms.types.snowflake_table_schema_list.serialize_json(
                value["v1"]
            )
        }
    else:
        raise SerializationError("SnowflakeTableSchema: no variant present")


def deserialize_json(data: dict) -> SnowflakeTableSchema:
    if data.get("v1") is not None:
        import capo_cleanrooms.types.snowflake_table_schema_list

        return {
            "v1": capo_cleanrooms.types.snowflake_table_schema_list.deserialize_json(
                data["v1"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SnowflakeTableSchema: no recognized variant key")
