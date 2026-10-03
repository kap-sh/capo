"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateVpcPeeringConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.non_zero_and_max_string


class CreateVpcPeeringConnectionInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet. You can use either the fleet ID or ARN value. This tells Amazon GameLift Servers which GameLift VPC to peer with. </p>"""
    peer_vpc_aws_account_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for the Amazon Web Services account with the VPC that you want to peer your Amazon GameLift Servers fleet with. You can find your Account ID in the Amazon Web Services Management Console under account settings.</p>"""
    peer_vpc_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href="https://console.aws.amazon.com/vpc/">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVpcPeeringConnectionInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "peer_vpc_aws_account_id" in value:
        out["PeerVpcAwsAccountId"] = value["peer_vpc_aws_account_id"]
    if "peer_vpc_id" in value:
        out["PeerVpcId"] = value["peer_vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVpcPeeringConnectionInput:
    out: CreateVpcPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("PeerVpcAwsAccountId") is not None:
        out["peer_vpc_aws_account_id"] = data["PeerVpcAwsAccountId"]
    if data.get("PeerVpcId") is not None:
        out["peer_vpc_id"] = data["PeerVpcId"]
    return out
