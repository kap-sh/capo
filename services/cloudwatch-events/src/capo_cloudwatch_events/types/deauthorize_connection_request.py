"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DeauthorizeConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_name


class DeauthorizeConnectionRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.connection_name.ConnectionName"
    """<p>The name of the connection to remove authorization from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeauthorizeConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeauthorizeConnectionRequest:
    out: DeauthorizeConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
