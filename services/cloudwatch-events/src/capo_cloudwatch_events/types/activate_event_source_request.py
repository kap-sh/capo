"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ActivateEventSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_source_name


class ActivateEventSourceRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.event_source_name.EventSourceName"
    """<p>The name of the partner event source to activate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivateEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActivateEventSourceRequest:
    out: ActivateEventSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
