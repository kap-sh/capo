"""Generated from Smithy shape ``com.amazonaws.fms#PolicyOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.network_acl_common_policy
    import capo_fms.types.network_firewall_policy
    import capo_fms.types.third_party_firewall_policy


class PolicyOption(TypedDict, closed=True):
    network_firewall_policy: NotRequired[
        "capo_fms.types.network_firewall_policy.NetworkFirewallPolicy"
    ]
    """<p>Defines the deployment model to use for the firewall policy.</p>"""
    third_party_firewall_policy: NotRequired[
        "capo_fms.types.third_party_firewall_policy.ThirdPartyFirewallPolicy"
    ]
    """<p>Defines the policy options for a third-party firewall policy.</p>"""
    network_acl_common_policy: NotRequired[
        "capo_fms.types.network_acl_common_policy.NetworkAclCommonPolicy"
    ]
    """<p>Defines a Firewall Manager network ACL policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyOption) -> dict:
    out: dict = {}
    if "network_firewall_policy" in value:
        import capo_fms.types.network_firewall_policy

        out["NetworkFirewallPolicy"] = (
            capo_fms.types.network_firewall_policy.serialize_aws_json_1_1(
                value["network_firewall_policy"]
            )
        )
    if "third_party_firewall_policy" in value:
        import capo_fms.types.third_party_firewall_policy

        out["ThirdPartyFirewallPolicy"] = (
            capo_fms.types.third_party_firewall_policy.serialize_aws_json_1_1(
                value["third_party_firewall_policy"]
            )
        )
    if "network_acl_common_policy" in value:
        import capo_fms.types.network_acl_common_policy

        out["NetworkAclCommonPolicy"] = (
            capo_fms.types.network_acl_common_policy.serialize_aws_json_1_1(
                value["network_acl_common_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyOption:
    out: PolicyOption = {}  # type: ignore[typeddict-item]
    if data.get("NetworkFirewallPolicy") is not None:
        import capo_fms.types.network_firewall_policy

        out["network_firewall_policy"] = (
            capo_fms.types.network_firewall_policy.deserialize_aws_json_1_1(
                data["NetworkFirewallPolicy"]
            )
        )
    if data.get("ThirdPartyFirewallPolicy") is not None:
        import capo_fms.types.third_party_firewall_policy

        out["third_party_firewall_policy"] = (
            capo_fms.types.third_party_firewall_policy.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallPolicy"]
            )
        )
    if data.get("NetworkAclCommonPolicy") is not None:
        import capo_fms.types.network_acl_common_policy

        out["network_acl_common_policy"] = (
            capo_fms.types.network_acl_common_policy.deserialize_aws_json_1_1(
                data["NetworkAclCommonPolicy"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyOption) -> dict:
    out: dict = {}
    if "network_firewall_policy" in value:
        import capo_fms.types.network_firewall_policy

        out["NetworkFirewallPolicy"] = (
            capo_fms.types.network_firewall_policy.serialize_cbor(
                value["network_firewall_policy"]
            )
        )
    if "third_party_firewall_policy" in value:
        import capo_fms.types.third_party_firewall_policy

        out["ThirdPartyFirewallPolicy"] = (
            capo_fms.types.third_party_firewall_policy.serialize_cbor(
                value["third_party_firewall_policy"]
            )
        )
    if "network_acl_common_policy" in value:
        import capo_fms.types.network_acl_common_policy

        out["NetworkAclCommonPolicy"] = (
            capo_fms.types.network_acl_common_policy.serialize_cbor(
                value["network_acl_common_policy"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PolicyOption:
    out: PolicyOption = {}  # type: ignore[typeddict-item]
    if data.get("NetworkFirewallPolicy") is not None:
        import capo_fms.types.network_firewall_policy

        out["network_firewall_policy"] = (
            capo_fms.types.network_firewall_policy.deserialize_cbor(
                data["NetworkFirewallPolicy"]
            )
        )
    if data.get("ThirdPartyFirewallPolicy") is not None:
        import capo_fms.types.third_party_firewall_policy

        out["third_party_firewall_policy"] = (
            capo_fms.types.third_party_firewall_policy.deserialize_cbor(
                data["ThirdPartyFirewallPolicy"]
            )
        )
    if data.get("NetworkAclCommonPolicy") is not None:
        import capo_fms.types.network_acl_common_policy

        out["network_acl_common_policy"] = (
            capo_fms.types.network_acl_common_policy.deserialize_cbor(
                data["NetworkAclCommonPolicy"]
            )
        )
    return out
