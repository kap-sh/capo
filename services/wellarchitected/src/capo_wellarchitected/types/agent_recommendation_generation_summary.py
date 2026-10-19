"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentRecommendationGenerationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.generation_status
    import capo_wellarchitected.types.uuid


class AgentRecommendationGenerationSummary(TypedDict, closed=True):
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


# --- restJson1 ser/de ---
def serialize_json(value: AgentRecommendationGenerationSummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> AgentRecommendationGenerationSummary:
    out: AgentRecommendationGenerationSummary = {}  # type: ignore[typeddict-item]
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
    return out
