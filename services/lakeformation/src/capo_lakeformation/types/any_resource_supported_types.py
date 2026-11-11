"""Generated from Smithy shape ``com.amazonaws.lakeformation#AnyResourceSupportedTypes``."""

from typing import Literal, TypeAlias, cast

AnyResourceSupportedTypes: TypeAlias = Literal["TABLE",]


# --- restJson1 ser/de ---
def serialize_json(value: AnyResourceSupportedTypes) -> str:
    return value


def deserialize_json(data: str) -> AnyResourceSupportedTypes:
    return cast(AnyResourceSupportedTypes, data)
