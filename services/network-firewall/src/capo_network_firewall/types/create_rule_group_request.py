"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.rule_capacity
    import capo_network_firewall.types.rule_group
    import capo_network_firewall.types.rule_group_type
    import capo_network_firewall.types.rules_string
    import capo_network_firewall.types.source_metadata
    import capo_network_firewall.types.summary_configuration
    import capo_network_firewall.types.tag_list


class CreateRuleGroupRequest(TypedDict, closed=True):
    rule_group_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p>"""
    rule_group: NotRequired["capo_network_firewall.types.rule_group.RuleGroup"]
    """<p>An object that defines the rule group rules. </p> <note> <p>You must provide either this rule group setting or a <code>Rules</code> setting, but not both. </p> </note>"""
    rules: NotRequired["capo_network_firewall.types.rules_string.RulesString"]
    """<p>A string containing stateful rule group rules specifications in Suricata flat format, with one rule per line. Use this to import your existing Suricata compatible rule groups. </p> <note> <p>You must provide either this rules setting or a populated <code>RuleGroup</code> setting, but not both. </p> </note> <p>You can provide your rule group specification in Suricata flat format through this setting when you create or update your rule group. The call response returns a <a>RuleGroup</a> object that Network Firewall has populated from your string. </p>"""
    type: "capo_network_firewall.types.rule_group_type.RuleGroupType"
    """<p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the rule group. </p>"""
    capacity: "capo_network_firewall.types.rule_capacity.RuleCapacity"
    """<p>The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group. </p> <p>You can retrieve the capacity that would be required for a rule group before you create the rule group by calling <a>CreateRuleGroup</a> with <code>DryRun</code> set to <code>TRUE</code>. </p> <note> <p>You can't change or exceed this capacity when you update the rule group, so leave room for your rule group to grow. </p> </note> <p> <b>Capacity for a stateless rule group</b> </p> <p>For a stateless rule group, the capacity required is the sum of the capacity requirements of the individual rules that you expect to have in the rule group. </p> <p>To calculate the capacity requirement of a single rule, multiply the capacity requirement values of each of the rule's match settings:</p> <ul> <li> <p>A match setting with no criteria specified has a value of 1. </p> </li> <li> <p>A match setting with <code>Any</code> specified has a value of 1. </p> </li> <li> <p>All other match settings have a value equal to the number of elements provided in the setting. For example, a protocol setting ["UDP"] and a source setting ["10.0.0.0/24"] each have a value of 1. A protocol setting ["UDP","TCP"] has a value of 2. A source setting ["10.0.0.0/24","10.0.0.1/24","10.0.0.2/24"] has a value of 3. </p> </li> </ul> <p>A rule with no criteria specified in any of its match settings has a capacity requirement of 1. A rule with protocol setting ["UDP","TCP"], source setting ["10.0.0.0/24","10.0.0.1/24","10.0.0.2/24"], and a single specification or no specification for each of the other match settings has a capacity requirement of 6. </p> <p> <b>Capacity for a stateful rule group</b> </p> <p>For a stateful rule group, the minimum capacity required is the number of individual rules that you expect to have in the rule group. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    dry_run: "capo_network_firewall.types.boolean.Boolean"
    """<p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains settings for encryption of your rule group resources.</p>"""
    source_metadata: NotRequired[
        "capo_network_firewall.types.source_metadata.SourceMetadata"
    ]
    """<p>A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to keep track of updates made to the originating rule group.</p>"""
    analyze_rule_group: "capo_network_firewall.types.boolean.Boolean"
    """<p>Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to <code>TRUE</code>, Network Firewall runs the analysis and then creates the rule group for you. To run the stateless rule group analyzer without creating the rule group, set <code>DryRun</code> to <code>TRUE</code>.</p>"""
    summary_configuration: NotRequired[
        "capo_network_firewall.types.summary_configuration.SummaryConfiguration"
    ]
    """<p>An object that contains a <code>RuleOptions</code> array of strings. You use <code>RuleOptions</code> to determine which of the following <a>RuleSummary</a> values are returned in response to <code>DescribeRuleGroupSummary</code>.</p> <ul> <li> <p> <code>Metadata</code> - returns</p> </li> <li> <p> <code>Msg</code> </p> </li> <li> <p> <code>SID</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRuleGroupRequest) -> dict:
    out: dict = {}
    out["RuleGroupName"] = value["rule_group_name"]
    if "rule_group" in value:
        import capo_network_firewall.types.rule_group

        out["RuleGroup"] = (
            capo_network_firewall.types.rule_group.serialize_aws_json_1_0(
                value["rule_group"]
            )
        )
    if "rules" in value:
        out["Rules"] = value["rules"]
    import capo_network_firewall.types.rule_group_type

    out["Type"] = capo_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
        value["type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["Capacity"] = value["capacity"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    out["DryRun"] = value.get("dry_run", False)
    if "encryption_configuration" in value:
        import capo_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "source_metadata" in value:
        import capo_network_firewall.types.source_metadata

        out["SourceMetadata"] = (
            capo_network_firewall.types.source_metadata.serialize_aws_json_1_0(
                value["source_metadata"]
            )
        )
    out["AnalyzeRuleGroup"] = value.get("analyze_rule_group", False)
    if "summary_configuration" in value:
        import capo_network_firewall.types.summary_configuration

        out["SummaryConfiguration"] = (
            capo_network_firewall.types.summary_configuration.serialize_aws_json_1_0(
                value["summary_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRuleGroupRequest:
    out: CreateRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.rule_group_name required")
    if data.get("RuleGroup") is not None:
        import capo_network_firewall.types.rule_group

        out["rule_group"] = (
            capo_network_firewall.types.rule_group.deserialize_aws_json_1_0(
                data["RuleGroup"]
            )
        )
    if data.get("Rules") is not None:
        out["rules"] = data["Rules"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.rule_group_type

        out["type"] = (
            capo_network_firewall.types.rule_group_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CreateRuleGroupRequest.type required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.capacity required")
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if data.get("EncryptionConfiguration") is not None:
        import capo_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("SourceMetadata") is not None:
        import capo_network_firewall.types.source_metadata

        out["source_metadata"] = (
            capo_network_firewall.types.source_metadata.deserialize_aws_json_1_0(
                data["SourceMetadata"]
            )
        )
    if data.get("AnalyzeRuleGroup") is not None:
        out["analyze_rule_group"] = data["AnalyzeRuleGroup"]
    else:
        out["analyze_rule_group"] = False
    if data.get("SummaryConfiguration") is not None:
        import capo_network_firewall.types.summary_configuration

        out["summary_configuration"] = (
            capo_network_firewall.types.summary_configuration.deserialize_aws_json_1_0(
                data["SummaryConfiguration"]
            )
        )
    return out
