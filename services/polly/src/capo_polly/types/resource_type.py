"""Generated from Smithy shape ``com.amazonaws.polly#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal["lexicon",]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
