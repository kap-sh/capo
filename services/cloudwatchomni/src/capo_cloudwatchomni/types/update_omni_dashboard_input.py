"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateOmniDashboardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.dashboard_id
    import capo_cloudwatchomni.types.space_id


class UpdateOmniDashboardInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    dashboard_id: "capo_cloudwatchomni.types.dashboard_id.DashboardId"
    """The unique ID of the dashboard."""
    body: NotRequired["str"]
    """The new dashboard definition, as a JSON document. Maximum 1 MiB. Omit to leave unchanged."""
    name: NotRequired["str"]
    """A new name for the dashboard. Omit to leave unchanged."""
    description: NotRequired["str"]
    """A new description of the dashboard. Omit to leave unchanged."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateOmniDashboardInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["dashboardId"] = value["dashboard_id"]
    if "body" in value:
        out["body"] = value["body"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> UpdateOmniDashboardInput:
    out: UpdateOmniDashboardInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("dashboardId") is not None:
        out["dashboard_id"] = data["dashboardId"]
    else:
        out["dashboard_id"] = ""
    if data.get("body") is not None:
        out["body"] = data["body"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
