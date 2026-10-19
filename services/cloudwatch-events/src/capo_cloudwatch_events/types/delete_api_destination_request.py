"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DeleteApiDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.api_destination_name


class DeleteApiDestinationRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.api_destination_name.ApiDestinationName"
    """<p>The name of the destination to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApiDestinationRequest:
    out: DeleteApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
