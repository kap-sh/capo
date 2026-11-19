"""Generated from Smithy shape ``com.amazonaws.codedeploy#BlueGreenDeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.blue_instance_termination_option
    import capo_codedeploy.types.deployment_ready_option
    import capo_codedeploy.types.green_fleet_provisioning_option


class BlueGreenDeploymentConfiguration(TypedDict, closed=True):
    terminate_blue_instances_on_deployment_success: NotRequired[
        "capo_codedeploy.types.blue_instance_termination_option.BlueInstanceTerminationOption"
    ]
    """<p>Information about whether to terminate instances in the original fleet during a blue/green deployment.</p>"""
    deployment_ready_option: NotRequired[
        "capo_codedeploy.types.deployment_ready_option.DeploymentReadyOption"
    ]
    """<p>Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.</p>"""
    green_fleet_provisioning_option: NotRequired[
        "capo_codedeploy.types.green_fleet_provisioning_option.GreenFleetProvisioningOption"
    ]
    """<p>Information about how instances are provisioned for a replacement environment in a blue/green deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueGreenDeploymentConfiguration) -> dict:
    out: dict = {}
    if "terminate_blue_instances_on_deployment_success" in value:
        import capo_codedeploy.types.blue_instance_termination_option

        out["terminateBlueInstancesOnDeploymentSuccess"] = (
            capo_codedeploy.types.blue_instance_termination_option.serialize_aws_json_1_1(
                value["terminate_blue_instances_on_deployment_success"]
            )
        )
    if "deployment_ready_option" in value:
        import capo_codedeploy.types.deployment_ready_option

        out["deploymentReadyOption"] = (
            capo_codedeploy.types.deployment_ready_option.serialize_aws_json_1_1(
                value["deployment_ready_option"]
            )
        )
    if "green_fleet_provisioning_option" in value:
        import capo_codedeploy.types.green_fleet_provisioning_option

        out["greenFleetProvisioningOption"] = (
            capo_codedeploy.types.green_fleet_provisioning_option.serialize_aws_json_1_1(
                value["green_fleet_provisioning_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlueGreenDeploymentConfiguration:
    out: BlueGreenDeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("terminateBlueInstancesOnDeploymentSuccess") is not None:
        import capo_codedeploy.types.blue_instance_termination_option

        out["terminate_blue_instances_on_deployment_success"] = (
            capo_codedeploy.types.blue_instance_termination_option.deserialize_aws_json_1_1(
                data["terminateBlueInstancesOnDeploymentSuccess"]
            )
        )
    if data.get("deploymentReadyOption") is not None:
        import capo_codedeploy.types.deployment_ready_option

        out["deployment_ready_option"] = (
            capo_codedeploy.types.deployment_ready_option.deserialize_aws_json_1_1(
                data["deploymentReadyOption"]
            )
        )
    if data.get("greenFleetProvisioningOption") is not None:
        import capo_codedeploy.types.green_fleet_provisioning_option

        out["green_fleet_provisioning_option"] = (
            capo_codedeploy.types.green_fleet_provisioning_option.deserialize_aws_json_1_1(
                data["greenFleetProvisioningOption"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlueGreenDeploymentConfiguration) -> dict:
    out: dict = {}
    if "terminate_blue_instances_on_deployment_success" in value:
        import capo_codedeploy.types.blue_instance_termination_option

        out["terminateBlueInstancesOnDeploymentSuccess"] = (
            capo_codedeploy.types.blue_instance_termination_option.serialize_cbor(
                value["terminate_blue_instances_on_deployment_success"]
            )
        )
    if "deployment_ready_option" in value:
        import capo_codedeploy.types.deployment_ready_option

        out["deploymentReadyOption"] = (
            capo_codedeploy.types.deployment_ready_option.serialize_cbor(
                value["deployment_ready_option"]
            )
        )
    if "green_fleet_provisioning_option" in value:
        import capo_codedeploy.types.green_fleet_provisioning_option

        out["greenFleetProvisioningOption"] = (
            capo_codedeploy.types.green_fleet_provisioning_option.serialize_cbor(
                value["green_fleet_provisioning_option"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BlueGreenDeploymentConfiguration:
    out: BlueGreenDeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("terminateBlueInstancesOnDeploymentSuccess") is not None:
        import capo_codedeploy.types.blue_instance_termination_option

        out["terminate_blue_instances_on_deployment_success"] = (
            capo_codedeploy.types.blue_instance_termination_option.deserialize_cbor(
                data["terminateBlueInstancesOnDeploymentSuccess"]
            )
        )
    if data.get("deploymentReadyOption") is not None:
        import capo_codedeploy.types.deployment_ready_option

        out["deployment_ready_option"] = (
            capo_codedeploy.types.deployment_ready_option.deserialize_cbor(
                data["deploymentReadyOption"]
            )
        )
    if data.get("greenFleetProvisioningOption") is not None:
        import capo_codedeploy.types.green_fleet_provisioning_option

        out["green_fleet_provisioning_option"] = (
            capo_codedeploy.types.green_fleet_provisioning_option.deserialize_cbor(
                data["greenFleetProvisioningOption"]
            )
        )
    return out
