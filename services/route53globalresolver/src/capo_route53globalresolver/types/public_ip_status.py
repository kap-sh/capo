"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#PublicIpStatus``."""

from typing import Literal, TypeAlias, cast

PublicIpStatus: TypeAlias = Literal[
    "ENABLED_RESERVED",
    "DISABLED_RESERVED",
    "DISABLED_RELEASED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PublicIpStatus) -> str:
    return value


def deserialize_json(data: str) -> PublicIpStatus:
    return cast(PublicIpStatus, data)
