"""Generated from Smithy shape ``com.amazonaws.inspector2#FailedMemberAccountEc2DeepInspectionStatusState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.status


class FailedMemberAccountEc2DeepInspectionStatusState(TypedDict, closed=True):
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The unique identifier for the Amazon Web Services account of the organization member that failed to activate Amazon Inspector deep inspection.</p>"""
    ec2_scan_status: NotRequired["capo_inspector2.types.status.Status"]
    """<p>The status of EC2 scanning in the account that failed to activate Amazon Inspector deep inspection.</p>"""
    error_message: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The error message explaining why the account failed to activate Amazon Inspector deep inspection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedMemberAccountEc2DeepInspectionStatusState) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "ec2_scan_status" in value:
        out["ec2ScanStatus"] = value["ec2_scan_status"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedMemberAccountEc2DeepInspectionStatusState:
    out: FailedMemberAccountEc2DeepInspectionStatusState = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("ec2ScanStatus") is not None:
        out["ec2_scan_status"] = data["ec2ScanStatus"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
