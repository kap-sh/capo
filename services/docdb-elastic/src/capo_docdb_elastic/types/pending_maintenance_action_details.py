"""Generated from Smithy shape ``com.amazonaws.docdbelastic#PendingMaintenanceActionDetails``."""

from typing_extensions import NotRequired, TypedDict


class PendingMaintenanceActionDetails(TypedDict, closed=True):
    action: "str"
    """<p>Displays the specific action of a pending maintenance action.</p>"""
    auto_applied_after_date: NotRequired["str"]
    """<p>Displays the date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any <code>NEXT_MAINTENANCE</code> <code>optInType</code> requests are ignored.</p>"""
    forced_apply_date: NotRequired["str"]
    """<p>Displays the date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any <code>IMMEDIATE</code> <code>optInType</code> requests are ignored.</p>"""
    opt_in_status: NotRequired["str"]
    """<p>Displays the type of <code>optInType</code> request that has been received for the resource.</p>"""
    current_apply_date: NotRequired["str"]
    """<p>Displays the effective date when the pending maintenance action is applied to the resource.</p>"""
    description: NotRequired["str"]
    """<p>Displays a description providing more detail about the maintenance action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PendingMaintenanceActionDetails) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    if "auto_applied_after_date" in value:
        out["autoAppliedAfterDate"] = value["auto_applied_after_date"]
    if "forced_apply_date" in value:
        out["forcedApplyDate"] = value["forced_apply_date"]
    if "opt_in_status" in value:
        out["optInStatus"] = value["opt_in_status"]
    if "current_apply_date" in value:
        out["currentApplyDate"] = value["current_apply_date"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PendingMaintenanceActionDetails:
    out: PendingMaintenanceActionDetails = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("autoAppliedAfterDate") is not None:
        out["auto_applied_after_date"] = data["autoAppliedAfterDate"]
    if data.get("forcedApplyDate") is not None:
        out["forced_apply_date"] = data["forcedApplyDate"]
    if data.get("optInStatus") is not None:
        out["opt_in_status"] = data["optInStatus"]
    if data.get("currentApplyDate") is not None:
        out["current_apply_date"] = data["currentApplyDate"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
