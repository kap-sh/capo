"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeregisterDestinationEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_arn


class DeregisterDestinationEndpointResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the destination endpoint that was deregistered.</p>"""
    name: "str"
    """<p>The name of the destination endpoint that was deregistered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterDestinationEndpointResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeregisterDestinationEndpointResponse:
    out: DeregisterDestinationEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
