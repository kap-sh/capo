"""Generated from Smithy shape ``com.amazonaws.wisdom#RecommendationTriggerData``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_wisdom.types.query_recommendation_trigger_data


class _RecommendationTriggerData_query(TypedDict, closed=True):
    query: "capo_wisdom.types.query_recommendation_trigger_data.QueryRecommendationTriggerData"


RecommendationTriggerData: TypeAlias = _RecommendationTriggerData_query


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTriggerData) -> dict:
    if "query" in value:
        import capo_wisdom.types.query_recommendation_trigger_data

        return {
            "query": capo_wisdom.types.query_recommendation_trigger_data.serialize_json(
                value["query"]
            )
        }
    else:
        raise SerializationError("RecommendationTriggerData: no variant present")


def deserialize_json(data: dict) -> RecommendationTriggerData:
    if data.get("query") is not None:
        import capo_wisdom.types.query_recommendation_trigger_data

        return {
            "query": capo_wisdom.types.query_recommendation_trigger_data.deserialize_json(
                data["query"]
            )
        }
    else:
        raise DeserializationError(
            "RecommendationTriggerData: no recognized variant key"
        )


def redact_sensitive(value: RecommendationTriggerData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query" in value:
        import capo_wisdom.types.query_recommendation_trigger_data

        out["query"] = (
            capo_wisdom.types.query_recommendation_trigger_data.redact_sensitive(
                value["query"]
            )
        )
    return out
