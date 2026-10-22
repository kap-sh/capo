"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectDesignation``."""

from typing import Literal, TypeAlias, cast

ProjectDesignation: TypeAlias = Literal[
    "OWNER",
    "CONTRIBUTOR",
    "PROJECT_CATALOG_STEWARD",
    "USER_CREATED_DESIGNATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectDesignation) -> str:
    return value


def deserialize_json(data: str) -> ProjectDesignation:
    return cast(ProjectDesignation, data)
