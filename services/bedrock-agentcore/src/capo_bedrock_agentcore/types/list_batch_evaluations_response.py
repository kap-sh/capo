"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListBatchEvaluationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.batch_evaluation_summary_list


class ListBatchEvaluationsResponse(TypedDict, closed=True):
    batch_evaluations: "capo_bedrock_agentcore.types.batch_evaluation_summary_list.BatchEvaluationSummaryList"
    """<p>The list of batch evaluation summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchEvaluationsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.batch_evaluation_summary_list

    out["batchEvaluations"] = (
        capo_bedrock_agentcore.types.batch_evaluation_summary_list.serialize_json(
            value["batch_evaluations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBatchEvaluationsResponse:
    out: ListBatchEvaluationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("batchEvaluations") is not None:
        import capo_bedrock_agentcore.types.batch_evaluation_summary_list

        out["batch_evaluations"] = (
            capo_bedrock_agentcore.types.batch_evaluation_summary_list.deserialize_json(
                data["batchEvaluations"]
            )
        )
    else:
        out["batch_evaluations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
