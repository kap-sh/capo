"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.deployment_id
    import capo_gamelift.types.fleet_id_or_arn


class DescribeFleetDeploymentInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the container fleet. You can use either the fleet ID or ARN value.</p>"""
    deployment_id: NotRequired["capo_gamelift.types.deployment_id.DeploymentId"]
    """<p>A unique identifier for the deployment to return information for. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetDeploymentInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetDeploymentInput:
    out: DescribeFleetDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("DeploymentId") is not None:
        out["deployment_id"] = data["DeploymentId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetDeploymentInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "deployment_id" in value:
        out["DeploymentId"] = value["deployment_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeFleetDeploymentInput:
    out: DescribeFleetDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("DeploymentId") is not None:
        out["deployment_id"] = data["DeploymentId"]
    return out
