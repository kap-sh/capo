"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxySettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_settings
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.update_token


class UpdateProxySettingsRequest(TypedDict, closed=True):
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    proxy_settings: NotRequired[
        "capo_network_firewall.types.proxy_settings.ProxySettings"
    ]
    """<p>The proxy settings to set on the firewall. These replace the current proxy settings. Specify at least one listener, and at most one HTTP listener and one HTTPS listener, on different ports. If the firewall uses your own <code>CertificateArn</code> and <code>DomainName</code>, specify the same values that you used to create the firewall.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxySettingsRequest) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    if "proxy_settings" in value:
        import capo_network_firewall.types.proxy_settings

        out["ProxySettings"] = (
            capo_network_firewall.types.proxy_settings.serialize_aws_json_1_0(
                value["proxy_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxySettingsRequest:
    out: UpdateProxySettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    if data.get("ProxySettings") is not None:
        import capo_network_firewall.types.proxy_settings

        out["proxy_settings"] = (
            capo_network_firewall.types.proxy_settings.deserialize_aws_json_1_0(
                data["ProxySettings"]
            )
        )
    return out
