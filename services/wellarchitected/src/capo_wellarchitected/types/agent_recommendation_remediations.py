"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentRecommendationRemediations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_recommendation_remediation

AgentRecommendationRemediations: TypeAlias = list[
    "capo_wellarchitected.types.agent_recommendation_remediation.AgentRecommendationRemediation"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRecommendationRemediations) -> list:
    import capo_wellarchitected.types.agent_recommendation_remediation

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.agent_recommendation_remediation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentRecommendationRemediations:
    import capo_wellarchitected.types.agent_recommendation_remediation

    out: AgentRecommendationRemediations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.agent_recommendation_remediation.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AgentRecommendationRemediations) -> list[Any]:
    import capo_wellarchitected.types.agent_recommendation_remediation

    return [
        capo_wellarchitected.types.agent_recommendation_remediation.redact_sensitive(
            item
        )
        for item in value
    ]
