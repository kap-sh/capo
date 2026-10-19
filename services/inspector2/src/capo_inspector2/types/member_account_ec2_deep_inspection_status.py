"""Generated from Smithy shape ``com.amazonaws.inspector2#MemberAccountEc2DeepInspectionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id


class MemberAccountEc2DeepInspectionStatus(TypedDict, closed=True):
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The unique identifier for the Amazon Web Services account of the organization member.</p>"""
    activate_deep_inspection: "bool"
    """<p>Whether Amazon Inspector deep inspection is active in the account. If <code>TRUE</code> Amazon Inspector deep inspection is active, if <code>FALSE</code> it is not active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccountEc2DeepInspectionStatus) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["activateDeepInspection"] = value["activate_deep_inspection"]
    return out


def deserialize_json(data: dict) -> MemberAccountEc2DeepInspectionStatus:
    out: MemberAccountEc2DeepInspectionStatus = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("activateDeepInspection") is not None:
        out["activate_deep_inspection"] = data["activateDeepInspection"]
    else:
        out["activate_deep_inspection"] = False
    return out
