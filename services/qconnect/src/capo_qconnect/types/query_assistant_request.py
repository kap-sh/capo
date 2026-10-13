"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryAssistantRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_search_type
    import capo_qconnect.types.max_results
    import capo_qconnect.types.next_token
    import capo_qconnect.types.query_condition_expression
    import capo_qconnect.types.query_input_data
    import capo_qconnect.types.query_text
    import capo_qconnect.types.uuid_or_arn


class QueryAssistantRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    query_text: NotRequired["capo_qconnect.types.query_text.QueryText"]
    """<p>The text to search for.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    session_id: NotRequired["capo_qconnect.types.uuid_or_arn.UuidOrArn"]
    """<p>The identifier of the Amazon Q in Connect session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    query_condition: NotRequired[
        "capo_qconnect.types.query_condition_expression.QueryConditionExpression"
    ]
    """<p>Information about how to query content.</p>"""
    query_input_data: NotRequired["capo_qconnect.types.query_input_data.QueryInputData"]
    """<p>Information about the query.</p>"""
    override_knowledge_base_search_type: NotRequired[
        "capo_qconnect.types.knowledge_base_search_type.KnowledgeBaseSearchType"
    ]
    """<p>The search type to be used against the Knowledge Base for this request. The values can be <code>SEMANTIC</code> which uses vector embeddings or <code>HYBRID</code> which use vector embeddings and raw text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryAssistantRequest) -> dict:
    out: dict = {}
    if "query_text" in value:
        out["queryText"] = value["query_text"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "query_condition" in value:
        import capo_qconnect.types.query_condition_expression

        out["queryCondition"] = (
            capo_qconnect.types.query_condition_expression.serialize_json(
                value["query_condition"]
            )
        )
    if "query_input_data" in value:
        import capo_qconnect.types.query_input_data

        out["queryInputData"] = capo_qconnect.types.query_input_data.serialize_json(
            value["query_input_data"]
        )
    if "override_knowledge_base_search_type" in value:
        out["overrideKnowledgeBaseSearchType"] = value[
            "override_knowledge_base_search_type"
        ]
    return out


def deserialize_json(data: dict) -> QueryAssistantRequest:
    out: QueryAssistantRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryText") is not None:
        out["query_text"] = data["queryText"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("queryCondition") is not None:
        import capo_qconnect.types.query_condition_expression

        out["query_condition"] = (
            capo_qconnect.types.query_condition_expression.deserialize_json(
                data["queryCondition"]
            )
        )
    if data.get("queryInputData") is not None:
        import capo_qconnect.types.query_input_data

        out["query_input_data"] = capo_qconnect.types.query_input_data.deserialize_json(
            data["queryInputData"]
        )
    if data.get("overrideKnowledgeBaseSearchType") is not None:
        out["override_knowledge_base_search_type"] = data[
            "overrideKnowledgeBaseSearchType"
        ]
    return out


def redact_sensitive(value: QueryAssistantRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_text" in value:
        out["query_text"] = "*** Sensitive Data Redacted ***"
    if "query_input_data" in value:
        import capo_qconnect.types.query_input_data

        out["query_input_data"] = capo_qconnect.types.query_input_data.redact_sensitive(
            value["query_input_data"]
        )
    return out
