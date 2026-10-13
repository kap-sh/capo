"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentRecommendationSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_summary

AgentRecommendationSummaries: TypeAlias = list[
    "capo_wellarchitected.types.agent_recommendation_summary.AgentRecommendationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRecommendationSummaries) -> list:
    import capo_wellarchitected.types.agent_recommendation_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.agent_recommendation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentRecommendationSummaries:
    import capo_wellarchitected.types.agent_recommendation_summary

    out: AgentRecommendationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.agent_recommendation_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AgentRecommendationSummaries) -> list[Any]:
    import capo_wellarchitected.types.agent_recommendation_summary

    return [
        capo_wellarchitected.types.agent_recommendation_summary.redact_sensitive(item)
        for item in value
    ]
