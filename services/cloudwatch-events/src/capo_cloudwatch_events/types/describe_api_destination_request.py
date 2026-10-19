"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeApiDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.api_destination_name


class DescribeApiDestinationRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.api_destination_name.ApiDestinationName"
    """<p>The name of the API destination to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApiDestinationRequest:
    out: DescribeApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
