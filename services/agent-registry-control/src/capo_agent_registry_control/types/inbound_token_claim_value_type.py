"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#InboundTokenClaimValueType``."""

from typing import Literal, TypeAlias, cast

"""<p>The value type of a claim in an inbound JWT.</p>"""
InboundTokenClaimValueType: TypeAlias = Literal[
    "STRING",
    "STRING_ARRAY",
]


# --- restJson1 ser/de ---
def serialize_json(value: InboundTokenClaimValueType) -> str:
    return value


def deserialize_json(data: str) -> InboundTokenClaimValueType:
    return cast(InboundTokenClaimValueType, data)
