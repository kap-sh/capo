"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.aws_region_name
    import capo_codepipeline.types.command_list
    import capo_codepipeline.types.input_artifact_list
    import capo_codepipeline.types.role_arn
    import capo_codepipeline.types.rule_configuration_map
    import capo_codepipeline.types.rule_name
    import capo_codepipeline.types.rule_timeout
    import capo_codepipeline.types.rule_type_id


class RuleDeclaration(TypedDict, closed=True):
    name: "capo_codepipeline.types.rule_name.RuleName"
    """<p>The name of the rule that is created for the condition, such as <code>VariableCheck</code>.</p>"""
    rule_type_id: "capo_codepipeline.types.rule_type_id.RuleTypeId"
    """<p>The ID for the rule type, which is made up of the combined values for category, owner, provider, and version.</p>"""
    configuration: NotRequired[
        "capo_codepipeline.types.rule_configuration_map.RuleConfigurationMap"
    ]
    """<p>The action configuration fields for the rule.</p>"""
    commands: NotRequired["capo_codepipeline.types.command_list.CommandList"]
    """<p>The shell commands to run with your commands rule in CodePipeline. All commands are supported except multi-line formats. While CodeBuild logs and permissions are used, you do not need to create any resources in CodeBuild.</p> <note> <p>Using compute time for this action will incur separate charges in CodeBuild.</p> </note>"""
    input_artifacts: NotRequired[
        "capo_codepipeline.types.input_artifact_list.InputArtifactList"
    ]
    """<p>The input artifacts fields for the rule, such as specifying an input file for the rule.</p>"""
    role_arn: NotRequired["capo_codepipeline.types.role_arn.RoleArn"]
    """<p>The pipeline role ARN associated with the rule.</p>"""
    region: NotRequired["capo_codepipeline.types.aws_region_name.AWSRegionName"]
    """<p>The Region for the condition associated with the rule.</p>"""
    timeout_in_minutes: NotRequired["capo_codepipeline.types.rule_timeout.RuleTimeout"]
    """<p>The action timeout for the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
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
    if "commands" in value:
        import capo_codepipeline.types.command_list

        out["commands"] = capo_codepipeline.types.command_list.serialize_aws_json_1_1(
            value["commands"]
        )
    if "input_artifacts" in value:
        import capo_codepipeline.types.input_artifact_list

        out["inputArtifacts"] = (
            capo_codepipeline.types.input_artifact_list.serialize_aws_json_1_1(
                value["input_artifacts"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "region" in value:
        out["region"] = value["region"]
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleDeclaration:
    out: RuleDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("ruleTypeId") is not None:
        import capo_codepipeline.types.rule_type_id

        out["rule_type_id"] = (
            capo_codepipeline.types.rule_type_id.deserialize_aws_json_1_1(
                data["ruleTypeId"]
            )
        )
    else:
        raise DeserializationError("RuleDeclaration.rule_type_id required")
    if data.get("configuration") is not None:
        import capo_codepipeline.types.rule_configuration_map

        out["configuration"] = (
            capo_codepipeline.types.rule_configuration_map.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("commands") is not None:
        import capo_codepipeline.types.command_list

        out["commands"] = capo_codepipeline.types.command_list.deserialize_aws_json_1_1(
            data["commands"]
        )
    if data.get("inputArtifacts") is not None:
        import capo_codepipeline.types.input_artifact_list

        out["input_artifacts"] = (
            capo_codepipeline.types.input_artifact_list.deserialize_aws_json_1_1(
                data["inputArtifacts"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("timeoutInMinutes") is not None:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    return out
