"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.recommendation_error
    import capo_accessanalyzer.types.recommendation_type
    import capo_accessanalyzer.types.recommended_step_list
    import capo_accessanalyzer.types.resource_arn
    import capo_accessanalyzer.types.status
    import capo_accessanalyzer.types.timestamp
    import capo_accessanalyzer.types.token


class GetFindingRecommendationResponse(TypedDict, closed=True):
    started_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the retrieval of the finding recommendation was started.</p>"""
    completed_at: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the retrieval of the finding recommendation was completed.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    error: NotRequired[
        "capo_accessanalyzer.types.recommendation_error.RecommendationError"
    ]
    """<p>Detailed information about the reason that the retrieval of a recommendation for the finding failed.</p>"""
    resource_arn: "capo_accessanalyzer.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource of the finding.</p>"""
    recommended_steps: NotRequired[
        "capo_accessanalyzer.types.recommended_step_list.RecommendedStepList"
    ]
    """<p>A group of recommended steps for the finding.</p>"""
    recommendation_type: (
        "capo_accessanalyzer.types.recommendation_type.RecommendationType"
    )
    """<p>The type of recommendation for the finding.</p>"""
    status: "capo_accessanalyzer.types.status.Status"
    """<p>The status of the retrieval of the finding recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingRecommendationResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.timestamp

    out["startedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["started_at"]
    )
    if "completed_at" in value:
        import capo_accessanalyzer.types.timestamp

        out["completedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["completed_at"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "error" in value:
        import capo_accessanalyzer.types.recommendation_error

        out["error"] = capo_accessanalyzer.types.recommendation_error.serialize_json(
            value["error"]
        )
    out["resourceArn"] = value["resource_arn"]
    if "recommended_steps" in value:
        import capo_accessanalyzer.types.recommended_step_list

        out["recommendedSteps"] = (
            capo_accessanalyzer.types.recommended_step_list.serialize_json(
                value["recommended_steps"]
            )
        )
    out["recommendationType"] = value["recommendation_type"]
    out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> GetFindingRecommendationResponse:
    out: GetFindingRecommendationResponse = {}  # type: ignore[typeddict-item]
    if data.get("startedAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["started_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("completedAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["completed_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["completedAt"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("error") is not None:
        import capo_accessanalyzer.types.recommendation_error

        out["error"] = capo_accessanalyzer.types.recommendation_error.deserialize_json(
            data["error"]
        )
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("recommendedSteps") is not None:
        import capo_accessanalyzer.types.recommended_step_list

        out["recommended_steps"] = (
            capo_accessanalyzer.types.recommended_step_list.deserialize_json(
                data["recommendedSteps"]
            )
        )
    if data.get("recommendationType") is not None:
        out["recommendation_type"] = data["recommendationType"]
    else:
        out["recommendation_type"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
