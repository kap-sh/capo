"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.nat_gateway_id
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DeleteProxyResponse(TypedDict, closed=True):
    nat_gateway_id: NotRequired[
        "capo_network_firewall.types.nat_gateway_id.NatGatewayId"
    ]
    """<p>The NAT Gateway the Proxy was attached to. </p>"""
    proxy_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p>"""
    proxy_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyResponse) -> dict:
    out: dict = {}
    if "nat_gateway_id" in value:
        out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyResponse:
    out: DeleteProxyResponse = {}  # type: ignore[typeddict-item]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteProxyResponse) -> dict:
    out: dict = {}
    if "nat_gateway_id" in value:
        out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    return out


def deserialize_cbor(data: dict) -> DeleteProxyResponse:
    out: DeleteProxyResponse = {}  # type: ignore[typeddict-item]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    return out
