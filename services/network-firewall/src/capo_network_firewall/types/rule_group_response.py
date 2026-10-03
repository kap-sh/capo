"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.analysis_result_list
    import capo_network_firewall.types.description
    import capo_network_firewall.types.encryption_configuration
    import capo_network_firewall.types.last_update_time
    import capo_network_firewall.types.number_of_associations
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_id
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.resource_status
    import capo_network_firewall.types.rule_capacity
    import capo_network_firewall.types.rule_group_type
    import capo_network_firewall.types.source_metadata
    import capo_network_firewall.types.summary_configuration
    import capo_network_firewall.types.tag_list


class RuleGroupResponse(TypedDict, closed=True):
    rule_group_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the rule group.</p> <note> <p>If this response is for a create request that had <code>DryRun</code> set to <code>TRUE</code>, then this ARN is a placeholder that isn't attached to a valid resource.</p> </note>"""
    rule_group_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the rule group. You can't change the name of a rule group after you create it.</p>"""
    rule_group_id: "capo_network_firewall.types.resource_id.ResourceId"
    """<p>The unique identifier for the rule group. </p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the rule group. </p>"""
    type: NotRequired["capo_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules. </p>"""
    capacity: NotRequired["capo_network_firewall.types.rule_capacity.RuleCapacity"]
    """<p>The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group. </p> <p>You can retrieve the capacity that would be required for a rule group before you create the rule group by calling <a>CreateRuleGroup</a> with <code>DryRun</code> set to <code>TRUE</code>. </p>"""
    rule_group_status: NotRequired[
        "capo_network_firewall.types.resource_status.ResourceStatus"
    ]
    """<p>Detailed information about the current status of a rule group. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    consumed_capacity: NotRequired[
        "capo_network_firewall.types.rule_capacity.RuleCapacity"
    ]
    """<p>The number of capacity units currently consumed by the rule group rules. </p>"""
    number_of_associations: NotRequired[
        "capo_network_firewall.types.number_of_associations.NumberOfAssociations"
    ]
    """<p>The number of firewall policies that use this rule group.</p>"""
    encryption_configuration: NotRequired[
        "capo_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains the Amazon Web Services KMS encryption configuration settings for your rule group.</p>"""
    source_metadata: NotRequired[
        "capo_network_firewall.types.source_metadata.SourceMetadata"
    ]
    """<p>A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to track the version updates made to the originating rule group.</p>"""
    sns_topic: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service SNS topic that's used to record changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/welcome.html">Amazon Simple Notification Service Developer Guide.</a>.</p>"""
    last_modified_time: NotRequired[
        "capo_network_firewall.types.last_update_time.LastUpdateTime"
    ]
    """<p>The last time that the rule group was changed.</p>"""
    analysis_results: NotRequired[
        "capo_network_firewall.types.analysis_result_list.AnalysisResultList"
    ]
    """<p>The list of analysis results for <code>AnalyzeRuleGroup</code>. If you set <code>AnalyzeRuleGroup</code> to <code>TRUE</code> in <a>CreateRuleGroup</a>, <a>UpdateRuleGroup</a>, or <a>DescribeRuleGroup</a>, Network Firewall analyzes the rule group and identifies the rules that might adversely effect your firewall's functionality. For example, if Network Firewall detects a rule that's routing traffic asymmetrically, which impacts the service's ability to properly process traffic, the service includes the rule in the list of analysis results.</p>"""
    summary_configuration: NotRequired[
        "capo_network_firewall.types.summary_configuration.SummaryConfiguration"
    ]
    """<p>A complex type containing the currently selected rule option fields that will be displayed for rule summarization returned by <a>DescribeRuleGroupSummary</a>.</p> <ul> <li> <p>The <code>RuleOptions</code> specified in <a>SummaryConfiguration</a> </p> </li> <li> <p>Rule metadata organization preferences</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroupResponse) -> dict:
    out: dict = {}
    out["RuleGroupArn"] = value["rule_group_arn"]
    out["RuleGroupName"] = value["rule_group_name"]
    out["RuleGroupId"] = value["rule_group_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_network_firewall.types.rule_group_type

        out["Type"] = (
            capo_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "capacity" in value:
        out["Capacity"] = value["capacity"]
    if "rule_group_status" in value:
        import capo_network_firewall.types.resource_status

        out["RuleGroupStatus"] = (
            capo_network_firewall.types.resource_status.serialize_aws_json_1_0(
                value["rule_group_status"]
            )
        )
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "consumed_capacity" in value:
        out["ConsumedCapacity"] = value["consumed_capacity"]
    if "number_of_associations" in value:
        out["NumberOfAssociations"] = value["number_of_associations"]
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
    if "sns_topic" in value:
        out["SnsTopic"] = value["sns_topic"]
    if "last_modified_time" in value:
        import capo_network_firewall.types.last_update_time

        out["LastModifiedTime"] = (
            capo_network_firewall.types.last_update_time.serialize_aws_json_1_0(
                value["last_modified_time"]
            )
        )
    if "analysis_results" in value:
        import capo_network_firewall.types.analysis_result_list

        out["AnalysisResults"] = (
            capo_network_firewall.types.analysis_result_list.serialize_aws_json_1_0(
                value["analysis_results"]
            )
        )
    if "summary_configuration" in value:
        import capo_network_firewall.types.summary_configuration

        out["SummaryConfiguration"] = (
            capo_network_firewall.types.summary_configuration.serialize_aws_json_1_0(
                value["summary_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleGroupResponse:
    out: RuleGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupArn") is not None:
        out["rule_group_arn"] = data["RuleGroupArn"]
    else:
        raise DeserializationError("RuleGroupResponse.rule_group_arn required")
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    else:
        raise DeserializationError("RuleGroupResponse.rule_group_name required")
    if data.get("RuleGroupId") is not None:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        raise DeserializationError("RuleGroupResponse.rule_group_id required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.rule_group_type

        out["type"] = (
            capo_network_firewall.types.rule_group_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    if data.get("Capacity") is not None:
        out["capacity"] = data["Capacity"]
    if data.get("RuleGroupStatus") is not None:
        import capo_network_firewall.types.resource_status

        out["rule_group_status"] = (
            capo_network_firewall.types.resource_status.deserialize_aws_json_1_0(
                data["RuleGroupStatus"]
            )
        )
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("ConsumedCapacity") is not None:
        out["consumed_capacity"] = data["ConsumedCapacity"]
    if data.get("NumberOfAssociations") is not None:
        out["number_of_associations"] = data["NumberOfAssociations"]
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
    if data.get("SnsTopic") is not None:
        out["sns_topic"] = data["SnsTopic"]
    if data.get("LastModifiedTime") is not None:
        import capo_network_firewall.types.last_update_time

        out["last_modified_time"] = (
            capo_network_firewall.types.last_update_time.deserialize_aws_json_1_0(
                data["LastModifiedTime"]
            )
        )
    if data.get("AnalysisResults") is not None:
        import capo_network_firewall.types.analysis_result_list

        out["analysis_results"] = (
            capo_network_firewall.types.analysis_result_list.deserialize_aws_json_1_0(
                data["AnalysisResults"]
            )
        )
    if data.get("SummaryConfiguration") is not None:
        import capo_network_firewall.types.summary_configuration

        out["summary_configuration"] = (
            capo_network_firewall.types.summary_configuration.deserialize_aws_json_1_0(
                data["SummaryConfiguration"]
            )
        )
    return out
