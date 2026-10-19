"""Generated from Smithy shape ``com.amazonaws.mpa#MofNApprovalStrategy``."""

from typing_extensions import TypedDict


class MofNApprovalStrategy(TypedDict, closed=True):
    min_approvals_required: "int"
    """<p>Minimum number of approvals (M) required for a total number of approvers (N).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MofNApprovalStrategy) -> dict:
    out: dict = {}
    out["MinApprovalsRequired"] = value["min_approvals_required"]
    return out


def deserialize_json(data: dict) -> MofNApprovalStrategy:
    out: MofNApprovalStrategy = {}  # type: ignore[typeddict-item]
    if data.get("MinApprovalsRequired") is not None:
        out["min_approvals_required"] = data["MinApprovalsRequired"]
    else:
        out["min_approvals_required"] = 0
    return out
