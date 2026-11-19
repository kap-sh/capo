"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListRuleExecutionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.rule_execution_detail_list


class ListRuleExecutionsOutput(TypedDict, closed=True):
    rule_execution_details: NotRequired[
        "capo_codepipeline.types.rule_execution_detail_list.RuleExecutionDetailList"
    ]
    """<p>Details about the output for listing rule executions.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>A token that can be used in the next <code>ListRuleExecutions</code> call. To view all items in the list, continue to call this operation with each subsequent token until no more nextToken values are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleExecutionsOutput) -> dict:
    out: dict = {}
    if "rule_execution_details" in value:
        import capo_codepipeline.types.rule_execution_detail_list

        out["ruleExecutionDetails"] = (
            capo_codepipeline.types.rule_execution_detail_list.serialize_aws_json_1_1(
                value["rule_execution_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleExecutionsOutput:
    out: ListRuleExecutionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ruleExecutionDetails") is not None:
        import capo_codepipeline.types.rule_execution_detail_list

        out["rule_execution_details"] = (
            capo_codepipeline.types.rule_execution_detail_list.deserialize_aws_json_1_1(
                data["ruleExecutionDetails"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRuleExecutionsOutput) -> dict:
    out: dict = {}
    if "rule_execution_details" in value:
        import capo_codepipeline.types.rule_execution_detail_list

        out["ruleExecutionDetails"] = (
            capo_codepipeline.types.rule_execution_detail_list.serialize_cbor(
                value["rule_execution_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRuleExecutionsOutput:
    out: ListRuleExecutionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ruleExecutionDetails") is not None:
        import capo_codepipeline.types.rule_execution_detail_list

        out["rule_execution_details"] = (
            capo_codepipeline.types.rule_execution_detail_list.deserialize_cbor(
                data["ruleExecutionDetails"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
