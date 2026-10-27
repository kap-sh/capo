"""Generated from Smithy shape ``com.amazonaws.connect#UpdateOutboundEmailMessageSourceType``."""

from typing import Literal, TypeAlias, cast

UpdateOutboundEmailMessageSourceType: TypeAlias = Literal["RAW",]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutboundEmailMessageSourceType) -> str:
    return value


def deserialize_json(data: str) -> UpdateOutboundEmailMessageSourceType:
    return cast(UpdateOutboundEmailMessageSourceType, data)
