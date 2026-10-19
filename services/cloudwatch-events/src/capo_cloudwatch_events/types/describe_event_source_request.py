"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeEventSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_source_name


class DescribeEventSourceRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.event_source_name.EventSourceName"
    """<p>The name of the partner event source to display the details of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventSourceRequest:
    out: DescribeEventSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
