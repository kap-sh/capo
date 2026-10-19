"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.boolean
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.rule_group
    import capo_network_firewall.types.rule_group_type
    import capo_network_firewall.types.rules_string
    import capo_network_firewall.types.source_metadata
    import capo_network_firewall.types.summary_configuration
    import capo_network_firewall.types.update_token


class UpdateRuleGroupRequest(TypedDict, closed=True):
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request. </p> <p>To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    rule_group_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group: NotRequired["capo_network_firewall.types.rule_group.RuleGroup"]
    """<p>An object that defines the rule group rules. </p> <note> <p>You must provide either this rule group setting or a <code>Rules</code> setting, but not both. </p> </note>"""
    rules: NotRequired["capo_network_firewall.types.rules_string.RulesString"]
    """<p>A string containing stateful rule group rules specifications in Suricata flat format, with one rule per line. Use this to import your existing Suricata compatible rule groups. </p> <note> <p>You must provide either this rules setting or a populated <code>RuleGroup</code> setting, but not both. </p> </note> <p>You can provide your rule group specification in Suricata flat format through this setting when you create or update your rule group. The call response returns a <a>RuleGroup</a> object that Network Firewall has populated from your string. </p>"""
    type: NotRequired["capo_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p> <note> <p>This setting is required for requests that do not include the <code>RuleGroupARN</code>.</p> </note>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the rule group. </p>"""
    dry_run: NotRequired["capo_network_firewall.types.boolean.Boolean"]
    """<p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains settings for encryption of your rule group resources.</p>"""
    source_metadata: NotRequired[
        "capo_network_firewall.types.source_metadata.SourceMetadata"
    ]
    """<p>A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to keep track of updates made to the originating rule group.</p>"""
    analyze_rule_group: NotRequired["capo_network_firewall.types.boolean.Boolean"]
    """<p>Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to <code>TRUE</code>, Network Firewall runs the analysis and then updates the rule group for you. To run the stateless rule group analyzer without updating the rule group, set <code>DryRun</code> to <code>TRUE</code>. </p>"""
    summary_configuration: NotRequired[
        "capo_network_firewall.types.summary_configuration.SummaryConfiguration"
    ]
    """<p>Updates the selected summary configuration for a rule group.</p> <p>Changes affect subsequent responses from <a>DescribeRuleGroupSummary</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRuleGroupRequest) -> dict:
    out: dict = {}
    out["UpdateToken"] = value["update_token"]
    if "rule_group_arn" in value:
        out["RuleGroupArn"] = value["rule_group_arn"]
    if "rule_group_name" in value:
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
    if "type" in value:
        import capo_network_firewall.types.rule_group_type

        out["Type"] = (
            capo_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
                value["type"]
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
    if "source_metadata" in value:
        import capo_network_firewall.types.source_metadata

        out["SourceMetadata"] = (
            capo_network_firewall.types.source_metadata.serialize_aws_json_1_0(
                value["source_metadata"]
            )
        )
    if "analyze_rule_group" in value:
        out["AnalyzeRuleGroup"] = value["analyze_rule_group"]
    if "summary_configuration" in value:
        import capo_network_firewall.types.summary_configuration

        out["SummaryConfiguration"] = (
            capo_network_firewall.types.summary_configuration.serialize_aws_json_1_0(
                value["summary_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRuleGroupRequest:
    out: UpdateRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    if data.get("RuleGroupArn") is not None:
        out["rule_group_arn"] = data["RuleGroupArn"]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
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
    if data.get("SourceMetadata") is not None:
        import capo_network_firewall.types.source_metadata

        out["source_metadata"] = (
            capo_network_firewall.types.source_metadata.deserialize_aws_json_1_0(
                data["SourceMetadata"]
            )
        )
    if data.get("AnalyzeRuleGroup") is not None:
        out["analyze_rule_group"] = data["AnalyzeRuleGroup"]
    if data.get("SummaryConfiguration") is not None:
        import capo_network_firewall.types.summary_configuration

        out["summary_configuration"] = (
            capo_network_firewall.types.summary_configuration.deserialize_aws_json_1_0(
                data["SummaryConfiguration"]
            )
        )
    return out
