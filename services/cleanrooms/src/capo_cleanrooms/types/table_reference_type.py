"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TableReferenceType``."""

from typing import Literal, TypeAlias, cast

TableReferenceType: TypeAlias = Literal[
    "GLUE",
    "SNOWFLAKE",
    "ATHENA",
    "DATABRICKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TableReferenceType) -> str:
    return value


def deserialize_json(data: str) -> TableReferenceType:
    return cast(TableReferenceType, data)
