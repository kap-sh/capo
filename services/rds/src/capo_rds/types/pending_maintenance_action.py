"""Generated from Smithy shape ``com.amazonaws.rds#PendingMaintenanceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class PendingMaintenanceAction(TypedDict, closed=True):
    action: NotRequired["capo_rds.types.string.String"]
    """<p>The type of pending maintenance action that is available for the resource. </p> <p>For more information about maintenance actions, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html">Maintaining a DB instance</a>.</p> <p>Valid Values:</p> <ul> <li> <p> <code>ca-certificate-rotation</code> </p> </li> <li> <p> <code>db-upgrade</code> </p> </li> <li> <p> <code>hardware-maintenance</code> </p> </li> <li> <p> <code>os-upgrade</code> </p> </li> <li> <p> <code>serverless-platform-version-update</code> </p> </li> <li> <p> <code>system-update</code> </p> </li> </ul> <p>For more information about these actions, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-aurora">Maintenance actions for Amazon Aurora</a> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-rds">Maintenance actions for Amazon RDS</a>.</p>"""
    auto_applied_after_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date.</p>"""
    forced_apply_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The date when the maintenance action is automatically applied.</p> <p>On this date, the maintenance action is applied to the resource as soon as possible, regardless of the maintenance window for the resource. There might be a delay of one or more days from this date before the maintenance action is applied.</p>"""
    opt_in_status: NotRequired["capo_rds.types.string.String"]
    """<p>Indicates the type of opt-in request that has been received for the resource.</p>"""
    current_apply_date: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The effective date when the pending maintenance action is applied to the resource. This date takes into account opt-in requests received from the <code>ApplyPendingMaintenanceAction</code> API, the <code>AutoAppliedAfterDate</code>, and the <code>ForcedApplyDate</code>. This value is blank if an opt-in request has not been received and nothing has been specified as <code>AutoAppliedAfterDate</code> or <code>ForcedApplyDate</code>.</p>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>A description providing more detail about the maintenance action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PendingMaintenanceAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "action" in value:
        pairs.append((f"{key_prefix}Action", str(value["action"])))
    if "auto_applied_after_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["auto_applied_after_date"], pairs, f"{key_prefix}AutoAppliedAfterDate"
        )
    if "forced_apply_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["forced_apply_date"], pairs, f"{key_prefix}ForcedApplyDate"
        )
    if "opt_in_status" in value:
        pairs.append((f"{key_prefix}OptInStatus", str(value["opt_in_status"])))
    if "current_apply_date" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["current_apply_date"], pairs, f"{key_prefix}CurrentApplyDate"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> PendingMaintenanceAction:
    out: PendingMaintenanceAction = {}  # type: ignore[typeddict-item]
    child_action = el.find("Action")
    if child_action is not None:
        out["action"] = str(child_action.text or "")
    child_auto_applied_after_date = el.find("AutoAppliedAfterDate")
    if child_auto_applied_after_date is not None:
        import capo_rds.types.t_stamp

        out["auto_applied_after_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_auto_applied_after_date
        )
    child_forced_apply_date = el.find("ForcedApplyDate")
    if child_forced_apply_date is not None:
        import capo_rds.types.t_stamp

        out["forced_apply_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_forced_apply_date
        )
    child_opt_in_status = el.find("OptInStatus")
    if child_opt_in_status is not None:
        out["opt_in_status"] = str(child_opt_in_status.text or "")
    child_current_apply_date = el.find("CurrentApplyDate")
    if child_current_apply_date is not None:
        import capo_rds.types.t_stamp

        out["current_apply_date"] = capo_rds.types.t_stamp.deserialize_query(
            child_current_apply_date
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
