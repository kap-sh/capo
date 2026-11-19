"""Generated from Smithy shape ``com.amazonaws.wellarchitected#StartAgentRecommendationGenerationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.recommendation_types
    import capo_wellarchitected.types.scope
    import capo_wellarchitected.types.sensitive_document


class StartAgentRecommendationGenerationRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the optimization profile to use for generating recommendations.</p>"""
    types: "capo_wellarchitected.types.recommendation_types.RecommendationTypes"
    """<p>The types of recommendations to generate. You can specify up to two types in a single request. Currently, only <code>ARCHITECTURE</code> is supported for this operation.</p>"""
    name: NotRequired["str"]
    """<p>An optional name for this generation that identifies the architecture review in the console and in <code>ListAgentRecommendationGenerations</code> results. Applies to <code>ARCHITECTURE</code> type only. Must be absent for other types.</p>"""
    additional_context: NotRequired[
        "capo_wellarchitected.types.sensitive_document.SensitiveDocument"
    ]
    """<p>The location of the infrastructure as code (IaC) template to review, and the lenses to review it against. Required for the <code>ARCHITECTURE</code> type. Must be absent for other types. Specify a JSON object with the following members:</p> <ul> <li> <p> <code>s3Uri</code>: The Amazon S3 URI of the IaC template, .zip archive, or folder to review.</p> </li> <li> <p> <code>s3VersionId</code>: The version ID of the Amazon S3 object. If you omit this member, the current version is used.</p> </li> <li> <p> <code>lensArns</code>: The ARNs of the lenses to review against. Only <code>arn:aws:wellarchitected::aws:lens/wellarchitected</code> is supported.</p> </li> </ul>"""
    scope: NotRequired["capo_wellarchitected.types.scope.Scope"]
    """<p>Defines which pillars, goals, and items the review covers. Required for the <code>ARCHITECTURE</code> type. Must be absent for other types.</p>"""


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
    if "scope" in value:
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
    return out


def redact_sensitive(
    value: StartAgentRecommendationGenerationRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "additional_context" in value:
        out["additional_context"] = "*** Sensitive Data Redacted ***"
    return out
