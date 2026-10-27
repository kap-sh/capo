"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GetDestinationEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint


class GetDestinationEndpointResponse(TypedDict, closed=True):
    destination_endpoint: (
        "capo_mediaconnect.types.destination_endpoint.DestinationEndpoint"
    )
    """<p>The details of the destination endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDestinationEndpointResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.destination_endpoint

    out["destinationEndpoint"] = (
        capo_mediaconnect.types.destination_endpoint.serialize_json(
            value["destination_endpoint"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDestinationEndpointResponse:
    out: GetDestinationEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("destinationEndpoint") is not None:
        import capo_mediaconnect.types.destination_endpoint

        out["destination_endpoint"] = (
            capo_mediaconnect.types.destination_endpoint.deserialize_json(
                data["destinationEndpoint"]
            )
        )
    else:
        raise DeserializationError(
            "GetDestinationEndpointResponse.destination_endpoint required"
        )
    return out
