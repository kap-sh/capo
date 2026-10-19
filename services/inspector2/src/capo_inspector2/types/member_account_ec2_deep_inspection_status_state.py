"""Generated from Smithy shape ``com.amazonaws.inspector2#MemberAccountEc2DeepInspectionStatusState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.ec2_deep_inspection_status
    import capo_inspector2.types.non_empty_string


class MemberAccountEc2DeepInspectionStatusState(TypedDict, closed=True):
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The unique identifier for the Amazon Web Services account of the organization member</p>"""
    status: NotRequired[
        "capo_inspector2.types.ec2_deep_inspection_status.Ec2DeepInspectionStatus"
    ]
    """<p>The state of Amazon Inspector deep inspection in the member account.</p>"""
    error_message: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The error message explaining why the account failed to activate Amazon Inspector deep inspection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccountEc2DeepInspectionStatusState) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> MemberAccountEc2DeepInspectionStatusState:
    out: MemberAccountEc2DeepInspectionStatusState = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
