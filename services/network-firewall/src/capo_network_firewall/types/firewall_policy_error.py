"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policy_error_code
    import capo_network_firewall.types.firewall_policy_error_resource_id
    import capo_network_firewall.types.status_reason


class FirewallPolicyError(TypedDict, closed=True):
    code: (
        "capo_network_firewall.types.firewall_policy_error_code.FirewallPolicyErrorCode"
    )
    """<p>The error code identifies the type of error. Valid values are the following:</p> <ul> <li> <p> <code>DNS_FIREWALL_RULE_GROUP_UNAVAILABLE</code> – The Amazon Route 53 Resolver DNS Firewall rule group that resolved IP validation references is unavailable, for example, because it was deleted or is no longer accessible from your account. Update the rule group ID or remove the resolved IP validation configuration.</p> </li> <li> <p> <code>ROUTE53_RESOLVED_IP_VALIDATION_MISSING</code> – An associated stateful rule group uses the <code>aws_route_53_resolved_domain</code> keyword, but the policy doesn't have resolved IP validation configured. The affected rules are inactive until you add resolved IP validation to the policy or remove the keyword rules.</p> </li> </ul>"""
    message: "capo_network_firewall.types.status_reason.StatusReason"
    """<p>A description of the error and how to resolve it.</p>"""
    resource_id: NotRequired[
        "capo_network_firewall.types.firewall_policy_error_resource_id.FirewallPolicyErrorResourceId"
    ]
    """<p>The ID of the resource that the error relates to, when applicable. For example, for <code>DNS_FIREWALL_RULE_GROUP_UNAVAILABLE</code> this is the Amazon Route 53 Resolver DNS Firewall rule group ID.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyError) -> dict:
    out: dict = {}
    import capo_network_firewall.types.firewall_policy_error_code

    out["Code"] = (
        capo_network_firewall.types.firewall_policy_error_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallPolicyError:
    out: FirewallPolicyError = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_network_firewall.types.firewall_policy_error_code

        out["code"] = (
            capo_network_firewall.types.firewall_policy_error_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_network_firewall.types.firewall_policy_error_code.FirewallPolicyErrorCode",
            "",
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    return out
