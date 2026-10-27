"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetDestinationEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_arn


class GetDestinationEndpointRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the destination endpoint to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDestinationEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDestinationEndpointRequest:
    out: GetDestinationEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
