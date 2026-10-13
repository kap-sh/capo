"""Generated from Smithy shape ``com.amazonaws.location#ListDevicePositionsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.resource_name
    import capo_location.types.token
    import capo_location.types.tracking_filter_geometry


class ListDevicePositionsRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The tracker resource containing the requested devices.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of entries returned in a single call.</p> <p>Default value: <code>100</code> </p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>"""
    filter_geometry: NotRequired[
        "capo_location.types.tracking_filter_geometry.TrackingFilterGeometry"
    ]
    """<p>The geometry used to filter device positions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicePositionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filter_geometry" in value:
        import capo_location.types.tracking_filter_geometry

        out["FilterGeometry"] = (
            capo_location.types.tracking_filter_geometry.serialize_json(
                value["filter_geometry"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDevicePositionsRequest:
    out: ListDevicePositionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("FilterGeometry") is not None:
        import capo_location.types.tracking_filter_geometry

        out["filter_geometry"] = (
            capo_location.types.tracking_filter_geometry.deserialize_json(
                data["FilterGeometry"]
            )
        )
    return out


def redact_sensitive(value: ListDevicePositionsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter_geometry" in value:
        import capo_location.types.tracking_filter_geometry

        out["filter_geometry"] = (
            capo_location.types.tracking_filter_geometry.redact_sensitive(
                value["filter_geometry"]
            )
        )
    return out
