"""Generated from Smithy shape ``com.amazonaws.detective#DisassociateMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn


class DisassociateMembershipRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph to remove the member account from.</p> <p>The member account's member status in the behavior graph must be <code>ENABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMembershipRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateMembershipRequest:
    out: DisassociateMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    return out
