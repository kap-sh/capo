"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateMaintenanceWindowTargetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.boolean
    import capo_ssm.types.maintenance_window_description
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_name
    import capo_ssm.types.maintenance_window_target_id
    import capo_ssm.types.owner_information
    import capo_ssm.types.targets


class UpdateMaintenanceWindowTargetRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The maintenance window ID with which to modify the target.</p>"""
    window_target_id: (
        "capo_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId"
    )
    """<p>The target ID to modify.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>The targets to add or replace.</p>"""
    owner_information: NotRequired["capo_ssm.types.owner_information.OwnerInformation"]
    """<p>User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.</p>"""
    name: NotRequired["capo_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>A name for the update.</p>"""
    description: NotRequired[
        "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>An optional description for the update.</p>"""
    replace: NotRequired["capo_ssm.types.boolean.Boolean"]
    """<p>If <code>True</code>, then all fields that are required by the <a>RegisterTargetWithMaintenanceWindow</a> operation are also required for this API request. Optional fields that aren't specified are set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaintenanceWindowTargetRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
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
    if "replace" in value:
        out["Replace"] = value["replace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaintenanceWindowTargetRequest:
    out: UpdateMaintenanceWindowTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError(
            "UpdateMaintenanceWindowTargetRequest.window_id required"
        )
    if data.get("WindowTargetId") is not None:
        out["window_target_id"] = data["WindowTargetId"]
    else:
        raise DeserializationError(
            "UpdateMaintenanceWindowTargetRequest.window_target_id required"
        )
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
    if data.get("Replace") is not None:
        out["replace"] = data["Replace"]
    return out


def redact_sensitive(value: UpdateMaintenanceWindowTargetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "owner_information" in value:
        out["owner_information"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
