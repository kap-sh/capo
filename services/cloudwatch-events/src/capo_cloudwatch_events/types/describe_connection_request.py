"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_name


class DescribeConnectionRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.connection_name.ConnectionName"
    """<p>The name of the connection to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionRequest:
    out: DescribeConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
