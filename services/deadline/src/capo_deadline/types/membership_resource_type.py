"""Generated from Smithy shape ``com.amazonaws.deadline#MembershipResourceType``."""

from typing import Literal, TypeAlias, cast

MembershipResourceType: TypeAlias = Literal[
    "FARM",
    "QUEUE",
    "FLEET",
    "JOB",
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipResourceType) -> str:
    return value


def deserialize_json(data: str) -> MembershipResourceType:
    return cast(MembershipResourceType, data)
