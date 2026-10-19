"""Generated from Smithy shape ``com.amazonaws.braket#SearchDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.search_devices_filter_list


class SearchDevicesRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""
    filters: "capo_braket.types.search_devices_filter_list.SearchDevicesFilterList"
    """<p>Array of SearchDevicesFilter objects to use when searching for devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDevicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    import capo_braket.types.search_devices_filter_list

    out["filters"] = capo_braket.types.search_devices_filter_list.serialize_json(
        value["filters"]
    )
    return out


def deserialize_json(data: dict) -> SearchDevicesRequest:
    out: SearchDevicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_braket.types.search_devices_filter_list

        out["filters"] = capo_braket.types.search_devices_filter_list.deserialize_json(
            data["filters"]
        )
    else:
        out["filters"] = []
    return out
