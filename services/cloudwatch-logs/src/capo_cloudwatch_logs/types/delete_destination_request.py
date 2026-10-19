"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destination_name


class DeleteDestinationRequest(TypedDict, closed=True):
    destination_name: "capo_cloudwatch_logs.types.destination_name.DestinationName"
    """<p>The name of the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDestinationRequest) -> dict:
    out: dict = {}
    out["destinationName"] = value["destination_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDestinationRequest:
    out: DeleteDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("destinationName") is not None:
        out["destination_name"] = data["destinationName"]
    else:
        out["destination_name"] = ""
    return out
