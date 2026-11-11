"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLakeResourceType``."""

from typing import Literal, TypeAlias, cast

DataLakeResourceType: TypeAlias = Literal[
    "ANY_RESOURCE",
    "CATALOG",
    "DATABASE",
    "TABLE",
    "DATA_LOCATION",
    "LF_TAG",
    "LF_TAG_POLICY",
    "LF_TAG_POLICY_DATABASE",
    "LF_TAG_POLICY_TABLE",
    "LF_NAMED_TAG_EXPRESSION",
    "USER_DEFINED_FUNCTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeResourceType) -> str:
    return value


def deserialize_json(data: str) -> DataLakeResourceType:
    return cast(DataLakeResourceType, data)
