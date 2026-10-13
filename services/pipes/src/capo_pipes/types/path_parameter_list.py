"""Generated from Smithy shape ``com.amazonaws.pipes#PathParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.path_parameter

PathParameterList: TypeAlias = list["capo_pipes.types.path_parameter.PathParameter"]


# --- restJson1 ser/de ---
def serialize_json(value: PathParameterList) -> list:
    return list(value)


def deserialize_json(data: list) -> PathParameterList:
    return [item for item in data if item is not None]


def redact_sensitive(value: PathParameterList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
