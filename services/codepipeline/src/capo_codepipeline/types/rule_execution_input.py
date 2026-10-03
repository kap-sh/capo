"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_detail_list
    import capo_codepipeline.types.aws_region_name
    import capo_codepipeline.types.resolved_rule_configuration_map
    import capo_codepipeline.types.role_arn
    import capo_codepipeline.types.rule_configuration_map
    import capo_codepipeline.types.rule_type_id


class RuleExecutionInput(TypedDict, closed=True):
    rule_type_id: NotRequired["capo_codepipeline.types.rule_type_id.RuleTypeId"]
    """<p>The ID for the rule type, which is made up of the combined values for category, owner, provider, and version. For more information about conditions, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html">Stage conditions</a>. For more information about rules, see the <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/rule-reference.html">CodePipeline rule reference</a>.</p>"""
    configuration: NotRequired[
        "capo_codepipeline.types.rule_configuration_map.RuleConfigurationMap"
    ]
    """<p>Configuration data for a rule execution, such as the resolved values for that run.</p>"""
    resolved_configuration: NotRequired[
        "capo_codepipeline.types.resolved_rule_configuration_map.ResolvedRuleConfigurationMap"
    ]
    """<p>Configuration data for a rule execution with all variable references replaced with their real values for the execution.</p>"""
    role_arn: NotRequired["capo_codepipeline.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM service role that performs the declared rule. This is assumed through the roleArn for the pipeline.</p>"""
    region: NotRequired["capo_codepipeline.types.aws_region_name.AWSRegionName"]
    """<p>The Amazon Web Services Region for the rule, such as us-east-1.</p>"""
    input_artifacts: NotRequired[
        "capo_codepipeline.types.artifact_detail_list.ArtifactDetailList"
    ]
    """<p>Details of input artifacts of the rule that correspond to the rule execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionInput) -> dict:
    out: dict = {}
    if "rule_type_id" in value:
        import capo_codepipeline.types.rule_type_id

        out["ruleTypeId"] = capo_codepipeline.types.rule_type_id.serialize_aws_json_1_1(
            value["rule_type_id"]
        )
    if "configuration" in value:
        import capo_codepipeline.types.rule_configuration_map

        out["configuration"] = (
            capo_codepipeline.types.rule_configuration_map.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "resolved_configuration" in value:
        import capo_codepipeline.types.resolved_rule_configuration_map

        out["resolvedConfiguration"] = (
            capo_codepipeline.types.resolved_rule_configuration_map.serialize_aws_json_1_1(
                value["resolved_configuration"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "region" in value:
        out["region"] = value["region"]
    if "input_artifacts" in value:
        import capo_codepipeline.types.artifact_detail_list

        out["inputArtifacts"] = (
            capo_codepipeline.types.artifact_detail_list.serialize_aws_json_1_1(
                value["input_artifacts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleExecutionInput:
    out: RuleExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("ruleTypeId") is not None:
        import capo_codepipeline.types.rule_type_id

        out["rule_type_id"] = (
            capo_codepipeline.types.rule_type_id.deserialize_aws_json_1_1(
                data["ruleTypeId"]
            )
        )
    if data.get("configuration") is not None:
        import capo_codepipeline.types.rule_configuration_map

        out["configuration"] = (
            capo_codepipeline.types.rule_configuration_map.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("resolvedConfiguration") is not None:
        import capo_codepipeline.types.resolved_rule_configuration_map

        out["resolved_configuration"] = (
            capo_codepipeline.types.resolved_rule_configuration_map.deserialize_aws_json_1_1(
                data["resolvedConfiguration"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("inputArtifacts") is not None:
        import capo_codepipeline.types.artifact_detail_list

        out["input_artifacts"] = (
            capo_codepipeline.types.artifact_detail_list.deserialize_aws_json_1_1(
                data["inputArtifacts"]
            )
        )
    return out
