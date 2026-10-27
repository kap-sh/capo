"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListSourceEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.source_endpoint_filter_list


class ListSourceEndpointsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single request. The valid range is 1 to 100. If you don't specify a value, the service returns up to 100 results.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the next page of results to return. Use the token that a previous request returned.</p>"""
    filters: NotRequired[
        "capo_mediaconnect.types.source_endpoint_filter_list.SourceEndpointFilterList"
    ]
    """<p>The filters to apply to the list of source endpoints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceEndpointsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_mediaconnect.types.source_endpoint_filter_list

        out["filters"] = (
            capo_mediaconnect.types.source_endpoint_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSourceEndpointsRequest:
    out: ListSourceEndpointsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_mediaconnect.types.source_endpoint_filter_list

        out["filters"] = (
            capo_mediaconnect.types.source_endpoint_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out
