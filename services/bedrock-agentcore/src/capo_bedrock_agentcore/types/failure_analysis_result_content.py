"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FailureAnalysisResultContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.failure_category_cluster_list


class FailureAnalysisResultContent(TypedDict, closed=True):
    failures: "capo_bedrock_agentcore.types.failure_category_cluster_list.FailureCategoryClusterList"
    """<p>The list of failure category clusters identified across analyzed sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureAnalysisResultContent) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.failure_category_cluster_list

    out["failures"] = (
        capo_bedrock_agentcore.types.failure_category_cluster_list.serialize_json(
            value["failures"]
        )
    )
    return out


def deserialize_json(data: dict) -> FailureAnalysisResultContent:
    out: FailureAnalysisResultContent = {}  # type: ignore[typeddict-item]
    if data.get("failures") is not None:
        import capo_bedrock_agentcore.types.failure_category_cluster_list

        out["failures"] = (
            capo_bedrock_agentcore.types.failure_category_cluster_list.deserialize_json(
                data["failures"]
            )
        )
    else:
        out["failures"] = []
    return out
