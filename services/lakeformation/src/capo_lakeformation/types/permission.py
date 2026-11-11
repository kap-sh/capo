"""Generated from Smithy shape ``com.amazonaws.lakeformation#Permission``."""

from typing import Literal, TypeAlias, cast

Permission: TypeAlias = Literal[
    "ALL",
    "SELECT",
    "ALTER",
    "DROP",
    "DELETE",
    "INSERT",
    "DESCRIBE",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "CREATE_LF_TAG",
    "ASSOCIATE",
    "GRANT_WITH_LF_TAG_EXPRESSION",
    "CREATE_LF_TAG_EXPRESSION",
    "CREATE_CATALOG",
    "SUPER_USER",
    "EXECUTE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> str:
    return value


def deserialize_json(data: str) -> Permission:
    return cast(Permission, data)
