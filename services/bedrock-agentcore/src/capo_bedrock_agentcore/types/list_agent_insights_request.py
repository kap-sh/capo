"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListAgentInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_application_name
    import capo_bedrock_agentcore.types.agent_insight_archive_status
    import capo_bedrock_agentcore.types.batch_evaluation_id
    import capo_bedrock_agentcore.types.next_token


class ListAgentInsightsRequest(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_bedrock_agentcore.types.agent_application_name.AgentApplicationName"
    ]
    """<p>Filters the results to Agent Insights for an application.</p>"""
    batch_evaluation_id: NotRequired[
        "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId"
    ]
    """<p>Filters the results to Agent Insights produced by a batch evaluation.</p>"""
    archive_status: NotRequired[
        "capo_bedrock_agentcore.types.agent_insight_archive_status.AgentInsightArchiveStatus"
    ]
    """<p>Filters the results by archive status.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of Agent Insight summaries to return in one response. If you don't specify a value, the operation returns up to 50 summaries.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore.types.next_token.NextToken"]
    """<p>A token to specify where to start paginating the results. This token is returned in a previous response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentInsightsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentInsightsRequest:
    out: ListAgentInsightsRequest = {}  # type: ignore[typeddict-item]
    return out
