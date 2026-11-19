"""Generated from Smithy shape ``com.amazonaws.codedeploy#CreateDeploymentConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_config_id


class CreateDeploymentConfigOutput(TypedDict, closed=True):
    deployment_config_id: NotRequired[
        "capo_codedeploy.types.deployment_config_id.DeploymentConfigId"
    ]
    """<p>A unique deployment configuration ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDeploymentConfigOutput) -> dict:
    out: dict = {}
    if "deployment_config_id" in value:
        out["deploymentConfigId"] = value["deployment_config_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDeploymentConfigOutput:
    out: CreateDeploymentConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentConfigId") is not None:
        out["deployment_config_id"] = data["deploymentConfigId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateDeploymentConfigOutput) -> dict:
    out: dict = {}
    if "deployment_config_id" in value:
        out["deploymentConfigId"] = value["deployment_config_id"]
    return out


def deserialize_cbor(data: dict) -> CreateDeploymentConfigOutput:
    out: CreateDeploymentConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentConfigId") is not None:
        out["deployment_config_id"] = data["deploymentConfigId"]
    return out
