"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DisconnectEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_arn
    import capo_mediaconnect.types.source_endpoint_arn


class DisconnectEndpointsResponse(TypedDict, closed=True):
    destination_endpoint_arn: (
        "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn"
    )
    """<p>The Amazon Resource Name (ARN) of the disconnected destination endpoint.</p>"""
    destination_endpoint_name: "str"
    """<p>The name of the disconnected destination endpoint.</p>"""
    source_endpoint_arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the disconnected source endpoint.</p>"""
    source_endpoint_name: "str"
    """<p>The name of the disconnected source endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectEndpointsResponse) -> dict:
    out: dict = {}
    out["destinationEndpointArn"] = value["destination_endpoint_arn"]
    out["destinationEndpointName"] = value["destination_endpoint_name"]
    out["sourceEndpointArn"] = value["source_endpoint_arn"]
    out["sourceEndpointName"] = value["source_endpoint_name"]
    return out


def deserialize_json(data: dict) -> DisconnectEndpointsResponse:
    out: DisconnectEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("destinationEndpointArn") is not None:
        out["destination_endpoint_arn"] = data["destinationEndpointArn"]
    else:
        out["destination_endpoint_arn"] = ""
    if data.get("destinationEndpointName") is not None:
        out["destination_endpoint_name"] = data["destinationEndpointName"]
    else:
        out["destination_endpoint_name"] = ""
    if data.get("sourceEndpointArn") is not None:
        out["source_endpoint_arn"] = data["sourceEndpointArn"]
    else:
        out["source_endpoint_arn"] = ""
    if data.get("sourceEndpointName") is not None:
        out["source_endpoint_name"] = data["sourceEndpointName"]
    else:
        out["source_endpoint_name"] = ""
    return out
