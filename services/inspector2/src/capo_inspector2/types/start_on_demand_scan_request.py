"""Generated from Smithy shape ``com.amazonaws.inspector2#StartOnDemandScanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.on_demand_resource_type
    import capo_inspector2.types.resource_id


class StartOnDemandScanRequest(TypedDict, closed=True):
    resource_id: "capo_inspector2.types.resource_id.ResourceId"
    """<p>The ID of the resource to scan on demand.</p>"""
    resource_type: "capo_inspector2.types.on_demand_resource_type.OnDemandResourceType"
    """<p>The type of the resource to scan on demand.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOnDemandScanRequest) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    import capo_inspector2.types.on_demand_resource_type

    out["resourceType"] = capo_inspector2.types.on_demand_resource_type.serialize_json(
        value["resource_type"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartOnDemandScanRequest:
    out: StartOnDemandScanRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
