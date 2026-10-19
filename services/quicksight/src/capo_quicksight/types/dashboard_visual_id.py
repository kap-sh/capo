"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardVisualId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.short_restrictive_resource_id


class DashboardVisualId(TypedDict, closed=True):
    dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the dashboard that has the visual that you want to embed. The <code>DashboardId</code> can be found in the <code>IDs for developers</code> section of the <code>Embed visual</code> pane of the visual's on-visual menu of the Quick console. You can also get the <code>DashboardId</code> with a <code>ListDashboards</code> API operation.</p>"""
    sheet_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the sheet that the has visual that you want to embed. The <code>SheetId</code> can be found in the <code>IDs for developers</code> section of the <code>Embed visual</code> pane of the visual's on-visual menu of the Quick console.</p>"""
    visual_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the visual that you want to embed. The <code>VisualID</code> can be found in the <code>IDs for developers</code> section of the <code>Embed visual</code> pane of the visual's on-visual menu of the Amazon Quick Sight console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardVisualId) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    out["SheetId"] = value["sheet_id"]
    out["VisualId"] = value["visual_id"]
    return out


def deserialize_json(data: dict) -> DashboardVisualId:
    out: DashboardVisualId = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    else:
        out["dashboard_id"] = ""
    if data.get("SheetId") is not None:
        out["sheet_id"] = data["SheetId"]
    else:
        out["sheet_id"] = ""
    if data.get("VisualId") is not None:
        out["visual_id"] = data["VisualId"]
    else:
        out["visual_id"] = ""
    return out
