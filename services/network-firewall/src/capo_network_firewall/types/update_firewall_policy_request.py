"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateFirewallPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.firewall_policy
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.update_token


class UpdateFirewallPolicyRequest(TypedDict, closed=True):
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request. </p> <p>To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    firewall_policy_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the firewall policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy: "capo_network_firewall.types.firewall_policy.FirewallPolicy"
    """<p>The updated firewall policy to use for the firewall. You can't add or remove a <a>TLSInspectionConfiguration</a> after you create a firewall policy. However, you can replace an existing TLS inspection configuration with another <code>TLSInspectionConfiguration</code>.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the firewall policy.</p>"""
    dry_run: NotRequired["capo_network_firewall.types.boolean.Boolean"]
    """<p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains settings for encryption of your firewall policy resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateFirewallPolicyRequest) -> dict:
    out: dict = {}
    out["UpdateToken"] = value["update_token"]
    if "firewall_policy_arn" in value:
        out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    if "firewall_policy_name" in value:
        out["FirewallPolicyName"] = value["firewall_policy_name"]
    import capo_network_firewall.types.firewall_policy

    out["FirewallPolicy"] = (
        capo_network_firewall.types.firewall_policy.serialize_aws_json_1_0(
            value["firewall_policy"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "encryption_configuration" in value:
        import capo_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateFirewallPolicyRequest:
    out: UpdateFirewallPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        raise DeserializationError("UpdateFirewallPolicyRequest.update_token required")
    if data.get("FirewallPolicyArn") is not None:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    if data.get("FirewallPolicyName") is not None:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    if data.get("FirewallPolicy") is not None:
        import capo_network_firewall.types.firewall_policy

        out["firewall_policy"] = (
            capo_network_firewall.types.firewall_policy.deserialize_aws_json_1_0(
                data["FirewallPolicy"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateFirewallPolicyRequest.firewall_policy required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    return out
