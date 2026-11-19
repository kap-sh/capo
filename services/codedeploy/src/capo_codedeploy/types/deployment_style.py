"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_option
    import capo_codedeploy.types.deployment_type


class DeploymentStyle(TypedDict, closed=True):
    deployment_type: NotRequired["capo_codedeploy.types.deployment_type.DeploymentType"]
    """<p>Indicates whether to run an in-place deployment or a blue/green deployment.</p>"""
    deployment_option: NotRequired[
        "capo_codedeploy.types.deployment_option.DeploymentOption"
    ]
    """<p>Indicates whether to route deployment traffic behind a load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStyle) -> dict:
    out: dict = {}
    if "deployment_type" in value:
        import capo_codedeploy.types.deployment_type

        out["deploymentType"] = (
            capo_codedeploy.types.deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "deployment_option" in value:
        import capo_codedeploy.types.deployment_option

        out["deploymentOption"] = (
            capo_codedeploy.types.deployment_option.serialize_aws_json_1_1(
                value["deployment_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentStyle:
    out: DeploymentStyle = {}  # type: ignore[typeddict-item]
    if data.get("deploymentType") is not None:
        import capo_codedeploy.types.deployment_type

        out["deployment_type"] = (
            capo_codedeploy.types.deployment_type.deserialize_aws_json_1_1(
                data["deploymentType"]
            )
        )
    if data.get("deploymentOption") is not None:
        import capo_codedeploy.types.deployment_option

        out["deployment_option"] = (
            capo_codedeploy.types.deployment_option.deserialize_aws_json_1_1(
                data["deploymentOption"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentStyle) -> dict:
    out: dict = {}
    if "deployment_type" in value:
        import capo_codedeploy.types.deployment_type

        out["deploymentType"] = capo_codedeploy.types.deployment_type.serialize_cbor(
            value["deployment_type"]
        )
    if "deployment_option" in value:
        import capo_codedeploy.types.deployment_option

        out["deploymentOption"] = (
            capo_codedeploy.types.deployment_option.serialize_cbor(
                value["deployment_option"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeploymentStyle:
    out: DeploymentStyle = {}  # type: ignore[typeddict-item]
    if data.get("deploymentType") is not None:
        import capo_codedeploy.types.deployment_type

        out["deployment_type"] = capo_codedeploy.types.deployment_type.deserialize_cbor(
            data["deploymentType"]
        )
    if data.get("deploymentOption") is not None:
        import capo_codedeploy.types.deployment_option

        out["deployment_option"] = (
            capo_codedeploy.types.deployment_option.deserialize_cbor(
                data["deploymentOption"]
            )
        )
    return out
