"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentRecommendationGenerationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.error_details
    import capo_wellarchitected.types.generation_recommendation_types
    import capo_wellarchitected.types.generation_status
    import capo_wellarchitected.types.generation_type
    import capo_wellarchitected.types.progress
    import capo_wellarchitected.types.scope
    import capo_wellarchitected.types.sensitive_document
    import capo_wellarchitected.types.uuid


class GetAgentRecommendationGenerationResponse(TypedDict, closed=True):
    id: "capo_wellarchitected.types.uuid.UUID"
    """<p>The unique identifier of the recommendation generation.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile used for this generation.</p>"""
    name: NotRequired["str"]
    """<p>The name of the recommendation generation.</p>"""
    status: "capo_wellarchitected.types.generation_status.GenerationStatus"
    """<p>The current status of the recommendation generation.</p>"""
    estimated_completion_time: NotRequired["datetime.datetime"]
    """<p>The estimated time for the generation to complete.</p>"""
    created_by: "str"
    """<p>The identifier of the user or system that started this generation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the generation was started.</p>"""
    last_modified_by: NotRequired["str"]
    """<p>The identifier of the user or system that last modified this generation.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the generation was last modified.</p>"""
    generation_type: NotRequired[
        "capo_wellarchitected.types.generation_type.GenerationType"
    ]
    """<p>How the generation was started.</p>"""
    generation_recommendation_types: NotRequired[
        "capo_wellarchitected.types.generation_recommendation_types.GenerationRecommendationTypes"
    ]
    """<p>The recommendation types the generation covers.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the recommendation generation process started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the recommendation generation process completed.</p>"""
    error_details: NotRequired["capo_wellarchitected.types.error_details.ErrorDetails"]
    """<p>Details about the error if the generation status is ERROR.</p>"""
    additional_context: NotRequired[
        "capo_wellarchitected.types.sensitive_document.SensitiveDocument"
    ]
    """<p>The additional context that was provided when the generation was started. For <code>ARCHITECTURE</code> generations, this includes the location of the reviewed IaC template and the lenses used.</p>"""
    scope: NotRequired["capo_wellarchitected.types.scope.Scope"]
    """<p>The scope configuration that defines which pillars and goals to focus on during generation.</p>"""
    progress: NotRequired["capo_wellarchitected.types.progress.Progress"]
    """<p>Current progress information including steps completed and completion percentage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRecommendationGenerationResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["profileArn"] = value["profile_arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_wellarchitected.types.generation_status

    out["status"] = capo_wellarchitected.types.generation_status.serialize_json(
        value["status"]
    )
    if "estimated_completion_time" in value:
        import capo_wellarchitected._protocol.serialize

        out["estimatedCompletionTime"] = (
            capo_wellarchitected._protocol.serialize.fmt_date_time(
                value["estimated_completion_time"]
            )
        )
    out["createdBy"] = value["created_by"]
    import capo_wellarchitected._protocol.serialize

    out["createdAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "last_modified_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["lastModifiedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    if "generation_type" in value:
        import capo_wellarchitected.types.generation_type

        out["generationType"] = (
            capo_wellarchitected.types.generation_type.serialize_json(
                value["generation_type"]
            )
        )
    if "generation_recommendation_types" in value:
        import capo_wellarchitected.types.generation_recommendation_types

        out["generationRecommendationTypes"] = (
            capo_wellarchitected.types.generation_recommendation_types.serialize_json(
                value["generation_recommendation_types"]
            )
        )
    if "started_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["startedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["endedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["ended_at"]
        )
    if "error_details" in value:
        import capo_wellarchitected.types.error_details

        out["errorDetails"] = capo_wellarchitected.types.error_details.serialize_json(
            value["error_details"]
        )
    if "additional_context" in value:
        out["additionalContext"] = value["additional_context"]
    if "scope" in value:
        import capo_wellarchitected.types.scope

        out["scope"] = capo_wellarchitected.types.scope.serialize_json(value["scope"])
    if "progress" in value:
        import capo_wellarchitected.types.progress

        out["progress"] = capo_wellarchitected.types.progress.serialize_json(
            value["progress"]
        )
    return out


def deserialize_json(data: dict) -> GetAgentRecommendationGenerationResponse:
    out: GetAgentRecommendationGenerationResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        out["profile_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_wellarchitected.types.generation_status

        out["status"] = capo_wellarchitected.types.generation_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_wellarchitected.types.generation_status.GenerationStatus", ""
        )
    if data.get("estimatedCompletionTime") is not None:
        import datetime

        out["estimated_completion_time"] = datetime.datetime.fromisoformat(
            data["estimatedCompletionTime"].replace("Z", "+00:00")
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["lastModifiedAt"].replace("Z", "+00:00")
        )
    if data.get("generationType") is not None:
        import capo_wellarchitected.types.generation_type

        out["generation_type"] = (
            capo_wellarchitected.types.generation_type.deserialize_json(
                data["generationType"]
            )
        )
    if data.get("generationRecommendationTypes") is not None:
        import capo_wellarchitected.types.generation_recommendation_types

        out["generation_recommendation_types"] = (
            capo_wellarchitected.types.generation_recommendation_types.deserialize_json(
                data["generationRecommendationTypes"]
            )
        )
    if data.get("startedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["startedAt"].replace("Z", "+00:00")
        )
    if data.get("endedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["endedAt"].replace("Z", "+00:00")
        )
    if data.get("errorDetails") is not None:
        import capo_wellarchitected.types.error_details

        out["error_details"] = (
            capo_wellarchitected.types.error_details.deserialize_json(
                data["errorDetails"]
            )
        )
    if data.get("additionalContext") is not None:
        out["additional_context"] = data["additionalContext"]
    if data.get("scope") is not None:
        import capo_wellarchitected.types.scope

        out["scope"] = capo_wellarchitected.types.scope.deserialize_json(data["scope"])
    if data.get("progress") is not None:
        import capo_wellarchitected.types.progress

        out["progress"] = capo_wellarchitected.types.progress.deserialize_json(
            data["progress"]
        )
    return out


def redact_sensitive(value: GetAgentRecommendationGenerationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "additional_context" in value:
        out["additional_context"] = "*** Sensitive Data Redacted ***"
    return out
