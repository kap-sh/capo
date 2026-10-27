"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeregisterSourceEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_arn


class DeregisterSourceEndpointRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the source endpoint to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterSourceEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterSourceEndpointRequest:
    out: DeregisterSourceEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
