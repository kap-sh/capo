"""Generated from Smithy shape ``com.amazonaws.gamelift#VpcPeeringAuthorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.timestamp


class VpcPeeringAuthorization(TypedDict, closed=True):
    game_lift_aws_account_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for the Amazon Web Services account that you use to manage your Amazon GameLift Servers fleet. You can find your Account ID in the Amazon Web Services Management Console under account settings.</p>"""
    peer_vpc_aws_account_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>The authorization's peer VPC Amazon Web Services account ID.</p>"""
    peer_vpc_id: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href="https://console.aws.amazon.com/vpc/">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>"""
    creation_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>Time stamp indicating when this authorization was issued. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""
    expiration_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>Time stamp indicating when this authorization expires (24 hours after issuance). Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcPeeringAuthorization) -> dict:
    out: dict = {}
    if "game_lift_aws_account_id" in value:
        out["GameLiftAwsAccountId"] = value["game_lift_aws_account_id"]
    if "peer_vpc_aws_account_id" in value:
        out["PeerVpcAwsAccountId"] = value["peer_vpc_aws_account_id"]
    if "peer_vpc_id" in value:
        out["PeerVpcId"] = value["peer_vpc_id"]
    if "creation_time" in value:
        import capo_gamelift.types.timestamp

        out["CreationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "expiration_time" in value:
        import capo_gamelift.types.timestamp

        out["ExpirationTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["expiration_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VpcPeeringAuthorization:
    out: VpcPeeringAuthorization = {}  # type: ignore[typeddict-item]
    if data.get("GameLiftAwsAccountId") is not None:
        out["game_lift_aws_account_id"] = data["GameLiftAwsAccountId"]
    if data.get("PeerVpcAwsAccountId") is not None:
        out["peer_vpc_aws_account_id"] = data["PeerVpcAwsAccountId"]
    if data.get("PeerVpcId") is not None:
        out["peer_vpc_id"] = data["PeerVpcId"]
    if data.get("CreationTime") is not None:
        import capo_gamelift.types.timestamp

        out["creation_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("ExpirationTime") is not None:
        import capo_gamelift.types.timestamp

        out["expiration_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["ExpirationTime"]
        )
    return out
