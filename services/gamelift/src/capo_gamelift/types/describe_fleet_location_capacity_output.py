"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetLocationCapacityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_capacity


class DescribeFleetLocationCapacityOutput(TypedDict, closed=True):
    fleet_capacity: NotRequired["capo_gamelift.types.fleet_capacity.FleetCapacity"]
    """<p>Resource capacity information for the requested fleet location. Capacity objects are returned only for fleets and locations that currently exist. Changes in desired instance value can take up to 1 minute to be reflected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetLocationCapacityOutput) -> dict:
    out: dict = {}
    if "fleet_capacity" in value:
        import capo_gamelift.types.fleet_capacity

        out["FleetCapacity"] = (
            capo_gamelift.types.fleet_capacity.serialize_aws_json_1_1(
                value["fleet_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetLocationCapacityOutput:
    out: DescribeFleetLocationCapacityOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetCapacity") is not None:
        import capo_gamelift.types.fleet_capacity

        out["fleet_capacity"] = (
            capo_gamelift.types.fleet_capacity.deserialize_aws_json_1_1(
                data["FleetCapacity"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetLocationCapacityOutput) -> dict:
    out: dict = {}
    if "fleet_capacity" in value:
        import capo_gamelift.types.fleet_capacity

        out["FleetCapacity"] = capo_gamelift.types.fleet_capacity.serialize_cbor(
            value["fleet_capacity"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeFleetLocationCapacityOutput:
    out: DescribeFleetLocationCapacityOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetCapacity") is not None:
        import capo_gamelift.types.fleet_capacity

        out["fleet_capacity"] = capo_gamelift.types.fleet_capacity.deserialize_cbor(
            data["FleetCapacity"]
        )
    return out
