"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeVpcPeeringConnectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.vpc_peering_connection_list


class DescribeVpcPeeringConnectionsOutput(TypedDict, closed=True):
    vpc_peering_connections: NotRequired[
        "capo_gamelift.types.vpc_peering_connection_list.VpcPeeringConnectionList"
    ]
    """<p>A collection of VPC peering connection records that match the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVpcPeeringConnectionsOutput) -> dict:
    out: dict = {}
    if "vpc_peering_connections" in value:
        import capo_gamelift.types.vpc_peering_connection_list

        out["VpcPeeringConnections"] = (
            capo_gamelift.types.vpc_peering_connection_list.serialize_aws_json_1_1(
                value["vpc_peering_connections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVpcPeeringConnectionsOutput:
    out: DescribeVpcPeeringConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("VpcPeeringConnections") is not None:
        import capo_gamelift.types.vpc_peering_connection_list

        out["vpc_peering_connections"] = (
            capo_gamelift.types.vpc_peering_connection_list.deserialize_aws_json_1_1(
                data["VpcPeeringConnections"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeVpcPeeringConnectionsOutput) -> dict:
    out: dict = {}
    if "vpc_peering_connections" in value:
        import capo_gamelift.types.vpc_peering_connection_list

        out["VpcPeeringConnections"] = (
            capo_gamelift.types.vpc_peering_connection_list.serialize_cbor(
                value["vpc_peering_connections"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeVpcPeeringConnectionsOutput:
    out: DescribeVpcPeeringConnectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("VpcPeeringConnections") is not None:
        import capo_gamelift.types.vpc_peering_connection_list

        out["vpc_peering_connections"] = (
            capo_gamelift.types.vpc_peering_connection_list.deserialize_cbor(
                data["VpcPeeringConnections"]
            )
        )
    return out
