"""Generated from Smithy shape ``com.amazonaws.amp#DescribeResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amp.types.workspace_policy_status_code


class DescribeResourcePolicyResponse(TypedDict, closed=True):
    policy_document: "str"
    """<p>The JSON policy document for the resource-based policy attached to the workspace.</p>"""
    policy_status: (
        "capo_amp.types.workspace_policy_status_code.WorkspacePolicyStatusCode"
    )
    """<p>The current status of the resource-based policy.</p>"""
    revision_id: "str"
    """<p>The revision ID of the current resource-based policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourcePolicyResponse) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    out["policyStatus"] = value["policy_status"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> DescribeResourcePolicyResponse:
    out: DescribeResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        out["policy_document"] = ""
    if data.get("policyStatus") is not None:
        out["policy_status"] = data["policyStatus"]
    else:
        out["policy_status"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    return out
