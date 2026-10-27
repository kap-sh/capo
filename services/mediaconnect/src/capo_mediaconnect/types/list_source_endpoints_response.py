"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListSourceEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_source_endpoint_list


class ListSourceEndpointsResponse(TypedDict, closed=True):
    source_endpoints: (
        "capo_mediaconnect.types.listed_source_endpoint_list.ListedSourceEndpointList"
    )
    """<p>The source endpoints that match the request.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use in the next request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceEndpointsResponse) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.listed_source_endpoint_list

    out["sourceEndpoints"] = (
        capo_mediaconnect.types.listed_source_endpoint_list.serialize_json(
            value["source_endpoints"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSourceEndpointsResponse:
    out: ListSourceEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceEndpoints") is not None:
        import capo_mediaconnect.types.listed_source_endpoint_list

        out["source_endpoints"] = (
            capo_mediaconnect.types.listed_source_endpoint_list.deserialize_json(
                data["sourceEndpoints"]
            )
        )
    else:
        out["source_endpoints"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
