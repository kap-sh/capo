"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#OrgMembershipStatus``."""

from typing import Literal, TypeAlias, cast

OrgMembershipStatus: TypeAlias = Literal[
    "IN_ORG",
    "NOT_IN_ORG",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrgMembershipStatus) -> str:
    return value


def deserialize_json(data: str) -> OrgMembershipStatus:
    return cast(OrgMembershipStatus, data)
