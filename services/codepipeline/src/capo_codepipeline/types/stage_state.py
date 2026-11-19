"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_state_list
    import capo_codepipeline.types.retry_stage_metadata
    import capo_codepipeline.types.stage_condition_state
    import capo_codepipeline.types.stage_execution
    import capo_codepipeline.types.stage_execution_list
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.transition_state


class StageState(TypedDict, closed=True):
    stage_name: NotRequired["capo_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage.</p>"""
    inbound_execution: NotRequired[
        "capo_codepipeline.types.stage_execution.StageExecution"
    ]
    inbound_executions: NotRequired[
        "capo_codepipeline.types.stage_execution_list.StageExecutionList"
    ]
    """<p>The inbound executions for a stage.</p>"""
    inbound_transition_state: NotRequired[
        "capo_codepipeline.types.transition_state.TransitionState"
    ]
    """<p>The state of the inbound transition, which is either enabled or disabled.</p>"""
    action_states: NotRequired[
        "capo_codepipeline.types.action_state_list.ActionStateList"
    ]
    """<p>The state of the stage.</p>"""
    latest_execution: NotRequired[
        "capo_codepipeline.types.stage_execution.StageExecution"
    ]
    """<p>Information about the latest execution in the stage, including its ID and status.</p>"""
    before_entry_condition_state: NotRequired[
        "capo_codepipeline.types.stage_condition_state.StageConditionState"
    ]
    """<p>The state of the entry conditions for a stage.</p>"""
    on_success_condition_state: NotRequired[
        "capo_codepipeline.types.stage_condition_state.StageConditionState"
    ]
    """<p>The state of the success conditions for a stage.</p>"""
    on_failure_condition_state: NotRequired[
        "capo_codepipeline.types.stage_condition_state.StageConditionState"
    ]
    """<p>The state of the failure conditions for a stage.</p>"""
    retry_stage_metadata: NotRequired[
        "capo_codepipeline.types.retry_stage_metadata.RetryStageMetadata"
    ]
    """<p>he details of a specific automatic retry on stage failure, including the attempt number and trigger.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageState) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "inbound_execution" in value:
        import capo_codepipeline.types.stage_execution

        out["inboundExecution"] = (
            capo_codepipeline.types.stage_execution.serialize_aws_json_1_1(
                value["inbound_execution"]
            )
        )
    if "inbound_executions" in value:
        import capo_codepipeline.types.stage_execution_list

        out["inboundExecutions"] = (
            capo_codepipeline.types.stage_execution_list.serialize_aws_json_1_1(
                value["inbound_executions"]
            )
        )
    if "inbound_transition_state" in value:
        import capo_codepipeline.types.transition_state

        out["inboundTransitionState"] = (
            capo_codepipeline.types.transition_state.serialize_aws_json_1_1(
                value["inbound_transition_state"]
            )
        )
    if "action_states" in value:
        import capo_codepipeline.types.action_state_list

        out["actionStates"] = (
            capo_codepipeline.types.action_state_list.serialize_aws_json_1_1(
                value["action_states"]
            )
        )
    if "latest_execution" in value:
        import capo_codepipeline.types.stage_execution

        out["latestExecution"] = (
            capo_codepipeline.types.stage_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "before_entry_condition_state" in value:
        import capo_codepipeline.types.stage_condition_state

        out["beforeEntryConditionState"] = (
            capo_codepipeline.types.stage_condition_state.serialize_aws_json_1_1(
                value["before_entry_condition_state"]
            )
        )
    if "on_success_condition_state" in value:
        import capo_codepipeline.types.stage_condition_state

        out["onSuccessConditionState"] = (
            capo_codepipeline.types.stage_condition_state.serialize_aws_json_1_1(
                value["on_success_condition_state"]
            )
        )
    if "on_failure_condition_state" in value:
        import capo_codepipeline.types.stage_condition_state

        out["onFailureConditionState"] = (
            capo_codepipeline.types.stage_condition_state.serialize_aws_json_1_1(
                value["on_failure_condition_state"]
            )
        )
    if "retry_stage_metadata" in value:
        import capo_codepipeline.types.retry_stage_metadata

        out["retryStageMetadata"] = (
            capo_codepipeline.types.retry_stage_metadata.serialize_aws_json_1_1(
                value["retry_stage_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StageState:
    out: StageState = {}  # type: ignore[typeddict-item]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("inboundExecution") is not None:
        import capo_codepipeline.types.stage_execution

        out["inbound_execution"] = (
            capo_codepipeline.types.stage_execution.deserialize_aws_json_1_1(
                data["inboundExecution"]
            )
        )
    if data.get("inboundExecutions") is not None:
        import capo_codepipeline.types.stage_execution_list

        out["inbound_executions"] = (
            capo_codepipeline.types.stage_execution_list.deserialize_aws_json_1_1(
                data["inboundExecutions"]
            )
        )
    if data.get("inboundTransitionState") is not None:
        import capo_codepipeline.types.transition_state

        out["inbound_transition_state"] = (
            capo_codepipeline.types.transition_state.deserialize_aws_json_1_1(
                data["inboundTransitionState"]
            )
        )
    if data.get("actionStates") is not None:
        import capo_codepipeline.types.action_state_list

        out["action_states"] = (
            capo_codepipeline.types.action_state_list.deserialize_aws_json_1_1(
                data["actionStates"]
            )
        )
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.stage_execution

        out["latest_execution"] = (
            capo_codepipeline.types.stage_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if data.get("beforeEntryConditionState") is not None:
        import capo_codepipeline.types.stage_condition_state

        out["before_entry_condition_state"] = (
            capo_codepipeline.types.stage_condition_state.deserialize_aws_json_1_1(
                data["beforeEntryConditionState"]
            )
        )
    if data.get("onSuccessConditionState") is not None:
        import capo_codepipeline.types.stage_condition_state

        out["on_success_condition_state"] = (
            capo_codepipeline.types.stage_condition_state.deserialize_aws_json_1_1(
                data["onSuccessConditionState"]
            )
        )
    if data.get("onFailureConditionState") is not None:
        import capo_codepipeline.types.stage_condition_state

        out["on_failure_condition_state"] = (
            capo_codepipeline.types.stage_condition_state.deserialize_aws_json_1_1(
                data["onFailureConditionState"]
            )
        )
    if data.get("retryStageMetadata") is not None:
        import capo_codepipeline.types.retry_stage_metadata

        out["retry_stage_metadata"] = (
            capo_codepipeline.types.retry_stage_metadata.deserialize_aws_json_1_1(
                data["retryStageMetadata"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageState) -> dict:
    out: dict = {}
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "inbound_execution" in value:
        import capo_codepipeline.types.stage_execution

        out["inboundExecution"] = (
            capo_codepipeline.types.stage_execution.serialize_cbor(
                value["inbound_execution"]
            )
        )
    if "inbound_executions" in value:
        import capo_codepipeline.types.stage_execution_list

        out["inboundExecutions"] = (
            capo_codepipeline.types.stage_execution_list.serialize_cbor(
                value["inbound_executions"]
            )
        )
    if "inbound_transition_state" in value:
        import capo_codepipeline.types.transition_state

        out["inboundTransitionState"] = (
            capo_codepipeline.types.transition_state.serialize_cbor(
                value["inbound_transition_state"]
            )
        )
    if "action_states" in value:
        import capo_codepipeline.types.action_state_list

        out["actionStates"] = capo_codepipeline.types.action_state_list.serialize_cbor(
            value["action_states"]
        )
    if "latest_execution" in value:
        import capo_codepipeline.types.stage_execution

        out["latestExecution"] = capo_codepipeline.types.stage_execution.serialize_cbor(
            value["latest_execution"]
        )
    if "before_entry_condition_state" in value:
        import capo_codepipeline.types.stage_condition_state

        out["beforeEntryConditionState"] = (
            capo_codepipeline.types.stage_condition_state.serialize_cbor(
                value["before_entry_condition_state"]
            )
        )
    if "on_success_condition_state" in value:
        import capo_codepipeline.types.stage_condition_state

        out["onSuccessConditionState"] = (
            capo_codepipeline.types.stage_condition_state.serialize_cbor(
                value["on_success_condition_state"]
            )
        )
    if "on_failure_condition_state" in value:
        import capo_codepipeline.types.stage_condition_state

        out["onFailureConditionState"] = (
            capo_codepipeline.types.stage_condition_state.serialize_cbor(
                value["on_failure_condition_state"]
            )
        )
    if "retry_stage_metadata" in value:
        import capo_codepipeline.types.retry_stage_metadata

        out["retryStageMetadata"] = (
            capo_codepipeline.types.retry_stage_metadata.serialize_cbor(
                value["retry_stage_metadata"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StageState:
    out: StageState = {}  # type: ignore[typeddict-item]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("inboundExecution") is not None:
        import capo_codepipeline.types.stage_execution

        out["inbound_execution"] = (
            capo_codepipeline.types.stage_execution.deserialize_cbor(
                data["inboundExecution"]
            )
        )
    if data.get("inboundExecutions") is not None:
        import capo_codepipeline.types.stage_execution_list

        out["inbound_executions"] = (
            capo_codepipeline.types.stage_execution_list.deserialize_cbor(
                data["inboundExecutions"]
            )
        )
    if data.get("inboundTransitionState") is not None:
        import capo_codepipeline.types.transition_state

        out["inbound_transition_state"] = (
            capo_codepipeline.types.transition_state.deserialize_cbor(
                data["inboundTransitionState"]
            )
        )
    if data.get("actionStates") is not None:
        import capo_codepipeline.types.action_state_list

        out["action_states"] = (
            capo_codepipeline.types.action_state_list.deserialize_cbor(
                data["actionStates"]
            )
        )
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.stage_execution

        out["latest_execution"] = (
            capo_codepipeline.types.stage_execution.deserialize_cbor(
                data["latestExecution"]
            )
        )
    if data.get("beforeEntryConditionState") is not None:
        import capo_codepipeline.types.stage_condition_state

        out["before_entry_condition_state"] = (
            capo_codepipeline.types.stage_condition_state.deserialize_cbor(
                data["beforeEntryConditionState"]
            )
        )
    if data.get("onSuccessConditionState") is not None:
        import capo_codepipeline.types.stage_condition_state

        out["on_success_condition_state"] = (
            capo_codepipeline.types.stage_condition_state.deserialize_cbor(
                data["onSuccessConditionState"]
            )
        )
    if data.get("onFailureConditionState") is not None:
        import capo_codepipeline.types.stage_condition_state

        out["on_failure_condition_state"] = (
            capo_codepipeline.types.stage_condition_state.deserialize_cbor(
                data["onFailureConditionState"]
            )
        )
    if data.get("retryStageMetadata") is not None:
        import capo_codepipeline.types.retry_stage_metadata

        out["retry_stage_metadata"] = (
            capo_codepipeline.types.retry_stage_metadata.deserialize_cbor(
                data["retryStageMetadata"]
            )
        )
    return out
