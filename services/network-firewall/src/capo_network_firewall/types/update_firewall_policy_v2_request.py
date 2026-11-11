"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateFirewallPolicyV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.firewall_policy_v2
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.update_token


class UpdateFirewallPolicyV2Request(TypedDict, closed=True):
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request. </p> <p>To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    firewall_policy_v2_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Next Generation policy.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy_v2_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_policy_v2: (
        "capo_network_firewall.types.firewall_policy_v2.FirewallPolicyV2"
    )
    """<p>The updated rule groups and other settings that define the Next Generation policy.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the firewall policy.</p>"""
    dry_run: NotRequired["capo_network_firewall.types.boolean.Boolean"]
    """<p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains settings for encryption of your firewall policy resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateFirewallPolicyV2Request) -> dict:
    out: dict = {}
    out["UpdateToken"] = value["update_token"]
    if "firewall_policy_v2_arn" in value:
        out["FirewallPolicyV2Arn"] = value["firewall_policy_v2_arn"]
    if "firewall_policy_v2_name" in value:
        out["FirewallPolicyV2Name"] = value["firewall_policy_v2_name"]
    import capo_network_firewall.types.firewall_policy_v2

    out["FirewallPolicyV2"] = (
        capo_network_firewall.types.firewall_policy_v2.serialize_aws_json_1_0(
            value["firewall_policy_v2"]
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


def deserialize_aws_json_1_0(data: dict) -> UpdateFirewallPolicyV2Request:
    out: UpdateFirewallPolicyV2Request = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    if data.get("FirewallPolicyV2Arn") is not None:
        out["firewall_policy_v2_arn"] = data["FirewallPolicyV2Arn"]
    if data.get("FirewallPolicyV2Name") is not None:
        out["firewall_policy_v2_name"] = data["FirewallPolicyV2Name"]
    if data.get("FirewallPolicyV2") is not None:
        import capo_network_firewall.types.firewall_policy_v2

        out["firewall_policy_v2"] = (
            capo_network_firewall.types.firewall_policy_v2.deserialize_aws_json_1_0(
                data["FirewallPolicyV2"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateFirewallPolicyV2Request.firewall_policy_v2 required"
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
