"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.firewall_policy_errors
    import capo_network_firewall.types.last_update_time
    import capo_network_firewall.types.number_of_associations
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_id
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.resource_status
    import capo_network_firewall.types.resource_status_message
    import capo_network_firewall.types.rule_capacity
    import capo_network_firewall.types.tag_list


class FirewallPolicyV2Response(TypedDict, closed=True):
    firewall_policy_v2_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.</p>"""
    firewall_policy_v2_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Next Generation policy.</p>"""
    firewall_policy_v2_id: "capo_network_firewall.types.resource_id.ResourceId"
    """<p>The unique identifier of the Next Generation policy. Network Firewall assigns this identifier when you create the policy.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the Next Generation policy.</p>"""
    firewall_policy_v2_status: NotRequired[
        "capo_network_firewall.types.resource_status.ResourceStatus"
    ]
    """<p>The current status of the Next Generation policy. A policy must be in the <code>ACTIVE</code> state before you can use it in a firewall.</p>"""
    status_message: NotRequired[
        "capo_network_firewall.types.resource_status_message.ResourceStatusMessage"
    ]
    """<p>Additional information about the current status of the Next Generation policy.</p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key-value tag pairs that are associated with the Next Generation policy.</p>"""
    consumed_firewall_rule_capacity: NotRequired[
        "capo_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of firewall engine rule capacity units that the policy's firewall section currently consumes.</p>"""
    consumed_ips_rule_capacity: NotRequired[
        "capo_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of IPS engine rule capacity units that the policy's IPS section currently consumes.</p>"""
    consumed_ips_domain_capacity: NotRequired[
        "capo_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of IPS domain list capacity units that the policy's IPS section currently consumes.</p>"""
    number_of_associations: NotRequired[
        "capo_network_firewall.types.number_of_associations.NumberOfAssociations"
    ]
    """<p>The number of firewalls that are associated with the Next Generation policy.</p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your Next Generation policy.</p>"""
    errors: NotRequired[
        "capo_network_firewall.types.firewall_policy_errors.FirewallPolicyErrors"
    ]
    """<p>Any configuration errors that apply to the Next Generation policy. Network Firewall detects these errors asynchronously, after you create or update the policy, so an error can appear after the request that caused it has already succeeded. Each entry describes the problem and how to resolve it, and Network Firewall clears it automatically after you resolve the problem.</p>"""
    last_modified_time: NotRequired[
        "capo_network_firewall.types.last_update_time.LastUpdateTime"
    ]
    """<p>The last time that the Next Generation policy was changed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyV2Response) -> dict:
    out: dict = {}
    out["FirewallPolicyV2Name"] = value["firewall_policy_v2_name"]
    out["FirewallPolicyV2Arn"] = value["firewall_policy_v2_arn"]
    out["FirewallPolicyV2Id"] = value["firewall_policy_v2_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "firewall_policy_v2_status" in value:
        import capo_network_firewall.types.resource_status

        out["FirewallPolicyV2Status"] = (
            capo_network_firewall.types.resource_status.serialize_aws_json_1_0(
                value["firewall_policy_v2_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "consumed_firewall_rule_capacity" in value:
        out["ConsumedFirewallRuleCapacity"] = value["consumed_firewall_rule_capacity"]
    if "consumed_ips_rule_capacity" in value:
        out["ConsumedIpsRuleCapacity"] = value["consumed_ips_rule_capacity"]
    if "consumed_ips_domain_capacity" in value:
        out["ConsumedIpsDomainCapacity"] = value["consumed_ips_domain_capacity"]
    if "number_of_associations" in value:
        out["NumberOfAssociations"] = value["number_of_associations"]
    if "encryption_configuration" in value:
        import capo_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "errors" in value:
        import capo_network_firewall.types.firewall_policy_errors

        out["Errors"] = (
            capo_network_firewall.types.firewall_policy_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    if "last_modified_time" in value:
        import capo_network_firewall.types.last_update_time

        out["LastModifiedTime"] = (
            capo_network_firewall.types.last_update_time.serialize_aws_json_1_0(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallPolicyV2Response:
    out: FirewallPolicyV2Response = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyV2Name") is not None:
        out["firewall_policy_v2_name"] = data["FirewallPolicyV2Name"]
    else:
        out["firewall_policy_v2_name"] = ""
    if data.get("FirewallPolicyV2Arn") is not None:
        out["firewall_policy_v2_arn"] = data["FirewallPolicyV2Arn"]
    else:
        out["firewall_policy_v2_arn"] = ""
    if data.get("FirewallPolicyV2Id") is not None:
        out["firewall_policy_v2_id"] = data["FirewallPolicyV2Id"]
    else:
        out["firewall_policy_v2_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FirewallPolicyV2Status") is not None:
        import capo_network_firewall.types.resource_status

        out["firewall_policy_v2_status"] = (
            capo_network_firewall.types.resource_status.deserialize_aws_json_1_0(
                data["FirewallPolicyV2Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("ConsumedFirewallRuleCapacity") is not None:
        out["consumed_firewall_rule_capacity"] = data["ConsumedFirewallRuleCapacity"]
    if data.get("ConsumedIpsRuleCapacity") is not None:
        out["consumed_ips_rule_capacity"] = data["ConsumedIpsRuleCapacity"]
    if data.get("ConsumedIpsDomainCapacity") is not None:
        out["consumed_ips_domain_capacity"] = data["ConsumedIpsDomainCapacity"]
    if data.get("NumberOfAssociations") is not None:
        out["number_of_associations"] = data["NumberOfAssociations"]
    if data.get("EncryptionConfiguration") is not None:
        import capo_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("Errors") is not None:
        import capo_network_firewall.types.firewall_policy_errors

        out["errors"] = (
            capo_network_firewall.types.firewall_policy_errors.deserialize_aws_json_1_0(
                data["Errors"]
            )
        )
    if data.get("LastModifiedTime") is not None:
        import capo_network_firewall.types.last_update_time

        out["last_modified_time"] = (
            capo_network_firewall.types.last_update_time.deserialize_aws_json_1_0(
                data["LastModifiedTime"]
            )
        )
    return out
