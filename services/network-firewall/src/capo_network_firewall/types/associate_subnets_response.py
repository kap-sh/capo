"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AssociateSubnetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.subnet_mappings
    import capo_network_firewall.types.update_token


class AssociateSubnetsResponse(TypedDict, closed=True):
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p>"""
    subnet_mappings: NotRequired[
        "capo_network_firewall.types.subnet_mappings.SubnetMappings"
    ]
    """<p>The IDs of the subnets that are associated with the firewall. </p>"""
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateSubnetsResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "subnet_mappings" in value:
        import capo_network_firewall.types.subnet_mappings

        out["SubnetMappings"] = (
            capo_network_firewall.types.subnet_mappings.serialize_aws_json_1_0(
                value["subnet_mappings"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateSubnetsResponse:
    out: AssociateSubnetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("SubnetMappings") is not None:
        import capo_network_firewall.types.subnet_mappings

        out["subnet_mappings"] = (
            capo_network_firewall.types.subnet_mappings.deserialize_aws_json_1_0(
                data["SubnetMappings"]
            )
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateSubnetsResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "subnet_mappings" in value:
        import capo_network_firewall.types.subnet_mappings

        out["SubnetMappings"] = (
            capo_network_firewall.types.subnet_mappings.serialize_cbor(
                value["subnet_mappings"]
            )
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_cbor(data: dict) -> AssociateSubnetsResponse:
    out: AssociateSubnetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("SubnetMappings") is not None:
        import capo_network_firewall.types.subnet_mappings

        out["subnet_mappings"] = (
            capo_network_firewall.types.subnet_mappings.deserialize_cbor(
                data["SubnetMappings"]
            )
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    return out
