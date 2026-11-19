"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_result
    import capo_codepipeline.types.artifact_detail_list
    import capo_codepipeline.types.output_variables_map


class ActionExecutionOutput(TypedDict, closed=True):
    output_artifacts: NotRequired[
        "capo_codepipeline.types.artifact_detail_list.ArtifactDetailList"
    ]
    """<p>Details of output artifacts of the action that correspond to the action execution.</p>"""
    execution_result: NotRequired[
        "capo_codepipeline.types.action_execution_result.ActionExecutionResult"
    ]
    """<p>Execution result information listed in the output details for an action execution.</p>"""
    output_variables: NotRequired[
        "capo_codepipeline.types.output_variables_map.OutputVariablesMap"
    ]
    """<p>The outputVariables field shows the key-value pairs that were output as part of that execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionOutput) -> dict:
    out: dict = {}
    if "output_artifacts" in value:
        import capo_codepipeline.types.artifact_detail_list

        out["outputArtifacts"] = (
            capo_codepipeline.types.artifact_detail_list.serialize_aws_json_1_1(
                value["output_artifacts"]
            )
        )
    if "execution_result" in value:
        import capo_codepipeline.types.action_execution_result

        out["executionResult"] = (
            capo_codepipeline.types.action_execution_result.serialize_aws_json_1_1(
                value["execution_result"]
            )
        )
    if "output_variables" in value:
        import capo_codepipeline.types.output_variables_map

        out["outputVariables"] = (
            capo_codepipeline.types.output_variables_map.serialize_aws_json_1_1(
                value["output_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecutionOutput:
    out: ActionExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("outputArtifacts") is not None:
        import capo_codepipeline.types.artifact_detail_list

        out["output_artifacts"] = (
            capo_codepipeline.types.artifact_detail_list.deserialize_aws_json_1_1(
                data["outputArtifacts"]
            )
        )
    if data.get("executionResult") is not None:
        import capo_codepipeline.types.action_execution_result

        out["execution_result"] = (
            capo_codepipeline.types.action_execution_result.deserialize_aws_json_1_1(
                data["executionResult"]
            )
        )
    if data.get("outputVariables") is not None:
        import capo_codepipeline.types.output_variables_map

        out["output_variables"] = (
            capo_codepipeline.types.output_variables_map.deserialize_aws_json_1_1(
                data["outputVariables"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionExecutionOutput) -> dict:
    out: dict = {}
    if "output_artifacts" in value:
        import capo_codepipeline.types.artifact_detail_list

        out["outputArtifacts"] = (
            capo_codepipeline.types.artifact_detail_list.serialize_cbor(
                value["output_artifacts"]
            )
        )
    if "execution_result" in value:
        import capo_codepipeline.types.action_execution_result

        out["executionResult"] = (
            capo_codepipeline.types.action_execution_result.serialize_cbor(
                value["execution_result"]
            )
        )
    if "output_variables" in value:
        import capo_codepipeline.types.output_variables_map

        out["outputVariables"] = (
            capo_codepipeline.types.output_variables_map.serialize_cbor(
                value["output_variables"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ActionExecutionOutput:
    out: ActionExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("outputArtifacts") is not None:
        import capo_codepipeline.types.artifact_detail_list

        out["output_artifacts"] = (
            capo_codepipeline.types.artifact_detail_list.deserialize_cbor(
                data["outputArtifacts"]
            )
        )
    if data.get("executionResult") is not None:
        import capo_codepipeline.types.action_execution_result

        out["execution_result"] = (
            capo_codepipeline.types.action_execution_result.deserialize_cbor(
                data["executionResult"]
            )
        )
    if data.get("outputVariables") is not None:
        import capo_codepipeline.types.output_variables_map

        out["output_variables"] = (
            capo_codepipeline.types.output_variables_map.deserialize_cbor(
                data["outputVariables"]
            )
        )
    return out
