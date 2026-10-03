"""Generated from Smithy shape ``com.amazonaws.rds#ApplyPendingMaintenanceActionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class ApplyPendingMaintenanceActionMessage(TypedDict, closed=True):
    resource_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The RDS Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an RDS Amazon Resource Name (ARN)</a>.</p>"""
    apply_action: NotRequired["capo_rds.types.string.String"]
    """<p>The pending maintenance action to apply to this resource.</p> <p>Valid Values:</p> <ul> <li> <p> <code>ca-certificate-rotation</code> </p> </li> <li> <p> <code>db-upgrade</code> </p> </li> <li> <p> <code>hardware-maintenance</code> </p> </li> <li> <p> <code>os-upgrade</code> </p> </li> <li> <p> <code>system-update</code> </p> </li> </ul> <p>For more information about these actions, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-aurora">Maintenance actions for Amazon Aurora</a> or <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html#maintenance-actions-rds">Maintenance actions for Amazon RDS</a>.</p>"""
    opt_in_type: NotRequired["capo_rds.types.string.String"]
    """<p>A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type <code>immediate</code> can't be undone.</p> <p>Valid Values:</p> <ul> <li> <p> <code>immediate</code> - Apply the maintenance action immediately.</p> </li> <li> <p> <code>next-maintenance</code> - Apply the maintenance action during the next maintenance window for the resource.</p> </li> <li> <p> <code>undo-opt-in</code> - Cancel any existing <code>next-maintenance</code> opt-in requests.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplyPendingMaintenanceActionMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_identifier" in value:
        pairs.append(
            (f"{key_prefix}ResourceIdentifier", str(value["resource_identifier"]))
        )
    if "apply_action" in value:
        pairs.append((f"{key_prefix}ApplyAction", str(value["apply_action"])))
    if "opt_in_type" in value:
        pairs.append((f"{key_prefix}OptInType", str(value["opt_in_type"])))


def deserialize_query(el: Element) -> ApplyPendingMaintenanceActionMessage:
    out: ApplyPendingMaintenanceActionMessage = {}  # type: ignore[typeddict-item]
    child_resource_identifier = el.find("ResourceIdentifier")
    if child_resource_identifier is not None:
        out["resource_identifier"] = str(child_resource_identifier.text or "")
    child_apply_action = el.find("ApplyAction")
    if child_apply_action is not None:
        out["apply_action"] = str(child_apply_action.text or "")
    child_opt_in_type = el.find("OptInType")
    if child_opt_in_type is not None:
        out["opt_in_type"] = str(child_opt_in_type.text or "")
    return out
