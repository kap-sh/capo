"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DescribeProxyRequest(TypedDict, closed=True):
    proxy_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeProxyRequest) -> dict:
    out: dict = {}
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeProxyRequest:
    out: DescribeProxyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProxyRequest) -> dict:
    out: dict = {}
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeProxyRequest:
    out: DescribeProxyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    return out
