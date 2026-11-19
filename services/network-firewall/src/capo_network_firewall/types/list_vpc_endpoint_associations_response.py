"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListVpcEndpointAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.vpc_endpoint_associations


class ListVpcEndpointAssociationsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    vpc_endpoint_associations: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_associations.VpcEndpointAssociations"
    ]
    """<p>The VPC endpoint assocation metadata objects for the firewall that you specified. If you didn't specify a firewall, this is all VPC endpoint associations that you have defined. </p> <p>Depending on your setting for max results and the number of firewalls you have, a single call might not be the full list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcEndpointAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vpc_endpoint_associations" in value:
        import capo_network_firewall.types.vpc_endpoint_associations

        out["VpcEndpointAssociations"] = (
            capo_network_firewall.types.vpc_endpoint_associations.serialize_aws_json_1_0(
                value["vpc_endpoint_associations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcEndpointAssociationsResponse:
    out: ListVpcEndpointAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("VpcEndpointAssociations") is not None:
        import capo_network_firewall.types.vpc_endpoint_associations

        out["vpc_endpoint_associations"] = (
            capo_network_firewall.types.vpc_endpoint_associations.deserialize_aws_json_1_0(
                data["VpcEndpointAssociations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVpcEndpointAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "vpc_endpoint_associations" in value:
        import capo_network_firewall.types.vpc_endpoint_associations

        out["VpcEndpointAssociations"] = (
            capo_network_firewall.types.vpc_endpoint_associations.serialize_cbor(
                value["vpc_endpoint_associations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListVpcEndpointAssociationsResponse:
    out: ListVpcEndpointAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("VpcEndpointAssociations") is not None:
        import capo_network_firewall.types.vpc_endpoint_associations

        out["vpc_endpoint_associations"] = (
            capo_network_firewall.types.vpc_endpoint_associations.deserialize_cbor(
                data["VpcEndpointAssociations"]
            )
        )
    return out
