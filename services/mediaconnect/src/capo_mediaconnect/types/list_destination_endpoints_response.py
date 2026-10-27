"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListDestinationEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_destination_endpoint_list


class ListDestinationEndpointsResponse(TypedDict, closed=True):
    destination_endpoints: "capo_mediaconnect.types.listed_destination_endpoint_list.ListedDestinationEndpointList"
    """<p>The destination endpoints that match the request.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use in the next request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDestinationEndpointsResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.listed_destination_endpoint_list

    out["destinationEndpoints"] = (
        capo_mediaconnect.types.listed_destination_endpoint_list.serialize_json(
            value["destination_endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDestinationEndpointsResponse:
    out: ListDestinationEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("destinationEndpoints") is not None:
        import capo_mediaconnect.types.listed_destination_endpoint_list

        out["destination_endpoints"] = (
            capo_mediaconnect.types.listed_destination_endpoint_list.deserialize_json(
                data["destinationEndpoints"]
            )
        )
    else:
        out["destination_endpoints"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
