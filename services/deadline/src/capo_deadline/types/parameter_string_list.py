"""Generated from Smithy shape ``com.amazonaws.deadline#ParameterStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.parameter_string

ParameterStringList: TypeAlias = list[
    "capo_deadline.types.parameter_string.ParameterString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> ParameterStringList:
    return [item for item in data if item is not None]
