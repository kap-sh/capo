"""Generated from Smithy shape ``com.amazonaws.detective#StartMonitoringMemberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_id
    import capo_detective.types.graph_arn


class StartMonitoringMemberRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph.</p>"""
    account_id: "capo_detective.types.account_id.AccountId"
    """<p>The account ID of the member account to try to enable.</p> <p>The account must be an invited member account with a status of <code>ACCEPTED_BUT_DISABLED</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMonitoringMemberRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> StartMonitoringMemberRequest:
    out: StartMonitoringMemberRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    return out
