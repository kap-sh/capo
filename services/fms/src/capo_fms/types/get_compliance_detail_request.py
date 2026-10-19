"""Generated from Smithy shape ``com.amazonaws.fms#GetComplianceDetailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.policy_id


class GetComplianceDetailRequest(TypedDict, closed=True):
    policy_id: "capo_fms.types.policy_id.PolicyId"
    """<p>The ID of the policy that you want to get the details for. <code>PolicyId</code> is returned by <code>PutPolicy</code> and by <code>ListPolicies</code>.</p>"""
    member_account: "capo_fms.types.aws_account_id.AWSAccountId"
    """<p>The Amazon Web Services account that owns the resources that you want to get the details for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComplianceDetailRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    out["MemberAccount"] = value["member_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComplianceDetailRequest:
    out: GetComplianceDetailRequest = {}  # type: ignore[typeddict-item]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    else:
        out["policy_id"] = ""
    if data.get("MemberAccount") is not None:
        out["member_account"] = data["MemberAccount"]
    else:
        out["member_account"] = ""
    return out
