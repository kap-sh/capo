"""Generated from Smithy shape ``com.amazonaws.keyspaces#TimeToLive``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.time_to_live_status


class TimeToLive(TypedDict, closed=True):
    status: "capo_keyspaces.types.time_to_live_status.TimeToLiveStatus"
    """<p>Shows how to enable custom Time to Live (TTL) settings for the specified table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeToLive) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeToLive:
    out: TimeToLive = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
