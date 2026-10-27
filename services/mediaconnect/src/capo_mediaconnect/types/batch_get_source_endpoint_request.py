"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetSourceEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_arn_list


class BatchGetSourceEndpointRequest(TypedDict, closed=True):
    arns: "capo_mediaconnect.types.source_endpoint_arn_list.SourceEndpointArnList"
    """<p>The Amazon Resource Names (ARNs) of one or more source endpoints to retrieve. You can specify from 1 to 20 ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSourceEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetSourceEndpointRequest:
    out: BatchGetSourceEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
