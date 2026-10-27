"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DisconnectEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_arn
    import capo_mediaconnect.types.source_endpoint_arn


class DisconnectEndpointsRequest(TypedDict, closed=True):
    destination_endpoint_arn: (
        "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn"
    )
    """<p>The Amazon Resource Name (ARN) of the destination endpoint to disconnect.</p>"""
    source_endpoint_arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the source endpoint to disconnect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectEndpointsRequest) -> dict:
    out: dict = {}
    out["sourceEndpointArn"] = value["source_endpoint_arn"]
    return out


def deserialize_json(data: dict) -> DisconnectEndpointsRequest:
    out: DisconnectEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceEndpointArn") is not None:
        out["source_endpoint_arn"] = data["sourceEndpointArn"]
    else:
        out["source_endpoint_arn"] = ""
    return out
