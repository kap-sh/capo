"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_configuration_map
    import capo_codepipeline.types.action_namespace
    import capo_codepipeline.types.action_type_id
    import capo_codepipeline.types.artifact_detail_list
    import capo_codepipeline.types.aws_region_name
    import capo_codepipeline.types.resolved_action_configuration_map
    import capo_codepipeline.types.role_arn


class ActionExecutionInput(TypedDict, closed=True):
    action_type_id: NotRequired["capo_codepipeline.types.action_type_id.ActionTypeId"]
    configuration: NotRequired[
        "capo_codepipeline.types.action_configuration_map.ActionConfigurationMap"
    ]
    """<p>Configuration data for an action execution.</p>"""
    resolved_configuration: NotRequired[
        "capo_codepipeline.types.resolved_action_configuration_map.ResolvedActionConfigurationMap"
    ]
    """<p>Configuration data for an action execution with all variable references replaced with their real values for the execution.</p>"""
    role_arn: NotRequired["capo_codepipeline.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM service role that performs the declared action. This is assumed through the roleArn for the pipeline. </p>"""
    region: NotRequired["capo_codepipeline.types.aws_region_name.AWSRegionName"]
    """<p>The Amazon Web Services Region for the action, such as us-east-1.</p>"""
    input_artifacts: NotRequired[
        "capo_codepipeline.types.artifact_detail_list.ArtifactDetailList"
    ]
    """<p>Details of input artifacts of the action that correspond to the action execution.</p>"""
    namespace: NotRequired["capo_codepipeline.types.action_namespace.ActionNamespace"]
    """<p>The variable namespace associated with the action. All variables produced as output by this action fall under this namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionInput) -> dict:
    out: dict = {}
    if "action_type_id" in value:
        import capo_codepipeline.types.action_type_id

        out["actionTypeId"] = (
            capo_codepipeline.types.action_type_id.serialize_aws_json_1_1(
                value["action_type_id"]
            )
        )
    if "configuration" in value:
        import capo_codepipeline.types.action_configuration_map

        out["configuration"] = (
            capo_codepipeline.types.action_configuration_map.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "resolved_configuration" in value:
        import capo_codepipeline.types.resolved_action_configuration_map

        out["resolvedConfiguration"] = (
            capo_codepipeline.types.resolved_action_configuration_map.serialize_aws_json_1_1(
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
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecutionInput:
    out: ActionExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("actionTypeId") is not None:
        import capo_codepipeline.types.action_type_id

        out["action_type_id"] = (
            capo_codepipeline.types.action_type_id.deserialize_aws_json_1_1(
                data["actionTypeId"]
            )
        )
    if data.get("configuration") is not None:
        import capo_codepipeline.types.action_configuration_map

        out["configuration"] = (
            capo_codepipeline.types.action_configuration_map.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("resolvedConfiguration") is not None:
        import capo_codepipeline.types.resolved_action_configuration_map

        out["resolved_configuration"] = (
            capo_codepipeline.types.resolved_action_configuration_map.deserialize_aws_json_1_1(
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
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionExecutionInput) -> dict:
    out: dict = {}
    if "action_type_id" in value:
        import capo_codepipeline.types.action_type_id

        out["actionTypeId"] = capo_codepipeline.types.action_type_id.serialize_cbor(
            value["action_type_id"]
        )
    if "configuration" in value:
        import capo_codepipeline.types.action_configuration_map

        out["configuration"] = (
            capo_codepipeline.types.action_configuration_map.serialize_cbor(
                value["configuration"]
            )
        )
    if "resolved_configuration" in value:
        import capo_codepipeline.types.resolved_action_configuration_map

        out["resolvedConfiguration"] = (
            capo_codepipeline.types.resolved_action_configuration_map.serialize_cbor(
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
            capo_codepipeline.types.artifact_detail_list.serialize_cbor(
                value["input_artifacts"]
            )
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_cbor(data: dict) -> ActionExecutionInput:
    out: ActionExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("actionTypeId") is not None:
        import capo_codepipeline.types.action_type_id

        out["action_type_id"] = capo_codepipeline.types.action_type_id.deserialize_cbor(
            data["actionTypeId"]
        )
    if data.get("configuration") is not None:
        import capo_codepipeline.types.action_configuration_map

        out["configuration"] = (
            capo_codepipeline.types.action_configuration_map.deserialize_cbor(
                data["configuration"]
            )
        )
    if data.get("resolvedConfiguration") is not None:
        import capo_codepipeline.types.resolved_action_configuration_map

        out["resolved_configuration"] = (
            capo_codepipeline.types.resolved_action_configuration_map.deserialize_cbor(
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
            capo_codepipeline.types.artifact_detail_list.deserialize_cbor(
                data["inputArtifacts"]
            )
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    return out
