"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateVpcPeeringAuthorizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.vpc_peering_authorization


class CreateVpcPeeringAuthorizationOutput(TypedDict, closed=True):
    vpc_peering_authorization: NotRequired[
        "capo_gamelift.types.vpc_peering_authorization.VpcPeeringAuthorization"
    ]
    """<p>Details on the requested VPC peering authorization, including expiration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVpcPeeringAuthorizationOutput) -> dict:
    out: dict = {}
    if "vpc_peering_authorization" in value:
        import capo_gamelift.types.vpc_peering_authorization

        out["VpcPeeringAuthorization"] = (
            capo_gamelift.types.vpc_peering_authorization.serialize_aws_json_1_1(
                value["vpc_peering_authorization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVpcPeeringAuthorizationOutput:
    out: CreateVpcPeeringAuthorizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("VpcPeeringAuthorization") is not None:
        import capo_gamelift.types.vpc_peering_authorization

        out["vpc_peering_authorization"] = (
            capo_gamelift.types.vpc_peering_authorization.deserialize_aws_json_1_1(
                data["VpcPeeringAuthorization"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateVpcPeeringAuthorizationOutput) -> dict:
    out: dict = {}
    if "vpc_peering_authorization" in value:
        import capo_gamelift.types.vpc_peering_authorization

        out["VpcPeeringAuthorization"] = (
            capo_gamelift.types.vpc_peering_authorization.serialize_cbor(
                value["vpc_peering_authorization"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateVpcPeeringAuthorizationOutput:
    out: CreateVpcPeeringAuthorizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("VpcPeeringAuthorization") is not None:
        import capo_gamelift.types.vpc_peering_authorization

        out["vpc_peering_authorization"] = (
            capo_gamelift.types.vpc_peering_authorization.deserialize_cbor(
                data["VpcPeeringAuthorization"]
            )
        )
    return out
