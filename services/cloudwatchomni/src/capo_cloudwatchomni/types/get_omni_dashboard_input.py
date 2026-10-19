"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetOmniDashboardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.dashboard_id
    import capo_cloudwatchomni.types.space_id


class GetOmniDashboardInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    dashboard_id: "capo_cloudwatchomni.types.dashboard_id.DashboardId"
    """The unique ID of the dashboard."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetOmniDashboardInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["dashboardId"] = value["dashboard_id"]
    return out


def deserialize_cbor(data: dict) -> GetOmniDashboardInput:
    out: GetOmniDashboardInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("dashboardId") is not None:
        out["dashboard_id"] = data["dashboardId"]
    else:
        out["dashboard_id"] = ""
    return out
