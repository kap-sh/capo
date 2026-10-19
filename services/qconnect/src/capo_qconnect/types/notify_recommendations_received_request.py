"""Generated from Smithy shape ``com.amazonaws.qconnect#NotifyRecommendationsReceivedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.recommendation_id_list
    import capo_qconnect.types.uuid_or_arn


class NotifyRecommendationsReceivedRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    recommendation_ids: (
        "capo_qconnect.types.recommendation_id_list.RecommendationIdList"
    )
    """<p>The identifiers of the recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotifyRecommendationsReceivedRequest) -> dict:
    out: dict = {}
    import capo_qconnect.types.recommendation_id_list

    out["recommendationIds"] = (
        capo_qconnect.types.recommendation_id_list.serialize_json(
            value["recommendation_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> NotifyRecommendationsReceivedRequest:
    out: NotifyRecommendationsReceivedRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommendationIds") is not None:
        import capo_qconnect.types.recommendation_id_list

        out["recommendation_ids"] = (
            capo_qconnect.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    else:
        out["recommendation_ids"] = []
    return out
