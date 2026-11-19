"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetCapacityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_capacity_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeFleetCapacityOutput(TypedDict, closed=True):
    fleet_capacity: NotRequired[
        "capo_gamelift.types.fleet_capacity_list.FleetCapacityList"
    ]
    """<p>A collection of objects that contains capacity information for each requested fleet ID. Capacity objects are returned only for fleets that currently exist. Changes in desired instance value can take up to 1 minute to be reflected.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetCapacityOutput) -> dict:
    out: dict = {}
    if "fleet_capacity" in value:
        import capo_gamelift.types.fleet_capacity_list

        out["FleetCapacity"] = (
            capo_gamelift.types.fleet_capacity_list.serialize_aws_json_1_1(
                value["fleet_capacity"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetCapacityOutput:
    out: DescribeFleetCapacityOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetCapacity") is not None:
        import capo_gamelift.types.fleet_capacity_list

        out["fleet_capacity"] = (
            capo_gamelift.types.fleet_capacity_list.deserialize_aws_json_1_1(
                data["FleetCapacity"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetCapacityOutput) -> dict:
    out: dict = {}
    if "fleet_capacity" in value:
        import capo_gamelift.types.fleet_capacity_list

        out["FleetCapacity"] = capo_gamelift.types.fleet_capacity_list.serialize_cbor(
            value["fleet_capacity"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeFleetCapacityOutput:
    out: DescribeFleetCapacityOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetCapacity") is not None:
        import capo_gamelift.types.fleet_capacity_list

        out["fleet_capacity"] = (
            capo_gamelift.types.fleet_capacity_list.deserialize_cbor(
                data["FleetCapacity"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
