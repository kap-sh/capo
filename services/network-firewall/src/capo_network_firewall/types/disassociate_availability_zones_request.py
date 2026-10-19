"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DisassociateAvailabilityZonesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone_mappings
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.update_token


class DisassociateAvailabilityZonesRequest(TypedDict, closed=True):
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>An optional token that you can use for optimistic locking. Network Firewall returns a token to your requests that access the firewall. The token marks the state of the firewall resource at the time of the request. </p> <p>To make an unconditional change to the firewall, omit the token in your update request. Without the token, Network Firewall performs your updates regardless of whether the firewall has changed since you last retrieved it.</p> <p>To make a conditional change to the firewall, provide the token in your update request. Network Firewall uses the token to ensure that the firewall hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall again to get a current copy of it with a new token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    availability_zone_mappings: "capo_network_firewall.types.availability_zone_mappings.AvailabilityZoneMappings"
    """<p>Required. The Availability Zones to remove from the firewall's configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateAvailabilityZonesRequest) -> dict:
    out: dict = {}
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    import capo_network_firewall.types.availability_zone_mappings

    out["AvailabilityZoneMappings"] = (
        capo_network_firewall.types.availability_zone_mappings.serialize_aws_json_1_0(
            value["availability_zone_mappings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateAvailabilityZonesRequest:
    out: DisassociateAvailabilityZonesRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("AvailabilityZoneMappings") is not None:
        import capo_network_firewall.types.availability_zone_mappings

        out["availability_zone_mappings"] = (
            capo_network_firewall.types.availability_zone_mappings.deserialize_aws_json_1_0(
                data["AvailabilityZoneMappings"]
            )
        )
    else:
        out["availability_zone_mappings"] = []
    return out
