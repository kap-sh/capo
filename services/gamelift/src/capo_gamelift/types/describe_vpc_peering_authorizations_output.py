"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeVpcPeeringAuthorizationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.vpc_peering_authorization_list


class DescribeVpcPeeringAuthorizationsOutput(TypedDict, closed=True):
    vpc_peering_authorizations: NotRequired[
        "capo_gamelift.types.vpc_peering_authorization_list.VpcPeeringAuthorizationList"
    ]
    """<p>A collection of objects that describe all valid VPC peering operations for the current Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVpcPeeringAuthorizationsOutput) -> dict:
    out: dict = {}
    if "vpc_peering_authorizations" in value:
        import capo_gamelift.types.vpc_peering_authorization_list

        out["VpcPeeringAuthorizations"] = (
            capo_gamelift.types.vpc_peering_authorization_list.serialize_aws_json_1_1(
                value["vpc_peering_authorizations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVpcPeeringAuthorizationsOutput:
    out: DescribeVpcPeeringAuthorizationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("VpcPeeringAuthorizations") is not None:
        import capo_gamelift.types.vpc_peering_authorization_list

        out["vpc_peering_authorizations"] = (
            capo_gamelift.types.vpc_peering_authorization_list.deserialize_aws_json_1_1(
                data["VpcPeeringAuthorizations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeVpcPeeringAuthorizationsOutput) -> dict:
    out: dict = {}
    if "vpc_peering_authorizations" in value:
        import capo_gamelift.types.vpc_peering_authorization_list

        out["VpcPeeringAuthorizations"] = (
            capo_gamelift.types.vpc_peering_authorization_list.serialize_cbor(
                value["vpc_peering_authorizations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeVpcPeeringAuthorizationsOutput:
    out: DescribeVpcPeeringAuthorizationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("VpcPeeringAuthorizations") is not None:
        import capo_gamelift.types.vpc_peering_authorization_list

        out["vpc_peering_authorizations"] = (
            capo_gamelift.types.vpc_peering_authorization_list.deserialize_cbor(
                data["VpcPeeringAuthorizations"]
            )
        )
    return out
