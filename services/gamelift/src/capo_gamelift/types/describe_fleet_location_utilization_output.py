"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetLocationUtilizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_utilization


class DescribeFleetLocationUtilizationOutput(TypedDict, closed=True):
    fleet_utilization: NotRequired[
        "capo_gamelift.types.fleet_utilization.FleetUtilization"
    ]
    """<p>Utilization information for the requested fleet location. Utilization objects are returned only for fleets and locations that currently exist.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetLocationUtilizationOutput) -> dict:
    out: dict = {}
    if "fleet_utilization" in value:
        import capo_gamelift.types.fleet_utilization

        out["FleetUtilization"] = (
            capo_gamelift.types.fleet_utilization.serialize_aws_json_1_1(
                value["fleet_utilization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetLocationUtilizationOutput:
    out: DescribeFleetLocationUtilizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetUtilization") is not None:
        import capo_gamelift.types.fleet_utilization

        out["fleet_utilization"] = (
            capo_gamelift.types.fleet_utilization.deserialize_aws_json_1_1(
                data["FleetUtilization"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetLocationUtilizationOutput) -> dict:
    out: dict = {}
    if "fleet_utilization" in value:
        import capo_gamelift.types.fleet_utilization

        out["FleetUtilization"] = capo_gamelift.types.fleet_utilization.serialize_cbor(
            value["fleet_utilization"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeFleetLocationUtilizationOutput:
    out: DescribeFleetLocationUtilizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetUtilization") is not None:
        import capo_gamelift.types.fleet_utilization

        out["fleet_utilization"] = (
            capo_gamelift.types.fleet_utilization.deserialize_cbor(
                data["FleetUtilization"]
            )
        )
    return out
