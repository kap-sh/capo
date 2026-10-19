"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateFirewallPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.firewall_policy
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.tag_list


class CreateFirewallPolicyRequest(TypedDict, closed=True):
    firewall_policy_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p>"""
    firewall_policy: "capo_network_firewall.types.firewall_policy.FirewallPolicy"
    """<p>The rule groups and policy actions to use in the firewall policy.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the firewall policy.</p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    dry_run: NotRequired["capo_network_firewall.types.boolean.Boolean"]
    """<p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains settings for encryption of your firewall policy resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFirewallPolicyRequest) -> dict:
    out: dict = {}
    out["FirewallPolicyName"] = value["firewall_policy_name"]
    import capo_network_firewall.types.firewall_policy

    out["FirewallPolicy"] = (
        capo_network_firewall.types.firewall_policy.serialize_aws_json_1_0(
            value["firewall_policy"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
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


def deserialize_aws_json_1_0(data: dict) -> CreateFirewallPolicyRequest:
    out: CreateFirewallPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyName") is not None:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    else:
        out["firewall_policy_name"] = ""
    if data.get("FirewallPolicy") is not None:
        import capo_network_firewall.types.firewall_policy

        out["firewall_policy"] = (
            capo_network_firewall.types.firewall_policy.deserialize_aws_json_1_0(
                data["FirewallPolicy"]
            )
        )
    else:
        raise DeserializationError(
            "CreateFirewallPolicyRequest.firewall_policy required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
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
