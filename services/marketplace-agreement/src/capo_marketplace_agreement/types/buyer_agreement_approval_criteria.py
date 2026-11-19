"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalCriteria``."""

from typing_extensions import TypedDict


class BuyerAgreementApprovalCriteria(TypedDict, closed=True):
    required_approval_count: "int"
    """<p>The number of approvers in the group who must approve before the level is approved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalCriteria) -> dict:
    out: dict = {}
    out["requiredApprovalCount"] = value["required_approval_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalCriteria:
    out: BuyerAgreementApprovalCriteria = {}  # type: ignore[typeddict-item]
    if data.get("requiredApprovalCount") is not None:
        out["required_approval_count"] = data["requiredApprovalCount"]
    else:
        out["required_approval_count"] = 0
    return out
