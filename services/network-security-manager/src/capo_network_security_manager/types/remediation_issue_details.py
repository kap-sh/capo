"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RemediationIssueDetails``."""

from typing_extensions import NotRequired, TypedDict


class RemediationIssueDetails(TypedDict, closed=True):
    issue_type: NotRequired["str"]
    """<p>The type of remediation issue.</p>"""
    message: NotRequired["str"]
    """<p>A human-readable description of the remediation issue.</p>"""
    corrective_action: NotRequired["str"]
    """<p>A recommended action for resolving the remediation issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationIssueDetails) -> dict:
    out: dict = {}
    if "issue_type" in value:
        out["issueType"] = value["issue_type"]
    if "message" in value:
        out["message"] = value["message"]
    if "corrective_action" in value:
        out["correctiveAction"] = value["corrective_action"]
    return out


def deserialize_json(data: dict) -> RemediationIssueDetails:
    out: RemediationIssueDetails = {}  # type: ignore[typeddict-item]
    if data.get("issueType") is not None:
        out["issue_type"] = data["issueType"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("correctiveAction") is not None:
        out["corrective_action"] = data["correctiveAction"]
    return out
