"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name


class AssetBundleImportJobDashboardOverrideParameters(TypedDict, closed=True):
    dashboard_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dashboard that you want to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverrideParameters) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDashboardOverrideParameters:
    out: AssetBundleImportJobDashboardOverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    else:
        out["dashboard_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
