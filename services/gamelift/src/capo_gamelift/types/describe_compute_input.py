"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeComputeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.fleet_id_or_arn


class DescribeComputeInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that the compute belongs to. You can use either the fleet ID or ARN value.</p>"""
    compute_name: NotRequired[
        "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>The unique identifier of the compute resource to retrieve properties for. For a managed container fleet or Anywhere fleet, use a compute name. For an EC2 fleet, use an instance ID. To retrieve a fleet's compute identifiers, call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html">ListCompute</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComputeInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComputeInput:
    out: DescribeComputeInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    return out
