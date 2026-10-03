"""Generated from Smithy shape ``com.amazonaws.gamelift#GetComputeAccessInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.fleet_id_or_arn


class GetComputeAccessInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that holds the compute resource that you want to connect to. You can use either the fleet ID or ARN value.</p>"""
    compute_name: NotRequired[
        "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>A unique identifier for the compute resource that you want to connect to. For an EC2 fleet, use an instance ID. For a managed container fleet, use a compute name. You can retrieve a fleet's compute names by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html">ListCompute</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComputeAccessInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComputeAccessInput:
    out: GetComputeAccessInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    return out
