"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.guid
    import capo_opensearch.types.insight_feedback_entity
    import capo_opensearch.types.insight_feedback_text
    import capo_opensearch.types.insight_feedback_thumbs


class InsightFeedbackRequest(TypedDict, closed=True):
    entity: "capo_opensearch.types.insight_feedback_entity.InsightFeedbackEntity"
    """<p>The entity for which to submit insight feedback. Specifies the type and value of the entity, such as a domain name.</p>"""
    insight_id: "capo_opensearch.types.guid.GUID"
    """<p>The unique identifier of the insight for which to submit feedback.</p>"""
    thumbs: "capo_opensearch.types.insight_feedback_thumbs.InsightFeedbackThumbs"
    """<p>The thumbs up or thumbs down feedback for the insight. Possible values are <code>Up</code> and <code>Down</code>.</p>"""
    feedback_text: NotRequired[
        "capo_opensearch.types.insight_feedback_text.InsightFeedbackText"
    ]
    """<p>Optional text feedback providing additional details about the insight. Maximum length is 1000 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightFeedbackRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.insight_feedback_entity

    out["Entity"] = capo_opensearch.types.insight_feedback_entity.serialize_json(
        value["entity"]
    )
    out["InsightId"] = value["insight_id"]
    import capo_opensearch.types.insight_feedback_thumbs

    out["Thumbs"] = capo_opensearch.types.insight_feedback_thumbs.serialize_json(
        value["thumbs"]
    )
    if "feedback_text" in value:
        out["FeedbackText"] = value["feedback_text"]
    return out


def deserialize_json(data: dict) -> InsightFeedbackRequest:
    out: InsightFeedbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("Entity") is not None:
        import capo_opensearch.types.insight_feedback_entity

        out["entity"] = capo_opensearch.types.insight_feedback_entity.deserialize_json(
            data["Entity"]
        )
    else:
        raise DeserializationError("InsightFeedbackRequest.entity required")
    if data.get("InsightId") is not None:
        out["insight_id"] = data["InsightId"]
    else:
        out["insight_id"] = ""
    if data.get("Thumbs") is not None:
        import capo_opensearch.types.insight_feedback_thumbs

        out["thumbs"] = capo_opensearch.types.insight_feedback_thumbs.deserialize_json(
            data["Thumbs"]
        )
    else:
        import typing

        out["thumbs"] = typing.cast(
            "capo_opensearch.types.insight_feedback_thumbs.InsightFeedbackThumbs", ""
        )
    if data.get("FeedbackText") is not None:
        out["feedback_text"] = data["FeedbackText"]
    return out
