"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.document_list
    import capo_kendra_ranking.types.rescore_execution_plan_id
    import capo_kendra_ranking.types.search_query


class RescoreRequest(TypedDict, closed=True):
    rescore_execution_plan_id: (
        "capo_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    )
    """<p>The identifier of the rescore execution plan. A rescore execution plan is an Amazon Kendra Intelligent Ranking resource used for provisioning the <code>Rescore</code> API.</p>"""
    search_query: "capo_kendra_ranking.types.search_query.SearchQuery"
    """<p>The input query from the search service.</p>"""
    documents: "capo_kendra_ranking.types.document_list.DocumentList"
    """<p>The list of documents for Amazon Kendra Intelligent Ranking to rescore or rank on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreRequest) -> dict:
    out: dict = {}
    out["RescoreExecutionPlanId"] = value["rescore_execution_plan_id"]
    out["SearchQuery"] = value["search_query"]
    import capo_kendra_ranking.types.document_list

    out["Documents"] = capo_kendra_ranking.types.document_list.serialize_aws_json_1_0(
        value["documents"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreRequest:
    out: RescoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("RescoreExecutionPlanId") is not None:
        out["rescore_execution_plan_id"] = data["RescoreExecutionPlanId"]
    else:
        out["rescore_execution_plan_id"] = ""
    if data.get("SearchQuery") is not None:
        out["search_query"] = data["SearchQuery"]
    else:
        out["search_query"] = ""
    if data.get("Documents") is not None:
        import capo_kendra_ranking.types.document_list

        out["documents"] = (
            capo_kendra_ranking.types.document_list.deserialize_aws_json_1_0(
                data["Documents"]
            )
        )
    else:
        out["documents"] = []
    return out
