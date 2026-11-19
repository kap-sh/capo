"""Generated from Smithy shape ``com.amazonaws.gamelift#DeploymentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.deployment_id


class DeploymentDetails(TypedDict, closed=True):
    latest_deployment_id: NotRequired["capo_gamelift.types.deployment_id.DeploymentId"]
    """<p>A unique identifier for a fleet deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentDetails) -> dict:
    out: dict = {}
    if "latest_deployment_id" in value:
        out["LatestDeploymentId"] = value["latest_deployment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentDetails:
    out: DeploymentDetails = {}  # type: ignore[typeddict-item]
    if data.get("LatestDeploymentId") is not None:
        out["latest_deployment_id"] = data["LatestDeploymentId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentDetails) -> dict:
    out: dict = {}
    if "latest_deployment_id" in value:
        out["LatestDeploymentId"] = value["latest_deployment_id"]
    return out


def deserialize_cbor(data: dict) -> DeploymentDetails:
    out: DeploymentDetails = {}  # type: ignore[typeddict-item]
    if data.get("LatestDeploymentId") is not None:
        out["latest_deployment_id"] = data["LatestDeploymentId"]
    return out
