"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetSourceEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_arn


class GetSourceEndpointRequest(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the source endpoint to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSourceEndpointRequest:
    out: GetSourceEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
