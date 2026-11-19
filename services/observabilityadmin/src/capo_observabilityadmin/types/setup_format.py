"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SetupFormat``."""

from typing import Literal, TypeAlias, cast

SetupFormat: TypeAlias = Literal["BICEP",]


# --- restJson1 ser/de ---
def serialize_json(value: SetupFormat) -> str:
    return value


def deserialize_json(data: str) -> SetupFormat:
    return cast(SetupFormat, data)
