"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ApprovalMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Determines whether a subscription requires explicit approval before billing starts.</p>"""
ApprovalMode: TypeAlias = Literal[
    "MANUAL",
    "IMMEDIATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalMode) -> str:
    return value


def deserialize_json(data: str) -> ApprovalMode:
    return cast(ApprovalMode, data)
