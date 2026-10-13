"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateMaintenanceWindowTargetResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_description
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_name
    import capo_ssm.types.maintenance_window_target_id
    import capo_ssm.types.owner_information
    import capo_ssm.types.targets


class UpdateMaintenanceWindowTargetResult(TypedDict, closed=True):
    window_id: NotRequired["capo_ssm.types.maintenance_window_id.MaintenanceWindowId"]
    """<p>The maintenance window ID specified in the update request.</p>"""
    window_target_id: NotRequired[
        "capo_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    ]
    """<p>The target ID specified in the update request.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The updated targets.</p>"""
    owner_information: NotRequired["capo_ssm.types.owner_information.OwnerInformation"]
    """<p>The updated owner.</p>"""
    name: NotRequired["capo_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The updated name.</p>"""
    description: NotRequired[
        "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>The updated description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaintenanceWindowTargetResult) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "window_target_id" in value:
        out["WindowTargetId"] = value["window_target_id"]
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "owner_information" in value:
        out["OwnerInformation"] = value["owner_information"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaintenanceWindowTargetResult:
    out: UpdateMaintenanceWindowTargetResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    if data.get("WindowTargetId") is not None:
        out["window_target_id"] = data["WindowTargetId"]
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("OwnerInformation") is not None:
        out["owner_information"] = data["OwnerInformation"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: UpdateMaintenanceWindowTargetResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "owner_information" in value:
        out["owner_information"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
