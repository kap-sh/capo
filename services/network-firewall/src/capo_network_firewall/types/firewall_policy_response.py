"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyResponse``."""

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


class FirewallPolicyResponse(TypedDict, closed=True):
    firewall_policy_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p>"""
    firewall_policy_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall policy.</p> <note> <p>If this response is for a create request that had <code>DryRun</code> set to <code>TRUE</code>, then this ARN is a placeholder that isn't attached to a valid resource.</p> </note>"""
    firewall_policy_id: "capo_network_firewall.types.resource_id.ResourceId"
    """<p>The unique identifier for the firewall policy. </p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the firewall policy.</p>"""
    firewall_policy_status: NotRequired[
        "capo_network_firewall.types.resource_status.ResourceStatus"
    ]
    """<p>The current status of the firewall policy. You can retrieve this for a firewall policy by calling <a>DescribeFirewallPolicy</a> and providing the firewall policy's name or ARN.</p>"""
    status_message: NotRequired[
        "capo_network_firewall.types.resource_status_message.ResourceStatusMessage"
    ]
    """<p>Additional detail about the firewall policy's current status, when applicable. For example, while an Amazon Route 53 Resolver DNS Firewall rule group change is in progress, the status is <code>UPDATING</code> and this message is "A DNS Firewall rule group change is in progress."</p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    consumed_stateless_rule_capacity: NotRequired[
        "capo_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of capacity units currently consumed by the policy's stateless rules.</p>"""
    consumed_stateful_rule_capacity: NotRequired[
        "capo_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of capacity units currently consumed by the policy's stateful rules.</p>"""
    consumed_stateful_domain_capacity: NotRequired[
        "capo_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The total number of domain name specifications across all domain list rule groups in the firewall policy that use the <code>stateful-domain-rulegroup</code> resource type.</p>"""
    number_of_associations: NotRequired[
        "capo_network_firewall.types.number_of_associations.NumberOfAssociations"
    ]
    """<p>The number of firewalls that are associated with this firewall policy.</p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your firewall policy.</p>"""
    errors: NotRequired[
        "capo_network_firewall.types.firewall_policy_errors.FirewallPolicyErrors"
    ]
    """<p>Any configuration errors that apply to the firewall policy. Network Firewall detects these errors asynchronously, after you create or update the policy, so an error can appear after the request that caused it has already succeeded. Each entry describes the problem and how to resolve it, and Network Firewall clears it automatically after you resolve the problem.</p>"""
    last_modified_time: NotRequired[
        "capo_network_firewall.types.last_update_time.LastUpdateTime"
    ]
    """<p>The last time that the firewall policy was changed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyResponse) -> dict:
    out: dict = {}
    out["FirewallPolicyName"] = value["firewall_policy_name"]
    out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    out["FirewallPolicyId"] = value["firewall_policy_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "firewall_policy_status" in value:
        import capo_network_firewall.types.resource_status

        out["FirewallPolicyStatus"] = (
            capo_network_firewall.types.resource_status.serialize_aws_json_1_0(
                value["firewall_policy_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "consumed_stateless_rule_capacity" in value:
        out["ConsumedStatelessRuleCapacity"] = value["consumed_stateless_rule_capacity"]
    if "consumed_stateful_rule_capacity" in value:
        out["ConsumedStatefulRuleCapacity"] = value["consumed_stateful_rule_capacity"]
    if "consumed_stateful_domain_capacity" in value:
        out["ConsumedStatefulDomainCapacity"] = value[
            "consumed_stateful_domain_capacity"
        ]
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


def deserialize_aws_json_1_0(data: dict) -> FirewallPolicyResponse:
    out: FirewallPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallPolicyName") is not None:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    else:
        out["firewall_policy_name"] = ""
    if data.get("FirewallPolicyArn") is not None:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    else:
        out["firewall_policy_arn"] = ""
    if data.get("FirewallPolicyId") is not None:
        out["firewall_policy_id"] = data["FirewallPolicyId"]
    else:
        out["firewall_policy_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FirewallPolicyStatus") is not None:
        import capo_network_firewall.types.resource_status

        out["firewall_policy_status"] = (
            capo_network_firewall.types.resource_status.deserialize_aws_json_1_0(
                data["FirewallPolicyStatus"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("ConsumedStatelessRuleCapacity") is not None:
        out["consumed_stateless_rule_capacity"] = data["ConsumedStatelessRuleCapacity"]
    if data.get("ConsumedStatefulRuleCapacity") is not None:
        out["consumed_stateful_rule_capacity"] = data["ConsumedStatefulRuleCapacity"]
    if data.get("ConsumedStatefulDomainCapacity") is not None:
        out["consumed_stateful_domain_capacity"] = data[
            "ConsumedStatefulDomainCapacity"
        ]
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
