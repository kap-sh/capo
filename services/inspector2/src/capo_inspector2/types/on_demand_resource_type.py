"""Generated from Smithy shape ``com.amazonaws.inspector2#OnDemandResourceType``."""

from typing import Literal, TypeAlias, cast

OnDemandResourceType: TypeAlias = Literal["AMI",]


# --- restJson1 ser/de ---
def serialize_json(value: OnDemandResourceType) -> str:
    return value


def deserialize_json(data: str) -> OnDemandResourceType:
    return cast(OnDemandResourceType, data)
