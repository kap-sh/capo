"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationTrigger``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.recommendation_id_list
    import capo_qconnect.types.recommendation_source_type
    import capo_qconnect.types.recommendation_trigger_data
    import capo_qconnect.types.recommendation_trigger_type
    import capo_qconnect.types.uuid


class RecommendationTrigger(TypedDict, closed=True):
    id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the recommendation trigger.</p>"""
    type: "capo_qconnect.types.recommendation_trigger_type.RecommendationTriggerType"
    """<p>The type of recommendation trigger.</p>"""
    source: "capo_qconnect.types.recommendation_source_type.RecommendationSourceType"
    """<p>The source of the recommendation trigger.</p> <ul> <li> <p>ISSUE_DETECTION: The corresponding recommendations were triggered by a Contact Lens issue.</p> </li> <li> <p>RULE_EVALUATION: The corresponding recommendations were triggered by a Contact Lens rule.</p> </li> </ul>"""
    data: "capo_qconnect.types.recommendation_trigger_data.RecommendationTriggerData"
    """<p>A union type containing information related to the trigger.</p>"""
    recommendation_ids: (
        "capo_qconnect.types.recommendation_id_list.RecommendationIdList"
    )
    """<p>The identifiers of the recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTrigger) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["type"] = value["type"]
    out["source"] = value["source"]
    import capo_qconnect.types.recommendation_trigger_data

    out["data"] = capo_qconnect.types.recommendation_trigger_data.serialize_json(
        value["data"]
    )
    import capo_qconnect.types.recommendation_id_list

    out["recommendationIds"] = (
        capo_qconnect.types.recommendation_id_list.serialize_json(
            value["recommendation_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> RecommendationTrigger:
    out: RecommendationTrigger = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("data") is not None:
        import capo_qconnect.types.recommendation_trigger_data

        out["data"] = capo_qconnect.types.recommendation_trigger_data.deserialize_json(
            data["data"]
        )
    else:
        import capo_qconnect.types._unknown

        out["data"] = capo_qconnect.types._unknown.UnknownUnionMember("")
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


def redact_sensitive(value: RecommendationTrigger) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data" in value:
        import capo_qconnect.types.recommendation_trigger_data

        out["data"] = capo_qconnect.types.recommendation_trigger_data.redact_sensitive(
            value["data"]
        )
    return out
