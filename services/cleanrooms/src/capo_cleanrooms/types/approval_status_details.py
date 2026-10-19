"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ApprovalStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.approval_status


class ApprovalStatusDetails(TypedDict, closed=True):
    status: "capo_cleanrooms.types.approval_status.ApprovalStatus"
    """<p>The approval status of a member's vote on the change request. Valid values are PENDING (if they haven't voted), APPROVED, or DENIED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalStatusDetails) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.approval_status

    out["status"] = capo_cleanrooms.types.approval_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ApprovalStatusDetails:
    out: ApprovalStatusDetails = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_cleanrooms.types.approval_status

        out["status"] = capo_cleanrooms.types.approval_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanrooms.types.approval_status.ApprovalStatus", ""
        )
    return out
