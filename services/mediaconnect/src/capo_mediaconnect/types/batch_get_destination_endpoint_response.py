"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetDestinationEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_destination_endpoint_error_list
    import capo_mediaconnect.types.destination_endpoint_list


class BatchGetDestinationEndpointResponse(TypedDict, closed=True):
    destination_endpoints: (
        "capo_mediaconnect.types.destination_endpoint_list.DestinationEndpointList"
    )
    """<p>The destination endpoints that MediaConnect successfully retrieved.</p>"""
    errors: "capo_mediaconnect.types.batch_get_destination_endpoint_error_list.BatchGetDestinationEndpointErrorList"
    """<p>The errors for any destination endpoints that MediaConnect couldn't retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetDestinationEndpointResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.destination_endpoint_list

    out["destinationEndpoints"] = (
        capo_mediaconnect.types.destination_endpoint_list.serialize_json(
            value["destination_endpoints"]
        )
    )
    import capo_mediaconnect.types.batch_get_destination_endpoint_error_list

    out["errors"] = (
        capo_mediaconnect.types.batch_get_destination_endpoint_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetDestinationEndpointResponse:
    out: BatchGetDestinationEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("destinationEndpoints") is not None:
        import capo_mediaconnect.types.destination_endpoint_list

        out["destination_endpoints"] = (
            capo_mediaconnect.types.destination_endpoint_list.deserialize_json(
                data["destinationEndpoints"]
            )
        )
    else:
        out["destination_endpoints"] = []
    if data.get("errors") is not None:
        import capo_mediaconnect.types.batch_get_destination_endpoint_error_list

        out["errors"] = (
            capo_mediaconnect.types.batch_get_destination_endpoint_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
