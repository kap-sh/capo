"""Generated from Smithy shape ``com.amazonaws.medialive#InputPreference``."""

from typing import Literal, TypeAlias, cast

r"""Input preference when deciding which input to make active when a previously failed input has recovered. If \"EQUAL_INPUT_PREFERENCE\", then the active input will stay active as long as it is healthy. If \"PRIMARY_INPUT_PREFERRED\", then always switch back to the primary input when it is healthy."""
InputPreference: TypeAlias = Literal[
    "EQUAL_INPUT_PREFERENCE",
    "PRIMARY_INPUT_PREFERRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputPreference) -> str:
    return value


def deserialize_json(data: str) -> InputPreference:
    return cast(InputPreference, data)
