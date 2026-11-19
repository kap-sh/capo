"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#GetWorkspaceInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.billing_configuration
    import capo_workspaces_instances.types.ec2_instance_errors
    import capo_workspaces_instances.types.ec2_managed_instance
    import capo_workspaces_instances.types.provision_state_enum
    import capo_workspaces_instances.types.workspace_instance_errors
    import capo_workspaces_instances.types.workspace_instance_id


class GetWorkspaceInstanceResponse(TypedDict, closed=True):
    workspace_instance_errors: NotRequired[
        "capo_workspaces_instances.types.workspace_instance_errors.WorkspaceInstanceErrors"
    ]
    """<p>Captures any errors specific to the WorkSpace Instance lifecycle.</p>"""
    ec2_instance_errors: NotRequired[
        "capo_workspaces_instances.types.ec2_instance_errors.EC2InstanceErrors"
    ]
    """<p>Includes any underlying EC2 instance errors encountered.</p>"""
    provision_state: NotRequired[
        "capo_workspaces_instances.types.provision_state_enum.ProvisionStateEnum"
    ]
    """<p>Current provisioning state of the WorkSpaces Instance.</p>"""
    workspace_instance_id: NotRequired[
        "capo_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    ]
    """<p>Unique identifier of the retrieved WorkSpaces Instance.</p>"""
    ec2_managed_instance: NotRequired[
        "capo_workspaces_instances.types.ec2_managed_instance.EC2ManagedInstance"
    ]
    """<p>Details of the associated EC2 managed instance.</p>"""
    billing_configuration: NotRequired[
        "capo_workspaces_instances.types.billing_configuration.BillingConfiguration"
    ]
    """<p>Returns the current billing configuration for the WorkSpace Instance, indicating the active billing mode.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkspaceInstanceResponse) -> dict:
    out: dict = {}
    if "workspace_instance_errors" in value:
        import capo_workspaces_instances.types.workspace_instance_errors

        out["WorkspaceInstanceErrors"] = (
            capo_workspaces_instances.types.workspace_instance_errors.serialize_aws_json_1_0(
                value["workspace_instance_errors"]
            )
        )
    if "ec2_instance_errors" in value:
        import capo_workspaces_instances.types.ec2_instance_errors

        out["EC2InstanceErrors"] = (
            capo_workspaces_instances.types.ec2_instance_errors.serialize_aws_json_1_0(
                value["ec2_instance_errors"]
            )
        )
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
    if "billing_configuration" in value:
        import capo_workspaces_instances.types.billing_configuration

        out["BillingConfiguration"] = (
            capo_workspaces_instances.types.billing_configuration.serialize_aws_json_1_0(
                value["billing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkspaceInstanceResponse:
    out: GetWorkspaceInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstanceErrors") is not None:
        import capo_workspaces_instances.types.workspace_instance_errors

        out["workspace_instance_errors"] = (
            capo_workspaces_instances.types.workspace_instance_errors.deserialize_aws_json_1_0(
                data["WorkspaceInstanceErrors"]
            )
        )
    if data.get("EC2InstanceErrors") is not None:
        import capo_workspaces_instances.types.ec2_instance_errors

        out["ec2_instance_errors"] = (
            capo_workspaces_instances.types.ec2_instance_errors.deserialize_aws_json_1_0(
                data["EC2InstanceErrors"]
            )
        )
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
    if data.get("BillingConfiguration") is not None:
        import capo_workspaces_instances.types.billing_configuration

        out["billing_configuration"] = (
            capo_workspaces_instances.types.billing_configuration.deserialize_aws_json_1_0(
                data["BillingConfiguration"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetWorkspaceInstanceResponse) -> dict:
    out: dict = {}
    if "workspace_instance_errors" in value:
        import capo_workspaces_instances.types.workspace_instance_errors

        out["WorkspaceInstanceErrors"] = (
            capo_workspaces_instances.types.workspace_instance_errors.serialize_cbor(
                value["workspace_instance_errors"]
            )
        )
    if "ec2_instance_errors" in value:
        import capo_workspaces_instances.types.ec2_instance_errors

        out["EC2InstanceErrors"] = (
            capo_workspaces_instances.types.ec2_instance_errors.serialize_cbor(
                value["ec2_instance_errors"]
            )
        )
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
    if "billing_configuration" in value:
        import capo_workspaces_instances.types.billing_configuration

        out["BillingConfiguration"] = (
            capo_workspaces_instances.types.billing_configuration.serialize_cbor(
                value["billing_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetWorkspaceInstanceResponse:
    out: GetWorkspaceInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceInstanceErrors") is not None:
        import capo_workspaces_instances.types.workspace_instance_errors

        out["workspace_instance_errors"] = (
            capo_workspaces_instances.types.workspace_instance_errors.deserialize_cbor(
                data["WorkspaceInstanceErrors"]
            )
        )
    if data.get("EC2InstanceErrors") is not None:
        import capo_workspaces_instances.types.ec2_instance_errors

        out["ec2_instance_errors"] = (
            capo_workspaces_instances.types.ec2_instance_errors.deserialize_cbor(
                data["EC2InstanceErrors"]
            )
        )
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
    if data.get("BillingConfiguration") is not None:
        import capo_workspaces_instances.types.billing_configuration

        out["billing_configuration"] = (
            capo_workspaces_instances.types.billing_configuration.deserialize_cbor(
                data["BillingConfiguration"]
            )
        )
    return out
