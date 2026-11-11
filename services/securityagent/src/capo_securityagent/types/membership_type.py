"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of membership.</p>"""
MembershipType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipType) -> str:
    return value


def deserialize_json(data: str) -> MembershipType:
    return cast(MembershipType, data)
