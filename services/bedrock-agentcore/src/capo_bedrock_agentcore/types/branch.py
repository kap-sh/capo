"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Branch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.branch_name
    import capo_bedrock_agentcore.types.event_id


class Branch(TypedDict, closed=True):
    root_event_id: NotRequired["capo_bedrock_agentcore.types.event_id.EventId"]
    """<p>The identifier of the root event for this branch.</p>"""
    name: "capo_bedrock_agentcore.types.branch_name.BranchName"
    """<p>The name of the branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Branch) -> dict:
    out: dict = {}
    if "root_event_id" in value:
        out["rootEventId"] = value["root_event_id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Branch:
    out: Branch = {}  # type: ignore[typeddict-item]
    if data.get("rootEventId") is not None:
        out["root_event_id"] = data["rootEventId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
