"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.nat_gateway_id
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DeleteProxyRequest(TypedDict, closed=True):
    nat_gateway_id: "capo_network_firewall.types.nat_gateway_id.NatGatewayId"
    """<p>The NAT Gateway the proxy is attached to. </p>"""
    proxy_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyRequest) -> dict:
    out: dict = {}
    out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyRequest:
    out: DeleteProxyRequest = {}  # type: ignore[typeddict-item]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    else:
        out["nat_gateway_id"] = ""
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    return out
