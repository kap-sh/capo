"""Generated from Smithy shape ``com.amazonaws.apigateway#EndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.ip_address_type
    import capo_api_gateway.types.list_of_endpoint_type
    import capo_api_gateway.types.list_of_string


class EndpointConfiguration(TypedDict, closed=True):
    types: NotRequired[
        "capo_api_gateway.types.list_of_endpoint_type.ListOfEndpointType"
    ]
    """<p>A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is <code>"EDGE"</code>. For a regional API and its custom domain name, the endpoint type is <code>REGIONAL</code>. For a private API, the endpoint type is <code>PRIVATE</code>.</p>"""
    ip_address_type: NotRequired["capo_api_gateway.types.ip_address_type.IpAddressType"]
    """<p>The IP address types that can invoke an API (RestApi) or a DomainName. Use <code>ipv4</code> to allow only IPv4 addresses to invoke an API or DomainName, or use <code>dualstack</code> to allow both IPv4 and IPv6 addresses to invoke an API or a DomainName. For the <code>PRIVATE</code> endpoint type, only <code>dualstack</code> is supported.</p>"""
    vpc_endpoint_ids: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for <code>PRIVATE</code> endpoint type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointConfiguration) -> dict:
    out: dict = {}
    if "types" in value:
        import capo_api_gateway.types.list_of_endpoint_type

        out["types"] = capo_api_gateway.types.list_of_endpoint_type.serialize_json(
            value["types"]
        )
    if "ip_address_type" in value:
        import capo_api_gateway.types.ip_address_type

        out["ipAddressType"] = capo_api_gateway.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    if "vpc_endpoint_ids" in value:
        import capo_api_gateway.types.list_of_string

        out["vpcEndpointIds"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["vpc_endpoint_ids"]
        )
    return out


def deserialize_json(data: dict) -> EndpointConfiguration:
    out: EndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("types") is not None:
        import capo_api_gateway.types.list_of_endpoint_type

        out["types"] = capo_api_gateway.types.list_of_endpoint_type.deserialize_json(
            data["types"]
        )
    if data.get("ipAddressType") is not None:
        import capo_api_gateway.types.ip_address_type

        out["ip_address_type"] = (
            capo_api_gateway.types.ip_address_type.deserialize_json(
                data["ipAddressType"]
            )
        )
    if data.get("vpcEndpointIds") is not None:
        import capo_api_gateway.types.list_of_string

        out["vpc_endpoint_ids"] = (
            capo_api_gateway.types.list_of_string.deserialize_json(
                data["vpcEndpointIds"]
            )
        )
    return out
