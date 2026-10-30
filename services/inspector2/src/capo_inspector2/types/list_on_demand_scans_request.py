"""Generated from Smithy shape ``com.amazonaws.inspector2#ListOnDemandScansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.on_demand_resource_type
    import capo_inspector2.types.on_demand_scan_next_token
    import capo_inspector2.types.resource_id


class ListOnDemandScansRequest(TypedDict, closed=True):
    resource_id: "capo_inspector2.types.resource_id.ResourceId"
    """<p>The ID of the resource whose on-demand scans are being listed.</p>"""
    resource_type: "capo_inspector2.types.on_demand_resource_type.OnDemandResourceType"
    """<p>The type of the resource whose on-demand scans are being listed.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single page of the response.</p>"""
    next_token: NotRequired[
        "capo_inspector2.types.on_demand_scan_next_token.OnDemandScanNextToken"
    ]
    """<p>A pagination token from a previous response used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOnDemandScansRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    import capo_inspector2.types.on_demand_resource_type

    out["resourceType"] = capo_inspector2.types.on_demand_resource_type.serialize_json(
        value["resource_type"]
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOnDemandScansRequest:
    out: ListOnDemandScansRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("resourceType") is not None:
        import capo_inspector2.types.on_demand_resource_type

        out["resource_type"] = (
            capo_inspector2.types.on_demand_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_inspector2.types.on_demand_resource_type.OnDemandResourceType", ""
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
