"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ExecutionSummaryClusteringResultContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.execution_summary_cluster_list


class ExecutionSummaryClusteringResultContent(TypedDict, closed=True):
    execution_summaries: "capo_bedrock_agentcore.types.execution_summary_cluster_list.ExecutionSummaryClusterList"
    """<p>The list of execution summary clusters identified across analyzed sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionSummaryClusteringResultContent) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.execution_summary_cluster_list

    out["executionSummaries"] = (
        capo_bedrock_agentcore.types.execution_summary_cluster_list.serialize_json(
            value["execution_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExecutionSummaryClusteringResultContent:
    out: ExecutionSummaryClusteringResultContent = {}  # type: ignore[typeddict-item]
    if data.get("executionSummaries") is not None:
        import capo_bedrock_agentcore.types.execution_summary_cluster_list

        out["execution_summaries"] = (
            capo_bedrock_agentcore.types.execution_summary_cluster_list.deserialize_json(
                data["executionSummaries"]
            )
        )
    else:
        out["execution_summaries"] = []
    return out
