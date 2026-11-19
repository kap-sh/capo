"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFirewallResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall
    import capo_network_firewall.types.firewall_status
    import capo_network_firewall.types.update_token


class DescribeFirewallResponse(TypedDict, closed=True):
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    firewall: NotRequired["capo_network_firewall.types.firewall.Firewall"]
    """<p>The configuration settings for the firewall. These settings include the firewall policy and the subnets in your VPC to use for the firewall endpoints. </p>"""
    firewall_status: NotRequired[
        "capo_network_firewall.types.firewall_status.FirewallStatus"
    ]
    """<p>Detailed information about the current status of a <a>Firewall</a>. You can retrieve this for a firewall by calling <a>DescribeFirewall</a> and providing the firewall name and ARN.</p> <p>The firewall status indicates a combined status. It indicates whether all subnets are up-to-date with the latest firewall configurations, which is based on the sync states config values, and also whether all subnets have their endpoints fully enabled, based on their sync states attachment values. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFirewallResponse) -> dict:
    out: dict = {}
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    if "firewall" in value:
        import capo_network_firewall.types.firewall

        out["Firewall"] = capo_network_firewall.types.firewall.serialize_aws_json_1_0(
            value["firewall"]
        )
    if "firewall_status" in value:
        import capo_network_firewall.types.firewall_status

        out["FirewallStatus"] = (
            capo_network_firewall.types.firewall_status.serialize_aws_json_1_0(
                value["firewall_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFirewallResponse:
    out: DescribeFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    if data.get("Firewall") is not None:
        import capo_network_firewall.types.firewall

        out["firewall"] = capo_network_firewall.types.firewall.deserialize_aws_json_1_0(
            data["Firewall"]
        )
    if data.get("FirewallStatus") is not None:
        import capo_network_firewall.types.firewall_status

        out["firewall_status"] = (
            capo_network_firewall.types.firewall_status.deserialize_aws_json_1_0(
                data["FirewallStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFirewallResponse) -> dict:
    out: dict = {}
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    if "firewall" in value:
        import capo_network_firewall.types.firewall

        out["Firewall"] = capo_network_firewall.types.firewall.serialize_cbor(
            value["firewall"]
        )
    if "firewall_status" in value:
        import capo_network_firewall.types.firewall_status

        out["FirewallStatus"] = (
            capo_network_firewall.types.firewall_status.serialize_cbor(
                value["firewall_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeFirewallResponse:
    out: DescribeFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    if data.get("Firewall") is not None:
        import capo_network_firewall.types.firewall

        out["firewall"] = capo_network_firewall.types.firewall.deserialize_cbor(
            data["Firewall"]
        )
    if data.get("FirewallStatus") is not None:
        import capo_network_firewall.types.firewall_status

        out["firewall_status"] = (
            capo_network_firewall.types.firewall_status.deserialize_cbor(
                data["FirewallStatus"]
            )
        )
    return out
