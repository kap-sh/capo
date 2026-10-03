"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterTargetWithMaintenanceWindowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.client_token
    import capo_ssm.types.maintenance_window_description
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_name
    import capo_ssm.types.maintenance_window_resource_type
    import capo_ssm.types.owner_information
    import capo_ssm.types.targets


class RegisterTargetWithMaintenanceWindowRequest(TypedDict, closed=True):
    window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
    """<p>The ID of the maintenance window the target should be registered with.</p>"""
    resource_type: (
        "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
    )
    """<p>The type of target being registered with the maintenance window.</p>"""
    targets: "capo_ssm.types.targets.Targets"
    """<p>The targets to register with the maintenance window. In other words, the managed nodes to run commands on when the maintenance window runs.</p> <note> <p>If a single maintenance window task is registered with multiple targets, its task invocations occur sequentially and not in parallel. If your task must run on multiple targets at the same time, register a task for each target individually and assign each task the same priority level.</p> </note> <p>You can specify targets using managed node IDs, resource group names, or tags that have been applied to managed nodes.</p> <p> <b>Example 1</b>: Specify managed node IDs</p> <p> <code>Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>,<instance-id-3></code> </p> <p> <b>Example 2</b>: Use tag key-pairs applied to managed nodes</p> <p> <code>Key=tag:<my-tag-key>,Values=<my-tag-value-1>,<my-tag-value-2></code> </p> <p> <b>Example 3</b>: Use tag-keys applied to managed nodes</p> <p> <code>Key=tag-key,Values=<my-tag-key-1>,<my-tag-key-2></code> </p> <p> <b>Example 4</b>: Use resource group names</p> <p> <code>Key=resource-groups:Name,Values=<resource-group-name></code> </p> <p> <b>Example 5</b>: Use filters for resource group types</p> <p> <code>Key=resource-groups:ResourceTypeFilters,Values=<resource-type-1>,<resource-type-2></code> </p> <note> <p>For <code>Key=resource-groups:ResourceTypeFilters</code>, specify resource types in the following format</p> <p> <code>Key=resource-groups:ResourceTypeFilters,Values=AWS::EC2::INSTANCE,AWS::EC2::VPC</code> </p> </note> <p>For more information about these examples formats, including the best use case for each one, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html">Examples: Register targets with a maintenance window</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    owner_information: NotRequired["capo_ssm.types.owner_information.OwnerInformation"]
    """<p>User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.</p>"""
    name: NotRequired["capo_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>An optional name for the target.</p>"""
    description: NotRequired[
        "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>An optional description for the target.</p>"""
    client_token: NotRequired["capo_ssm.types.client_token.ClientToken"]
    """<p>User-provided idempotency token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterTargetWithMaintenanceWindowRequest) -> dict:
    out: dict = {}
    out["WindowId"] = value["window_id"]
    import capo_ssm.types.maintenance_window_resource_type

    out["ResourceType"] = (
        capo_ssm.types.maintenance_window_resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    import capo_ssm.types.targets

    out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "owner_information" in value:
        out["OwnerInformation"] = value["owner_information"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterTargetWithMaintenanceWindowRequest:
    out: RegisterTargetWithMaintenanceWindowRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowId") is not None:
        out["window_id"] = data["WindowId"]
    else:
        raise DeserializationError(
            "RegisterTargetWithMaintenanceWindowRequest.window_id required"
        )
    if data.get("ResourceType") is not None:
        import capo_ssm.types.maintenance_window_resource_type

        out["resource_type"] = (
            capo_ssm.types.maintenance_window_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterTargetWithMaintenanceWindowRequest.resource_type required"
        )
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    else:
        raise DeserializationError(
            "RegisterTargetWithMaintenanceWindowRequest.targets required"
        )
    if data.get("OwnerInformation") is not None:
        out["owner_information"] = data["OwnerInformation"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
