"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipTypeFilter``."""

from typing import Literal, TypeAlias, cast

"""<p>Filter for member type in list operations.</p>"""
MembershipTypeFilter: TypeAlias = Literal[
    "USER",
    "GROUP",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipTypeFilter) -> str:
    return value


def deserialize_json(data: str) -> MembershipTypeFilter:
    return cast(MembershipTypeFilter, data)
