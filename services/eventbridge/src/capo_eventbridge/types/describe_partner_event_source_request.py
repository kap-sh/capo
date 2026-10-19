"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribePartnerEventSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.event_source_name


class DescribePartnerEventSourceRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.event_source_name.EventSourceName"
    """<p>The name of the event source to display.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePartnerEventSourceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePartnerEventSourceRequest:
    out: DescribePartnerEventSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
