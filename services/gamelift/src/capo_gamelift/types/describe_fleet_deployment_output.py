"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_deployment
    import capo_gamelift.types.locational_deployments


class DescribeFleetDeploymentOutput(TypedDict, closed=True):
    fleet_deployment: NotRequired[
        "capo_gamelift.types.fleet_deployment.FleetDeployment"
    ]
    """<p>The requested deployment information.</p>"""
    locational_deployments: NotRequired[
        "capo_gamelift.types.locational_deployments.LocationalDeployments"
    ]
    """<p>If the deployment is for a multi-location fleet, the requests returns the deployment status in each fleet location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetDeploymentOutput) -> dict:
    out: dict = {}
    if "fleet_deployment" in value:
        import capo_gamelift.types.fleet_deployment

        out["FleetDeployment"] = (
            capo_gamelift.types.fleet_deployment.serialize_aws_json_1_1(
                value["fleet_deployment"]
            )
        )
    if "locational_deployments" in value:
        import capo_gamelift.types.locational_deployments

        out["LocationalDeployments"] = (
            capo_gamelift.types.locational_deployments.serialize_aws_json_1_1(
                value["locational_deployments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetDeploymentOutput:
    out: DescribeFleetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetDeployment") is not None:
        import capo_gamelift.types.fleet_deployment

        out["fleet_deployment"] = (
            capo_gamelift.types.fleet_deployment.deserialize_aws_json_1_1(
                data["FleetDeployment"]
            )
        )
    if data.get("LocationalDeployments") is not None:
        import capo_gamelift.types.locational_deployments

        out["locational_deployments"] = (
            capo_gamelift.types.locational_deployments.deserialize_aws_json_1_1(
                data["LocationalDeployments"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetDeploymentOutput) -> dict:
    out: dict = {}
    if "fleet_deployment" in value:
        import capo_gamelift.types.fleet_deployment

        out["FleetDeployment"] = capo_gamelift.types.fleet_deployment.serialize_cbor(
            value["fleet_deployment"]
        )
    if "locational_deployments" in value:
        import capo_gamelift.types.locational_deployments

        out["LocationalDeployments"] = (
            capo_gamelift.types.locational_deployments.serialize_cbor(
                value["locational_deployments"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeFleetDeploymentOutput:
    out: DescribeFleetDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetDeployment") is not None:
        import capo_gamelift.types.fleet_deployment

        out["fleet_deployment"] = capo_gamelift.types.fleet_deployment.deserialize_cbor(
            data["FleetDeployment"]
        )
    if data.get("LocationalDeployments") is not None:
        import capo_gamelift.types.locational_deployments

        out["locational_deployments"] = (
            capo_gamelift.types.locational_deployments.deserialize_cbor(
                data["LocationalDeployments"]
            )
        )
    return out
