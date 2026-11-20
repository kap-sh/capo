"""Generated from Smithy shape ``com.amazonaws.connectscheduling#TimeOffStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a time off request. <code>PENDING</code> means Connect Customer is processing a change to the request. <code>AWAITING_APPROVAL</code> means the request is waiting for a decision.</p>"""
TimeOffStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "REJECTED",
    "CANCELLED",
    "AWAITING_APPROVAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeOffStatus) -> str:
    return value


def deserialize_json(data: str) -> TimeOffStatus:
    return cast(TimeOffStatus, data)
