"""Generated from Smithy shape ``com.amazonaws.inspector2#GetOnDemandScanStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.on_demand_resource_type
    import capo_inspector2.types.resource_id
    import capo_inspector2.types.scan_id


class GetOnDemandScanStatusRequest(TypedDict, closed=True):
    resource_id: "capo_inspector2.types.resource_id.ResourceId"
    """<p>The ID of the resource whose on-demand scan status is being requested.</p>"""
    scan_id: "capo_inspector2.types.scan_id.ScanId"
    """<p>The unique identifier of the on-demand scan whose status is being requested.</p>"""
    resource_type: "capo_inspector2.types.on_demand_resource_type.OnDemandResourceType"
    """<p>The type of the resource whose on-demand scan status is being requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOnDemandScanStatusRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    out["scanId"] = value["scan_id"]
    import capo_inspector2.types.on_demand_resource_type

    out["resourceType"] = capo_inspector2.types.on_demand_resource_type.serialize_json(
        value["resource_type"]
    )
    return out


def deserialize_json(data: dict) -> GetOnDemandScanStatusRequest:
    out: GetOnDemandScanStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("scanId") is not None:
        out["scan_id"] = data["scanId"]
    else:
        out["scan_id"] = ""
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
    return out
