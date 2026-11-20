"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ApprovalType``."""

from typing import Literal, TypeAlias, cast

"""<p>Controls who approves a time off request. Use it on <code>CreateTimeOff</code> only, because <code>ApproveTimeOff</code> already names its own decision. <code>AWAIT_APPROVAL</code> waits for an <code>ApproveTimeOff</code> or <code>RejectTimeOff</code> call. <code>AUTOMATIC</code> has Connect Customer decide the request.</p>"""
ApprovalType: TypeAlias = Literal[
    "AWAIT_APPROVAL",
    "AUTOMATIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalType) -> str:
    return value


def deserialize_json(data: str) -> ApprovalType:
    return cast(ApprovalType, data)
