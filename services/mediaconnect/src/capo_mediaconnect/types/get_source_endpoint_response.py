"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetSourceEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint


class GetSourceEndpointResponse(TypedDict, closed=True):
    source_endpoint: "capo_mediaconnect.types.source_endpoint.SourceEndpoint"
    """<p>The details of the source endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceEndpointResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.source_endpoint

    out["sourceEndpoint"] = capo_mediaconnect.types.source_endpoint.serialize_json(
        value["source_endpoint"]
    )
    return out


def deserialize_json(data: dict) -> GetSourceEndpointResponse:
    out: GetSourceEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceEndpoint") is not None:
        import capo_mediaconnect.types.source_endpoint

        out["source_endpoint"] = (
            capo_mediaconnect.types.source_endpoint.deserialize_json(
                data["sourceEndpoint"]
            )
        )
    else:
        raise DeserializationError("GetSourceEndpointResponse.source_endpoint required")
    return out
