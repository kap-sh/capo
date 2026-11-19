"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeVpcPeeringConnectionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id


class DescribeVpcPeeringConnectionsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet. You can use either the fleet ID or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVpcPeeringConnectionsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVpcPeeringConnectionsInput:
    out: DescribeVpcPeeringConnectionsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeVpcPeeringConnectionsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeVpcPeeringConnectionsInput:
    out: DescribeVpcPeeringConnectionsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    return out
