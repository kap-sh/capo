"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetDestinationEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_arn_list


class BatchGetDestinationEndpointRequest(TypedDict, closed=True):
    arns: "capo_mediaconnect.types.destination_endpoint_arn_list.DestinationEndpointArnList"
    """<p>The Amazon Resource Names (ARNs) of one or more destination endpoints to retrieve. You can specify from 1 to 20 ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDestinationEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetDestinationEndpointRequest:
    out: BatchGetDestinationEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
