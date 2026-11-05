"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ReviewSourceId``."""

from typing import Literal, TypeAlias, cast

ReviewSourceId: TypeAlias = Literal[
    "AWS_MARKETPLACE",
    "G2",
    "PEERSPOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewSourceId) -> str:
    return value


def deserialize_json(data: str) -> ReviewSourceId:
    return cast(ReviewSourceId, data)
