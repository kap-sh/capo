"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageConditionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_state_list
    import capo_codepipeline.types.stage_conditions_execution


class StageConditionState(TypedDict, closed=True):
    latest_execution: NotRequired[
        "capo_codepipeline.types.stage_conditions_execution.StageConditionsExecution"
    ]
    """<p>Represents information about the latest run of a condition for a stage.</p>"""
    condition_states: NotRequired[
        "capo_codepipeline.types.condition_state_list.ConditionStateList"
    ]
    """<p>The states of the conditions for a run of a condition for a stage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageConditionState) -> dict:
    out: dict = {}
    if "latest_execution" in value:
        import capo_codepipeline.types.stage_conditions_execution

        out["latestExecution"] = (
            capo_codepipeline.types.stage_conditions_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "condition_states" in value:
        import capo_codepipeline.types.condition_state_list

        out["conditionStates"] = (
            capo_codepipeline.types.condition_state_list.serialize_aws_json_1_1(
                value["condition_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StageConditionState:
    out: StageConditionState = {}  # type: ignore[typeddict-item]
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.stage_conditions_execution

        out["latest_execution"] = (
            capo_codepipeline.types.stage_conditions_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if data.get("conditionStates") is not None:
        import capo_codepipeline.types.condition_state_list

        out["condition_states"] = (
            capo_codepipeline.types.condition_state_list.deserialize_aws_json_1_1(
                data["conditionStates"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageConditionState) -> dict:
    out: dict = {}
    if "latest_execution" in value:
        import capo_codepipeline.types.stage_conditions_execution

        out["latestExecution"] = (
            capo_codepipeline.types.stage_conditions_execution.serialize_cbor(
                value["latest_execution"]
            )
        )
    if "condition_states" in value:
        import capo_codepipeline.types.condition_state_list

        out["conditionStates"] = (
            capo_codepipeline.types.condition_state_list.serialize_cbor(
                value["condition_states"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StageConditionState:
    out: StageConditionState = {}  # type: ignore[typeddict-item]
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.stage_conditions_execution

        out["latest_execution"] = (
            capo_codepipeline.types.stage_conditions_execution.deserialize_cbor(
                data["latestExecution"]
            )
        )
    if data.get("conditionStates") is not None:
        import capo_codepipeline.types.condition_state_list

        out["condition_states"] = (
            capo_codepipeline.types.condition_state_list.deserialize_cbor(
                data["conditionStates"]
            )
        )
    return out
