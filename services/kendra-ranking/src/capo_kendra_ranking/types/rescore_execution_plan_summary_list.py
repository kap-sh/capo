"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreExecutionPlanSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra_ranking.types.rescore_execution_plan_summary

RescoreExecutionPlanSummaryList: TypeAlias = list[
    "capo_kendra_ranking.types.rescore_execution_plan_summary.RescoreExecutionPlanSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreExecutionPlanSummaryList) -> list:
    import capo_kendra_ranking.types.rescore_execution_plan_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra_ranking.types.rescore_execution_plan_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RescoreExecutionPlanSummaryList:
    import capo_kendra_ranking.types.rescore_execution_plan_summary

    out: RescoreExecutionPlanSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kendra_ranking.types.rescore_execution_plan_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RescoreExecutionPlanSummaryList) -> list:
    import capo_kendra_ranking.types.rescore_execution_plan_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra_ranking.types.rescore_execution_plan_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> RescoreExecutionPlanSummaryList:
    import capo_kendra_ranking.types.rescore_execution_plan_summary

    out: RescoreExecutionPlanSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kendra_ranking.types.rescore_execution_plan_summary.deserialize_cbor(
                item
            )
        )
    return out
