"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_execution
    import capo_codepipeline.types.rule_state_list


class ConditionState(TypedDict, closed=True):
    latest_execution: NotRequired[
        "capo_codepipeline.types.condition_execution.ConditionExecution"
    ]
    """<p>The state of the latest run of the rule.</p>"""
    rule_states: NotRequired["capo_codepipeline.types.rule_state_list.RuleStateList"]
    """<p>The state of the rules for the condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionState) -> dict:
    out: dict = {}
    if "latest_execution" in value:
        import capo_codepipeline.types.condition_execution

        out["latestExecution"] = (
            capo_codepipeline.types.condition_execution.serialize_aws_json_1_1(
                value["latest_execution"]
            )
        )
    if "rule_states" in value:
        import capo_codepipeline.types.rule_state_list

        out["ruleStates"] = (
            capo_codepipeline.types.rule_state_list.serialize_aws_json_1_1(
                value["rule_states"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConditionState:
    out: ConditionState = {}  # type: ignore[typeddict-item]
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.condition_execution

        out["latest_execution"] = (
            capo_codepipeline.types.condition_execution.deserialize_aws_json_1_1(
                data["latestExecution"]
            )
        )
    if data.get("ruleStates") is not None:
        import capo_codepipeline.types.rule_state_list

        out["rule_states"] = (
            capo_codepipeline.types.rule_state_list.deserialize_aws_json_1_1(
                data["ruleStates"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConditionState) -> dict:
    out: dict = {}
    if "latest_execution" in value:
        import capo_codepipeline.types.condition_execution

        out["latestExecution"] = (
            capo_codepipeline.types.condition_execution.serialize_cbor(
                value["latest_execution"]
            )
        )
    if "rule_states" in value:
        import capo_codepipeline.types.rule_state_list

        out["ruleStates"] = capo_codepipeline.types.rule_state_list.serialize_cbor(
            value["rule_states"]
        )
    return out


def deserialize_cbor(data: dict) -> ConditionState:
    out: ConditionState = {}  # type: ignore[typeddict-item]
    if data.get("latestExecution") is not None:
        import capo_codepipeline.types.condition_execution

        out["latest_execution"] = (
            capo_codepipeline.types.condition_execution.deserialize_cbor(
                data["latestExecution"]
            )
        )
    if data.get("ruleStates") is not None:
        import capo_codepipeline.types.rule_state_list

        out["rule_states"] = capo_codepipeline.types.rule_state_list.deserialize_cbor(
            data["ruleStates"]
        )
    return out
