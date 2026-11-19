"""Generated from Smithy shape ``com.amazonaws.kendraranking#ListRescoreExecutionPlansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request
    import capo_kendra_ranking.types.next_token


class ListRescoreExecutionPlansRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_kendra_ranking.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra Intelligent Ranking returns a pagination token in the response. You can use this pagination token to retrieve the next set of rescore execution plans.</p>"""
    max_results: NotRequired[
        "capo_kendra_ranking.types.max_results_integer_for_list_rescore_execution_plans_request.MaxResultsIntegerForListRescoreExecutionPlansRequest"
    ]
    """<p>The maximum number of rescore execution plans to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRescoreExecutionPlansRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRescoreExecutionPlansRequest:
    out: ListRescoreExecutionPlansRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRescoreExecutionPlansRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListRescoreExecutionPlansRequest:
    out: ListRescoreExecutionPlansRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
