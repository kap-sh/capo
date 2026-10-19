"""Generated from Smithy shape ``com.amazonaws.wellarchitected#StartAgentRecommendationGenerationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.recommendation_types
    import capo_wellarchitected.types.scope


class StartAgentRecommendationGenerationRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the optimization profile to use for generating recommendations.</p>"""
    types: "capo_wellarchitected.types.recommendation_types.RecommendationTypes"
    """<p>The types of recommendations to generate.</p>"""
    name: NotRequired["str"]
    """<p>An optional name for this generation process to help identify it in lists and logs.</p>"""
    additional_context: NotRequired["object"]
    """<p>Optional additional context to guide the recommendation generation, such as specific business requirements or constraints.</p>"""
    scope: "capo_wellarchitected.types.scope.Scope"
    """<p>Scope configuration to focus the generation on specific pillars or goals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAgentRecommendationGenerationRequest) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.recommendation_types

    out["types"] = capo_wellarchitected.types.recommendation_types.serialize_json(
        value["types"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "additional_context" in value:
        out["additionalContext"] = value["additional_context"]
    import capo_wellarchitected.types.scope

    out["scope"] = capo_wellarchitected.types.scope.serialize_json(value["scope"])
    return out


def deserialize_json(data: dict) -> StartAgentRecommendationGenerationRequest:
    out: StartAgentRecommendationGenerationRequest = {}  # type: ignore[typeddict-item]
    if data.get("types") is not None:
        import capo_wellarchitected.types.recommendation_types

        out["types"] = capo_wellarchitected.types.recommendation_types.deserialize_json(
            data["types"]
        )
    else:
        out["types"] = []
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("additionalContext") is not None:
        out["additional_context"] = data["additionalContext"]
    if data.get("scope") is not None:
        import capo_wellarchitected.types.scope

        out["scope"] = capo_wellarchitected.types.scope.deserialize_json(data["scope"])
    else:
        raise DeserializationError(
            "StartAgentRecommendationGenerationRequest.scope required"
        )
    return out
