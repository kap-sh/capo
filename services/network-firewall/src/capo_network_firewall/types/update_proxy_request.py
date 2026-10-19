"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.listener_properties_request
    import capo_network_firewall.types.nat_gateway_id
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.tls_intercept_properties_request
    import capo_network_firewall.types.update_token


class UpdateProxyRequest(TypedDict, closed=True):
    nat_gateway_id: "capo_network_firewall.types.nat_gateway_id.NatGatewayId"
    """<p>The NAT Gateway the proxy is attached to. </p>"""
    proxy_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the proxy. You can't change the name of a proxy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a proxy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    listener_properties_to_add: NotRequired[
        "capo_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
    ]
    """<p>Listener properties for HTTP and HTTPS traffic to add. </p>"""
    listener_properties_to_remove: NotRequired[
        "capo_network_firewall.types.listener_properties_request.ListenerPropertiesRequest"
    ]
    """<p>Listener properties for HTTP and HTTPS traffic to remove. </p>"""
    tls_intercept_properties: NotRequired[
        "capo_network_firewall.types.tls_intercept_properties_request.TlsInterceptPropertiesRequest"
    ]
    """<p>TLS decryption on traffic to filter on attributes in the HTTP header. </p>"""
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy. The token marks the state of the proxy resource at the time of the request. </p> <p>To make changes to the proxy, you provide the token in your request. Network Firewall uses the token to ensure that the proxy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRequest) -> dict:
    out: dict = {}
    out["NatGatewayId"] = value["nat_gateway_id"]
    if "proxy_name" in value:
        out["ProxyName"] = value["proxy_name"]
    if "proxy_arn" in value:
        out["ProxyArn"] = value["proxy_arn"]
    if "listener_properties_to_add" in value:
        import capo_network_firewall.types.listener_properties_request

        out["ListenerPropertiesToAdd"] = (
            capo_network_firewall.types.listener_properties_request.serialize_aws_json_1_0(
                value["listener_properties_to_add"]
            )
        )
    if "listener_properties_to_remove" in value:
        import capo_network_firewall.types.listener_properties_request

        out["ListenerPropertiesToRemove"] = (
            capo_network_firewall.types.listener_properties_request.serialize_aws_json_1_0(
                value["listener_properties_to_remove"]
            )
        )
    if "tls_intercept_properties" in value:
        import capo_network_firewall.types.tls_intercept_properties_request

        out["TlsInterceptProperties"] = (
            capo_network_firewall.types.tls_intercept_properties_request.serialize_aws_json_1_0(
                value["tls_intercept_properties"]
            )
        )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRequest:
    out: UpdateProxyRequest = {}  # type: ignore[typeddict-item]
    if data.get("NatGatewayId") is not None:
        out["nat_gateway_id"] = data["NatGatewayId"]
    else:
        out["nat_gateway_id"] = ""
    if data.get("ProxyName") is not None:
        out["proxy_name"] = data["ProxyName"]
    if data.get("ProxyArn") is not None:
        out["proxy_arn"] = data["ProxyArn"]
    if data.get("ListenerPropertiesToAdd") is not None:
        import capo_network_firewall.types.listener_properties_request

        out["listener_properties_to_add"] = (
            capo_network_firewall.types.listener_properties_request.deserialize_aws_json_1_0(
                data["ListenerPropertiesToAdd"]
            )
        )
    if data.get("ListenerPropertiesToRemove") is not None:
        import capo_network_firewall.types.listener_properties_request

        out["listener_properties_to_remove"] = (
            capo_network_firewall.types.listener_properties_request.deserialize_aws_json_1_0(
                data["ListenerPropertiesToRemove"]
            )
        )
    if data.get("TlsInterceptProperties") is not None:
        import capo_network_firewall.types.tls_intercept_properties_request

        out["tls_intercept_properties"] = (
            capo_network_firewall.types.tls_intercept_properties_request.deserialize_aws_json_1_0(
                data["TlsInterceptProperties"]
            )
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    return out
