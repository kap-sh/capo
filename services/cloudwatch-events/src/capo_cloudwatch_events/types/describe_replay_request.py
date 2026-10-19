"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeReplayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.replay_name


class DescribeReplayRequest(TypedDict, closed=True):
    replay_name: "capo_cloudwatch_events.types.replay_name.ReplayName"
    """<p>The name of the replay to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplayRequest) -> dict:
    out: dict = {}
    out["ReplayName"] = value["replay_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplayRequest:
    out: DescribeReplayRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReplayName") is not None:
        out["replay_name"] = data["ReplayName"]
    else:
        out["replay_name"] = ""
    return out
