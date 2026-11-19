"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#WorkspaceInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ec2_managed_instance
    import capo_workspaces_instances.types.provision_state_enum
    import capo_workspaces_instances.types.workspace_instance_id


class WorkspaceInstance(TypedDict, closed=True):
    provision_state: NotRequired[
        "capo_workspaces_instances.types.provision_state_enum.ProvisionStateEnum"
    ]
    """<p>Current provisioning state of the WorkSpace Instance.</p>"""
    workspace_instance_id: NotRequired[
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    ]
    """<p>Unique identifier for the WorkSpace Instance.</p>"""
    ec2_managed_instance: NotRequired[
        "capo_workspaces_instances.types.ec2_managed_instance.EC2ManagedInstance"
    ]
    """<p>Details of the associated EC2 managed instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkspaceInstance) -> dict:
    out: dict = {}
    if "provision_state" in value:
        import capo_workspaces_instances.types.provision_state_enum

        out["ProvisionState"] = (
            capo_workspaces_instances.types.provision_state_enum.serialize_aws_json_1_0(
                value["provision_state"]
            )
        )
    if "workspace_instance_id" in value:
        out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    if "ec2_managed_instance" in value:
        import capo_workspaces_instances.types.ec2_managed_instance

        out["EC2ManagedInstance"] = (
            capo_workspaces_instances.types.ec2_managed_instance.serialize_aws_json_1_0(
                value["ec2_managed_instance"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkspaceInstance:
    out: WorkspaceInstance = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionState") is not None:
        import capo_workspaces_instances.types.provision_state_enum

        out["provision_state"] = (
            capo_workspaces_instances.types.provision_state_enum.deserialize_aws_json_1_0(
                data["ProvisionState"]
            )
        )
    if data.get("WorkspaceInstanceId") is not None:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    if data.get("EC2ManagedInstance") is not None:
        import capo_workspaces_instances.types.ec2_managed_instance

        out["ec2_managed_instance"] = (
            capo_workspaces_instances.types.ec2_managed_instance.deserialize_aws_json_1_0(
                data["EC2ManagedInstance"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceInstance) -> dict:
    out: dict = {}
    if "provision_state" in value:
        import capo_workspaces_instances.types.provision_state_enum

        out["ProvisionState"] = (
            capo_workspaces_instances.types.provision_state_enum.serialize_cbor(
                value["provision_state"]
            )
        )
    if "workspace_instance_id" in value:
        out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    if "ec2_managed_instance" in value:
        import capo_workspaces_instances.types.ec2_managed_instance

        out["EC2ManagedInstance"] = (
            capo_workspaces_instances.types.ec2_managed_instance.serialize_cbor(
                value["ec2_managed_instance"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> WorkspaceInstance:
    out: WorkspaceInstance = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionState") is not None:
        import capo_workspaces_instances.types.provision_state_enum

        out["provision_state"] = (
            capo_workspaces_instances.types.provision_state_enum.deserialize_cbor(
                data["ProvisionState"]
            )
        )
    if data.get("WorkspaceInstanceId") is not None:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    if data.get("EC2ManagedInstance") is not None:
        import capo_workspaces_instances.types.ec2_managed_instance

        out["ec2_managed_instance"] = (
            capo_workspaces_instances.types.ec2_managed_instance.deserialize_cbor(
                data["EC2ManagedInstance"]
            )
        )
    return out
