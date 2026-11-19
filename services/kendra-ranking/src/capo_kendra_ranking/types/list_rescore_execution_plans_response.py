"""Generated from Smithy shape ``com.amazonaws.kendraranking#ListRescoreExecutionPlansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.next_token
    import capo_kendra_ranking.types.rescore_execution_plan_summary_list


class ListRescoreExecutionPlansResponse(TypedDict, closed=True):
    summary_items: NotRequired[
        "capo_kendra_ranking.types.rescore_execution_plan_summary_list.RescoreExecutionPlanSummaryList"
    ]
    """<p>An array of summary information for one or more rescore execution plans.</p>"""
    next_token: NotRequired["capo_kendra_ranking.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra Intelligent Ranking returns a pagination token in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRescoreExecutionPlansResponse) -> dict:
    out: dict = {}
    if "summary_items" in value:
        import capo_kendra_ranking.types.rescore_execution_plan_summary_list

        out["SummaryItems"] = (
            capo_kendra_ranking.types.rescore_execution_plan_summary_list.serialize_aws_json_1_0(
                value["summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRescoreExecutionPlansResponse:
    out: ListRescoreExecutionPlansResponse = {}  # type: ignore[typeddict-item]
    if data.get("SummaryItems") is not None:
        import capo_kendra_ranking.types.rescore_execution_plan_summary_list

        out["summary_items"] = (
            capo_kendra_ranking.types.rescore_execution_plan_summary_list.deserialize_aws_json_1_0(
                data["SummaryItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRescoreExecutionPlansResponse) -> dict:
    out: dict = {}
    if "summary_items" in value:
        import capo_kendra_ranking.types.rescore_execution_plan_summary_list

        out["SummaryItems"] = (
            capo_kendra_ranking.types.rescore_execution_plan_summary_list.serialize_cbor(
                value["summary_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRescoreExecutionPlansResponse:
    out: ListRescoreExecutionPlansResponse = {}  # type: ignore[typeddict-item]
    if data.get("SummaryItems") is not None:
        import capo_kendra_ranking.types.rescore_execution_plan_summary_list

        out["summary_items"] = (
            capo_kendra_ranking.types.rescore_execution_plan_summary_list.deserialize_cbor(
                data["SummaryItems"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
