"""Generated from Smithy shape ``com.amazonaws.eventbridge#CancelReplayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.replay_name


class CancelReplayRequest(TypedDict, closed=True):
    replay_name: "capo_eventbridge.types.replay_name.ReplayName"
    """<p>The name of the replay to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelReplayRequest) -> dict:
    out: dict = {}
    out["ReplayName"] = value["replay_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelReplayRequest:
    out: CancelReplayRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReplayName") is not None:
        out["replay_name"] = data["ReplayName"]
    else:
        out["replay_name"] = ""
    return out
