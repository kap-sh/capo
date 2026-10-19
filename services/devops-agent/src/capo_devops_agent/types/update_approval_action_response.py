"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateApprovalActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.approval_id
    import capo_devops_agent.types.approval_status


class UpdateApprovalActionResponse(TypedDict, closed=True):
    approval_id: "capo_devops_agent.types.approval_id.ApprovalId"
    """<p>Identifier of the approval request that was resolved. Echoed back so the client can correlate the response with the request.</p>"""
    status: "capo_devops_agent.types.approval_status.ApprovalStatus"
    """<p>Lifecycle status of the approval request immediately after submission. Expected post-submission states are APPROVED (when the action is APPROVED) or REJECTED (when the action is REJECTED); PENDING is not returned from this operation, and REVOKED and REDEEMED are reachable only via subsequent reads.</p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p>Absolute timestamp at which the approval expires. Set when status is APPROVED (computed as the submission time plus ttlSeconds); absent when status is REJECTED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApprovalActionResponse) -> dict:
    out: dict = {}
    out["approvalId"] = value["approval_id"]
    import capo_devops_agent.types.approval_status

    out["status"] = capo_devops_agent.types.approval_status.serialize_json(
        value["status"]
    )
    if "expires_at" in value:
        import capo_devops_agent.types._prelude.timestamp

        out["expiresAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateApprovalActionResponse:
    out: UpdateApprovalActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("approvalId") is not None:
        out["approval_id"] = data["approvalId"]
    else:
        out["approval_id"] = ""
    if data.get("status") is not None:
        import capo_devops_agent.types.approval_status

        out["status"] = capo_devops_agent.types.approval_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_devops_agent.types.approval_status.ApprovalStatus", ""
        )
    if data.get("expiresAt") is not None:
        import capo_devops_agent.types._prelude.timestamp

        out["expires_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["expiresAt"]
        )
    return out
