"""Generated from Smithy shape ``com.amazonaws.codedeploy#SkipWaitTimeForInstanceTerminationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_id


class SkipWaitTimeForInstanceTerminationInput(TypedDict, closed=True):
    deployment_id: NotRequired["capo_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a blue/green deployment for which you want to skip the instance termination wait time. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SkipWaitTimeForInstanceTerminationInput) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SkipWaitTimeForInstanceTerminationInput:
    out: SkipWaitTimeForInstanceTerminationInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SkipWaitTimeForInstanceTerminationInput) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    return out


def deserialize_cbor(data: dict) -> SkipWaitTimeForInstanceTerminationInput:
    out: SkipWaitTimeForInstanceTerminationInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    return out
