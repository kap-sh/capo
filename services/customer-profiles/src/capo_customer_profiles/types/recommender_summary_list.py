"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_summary

RecommenderSummaryList: TypeAlias = list[
    "capo_customer_profiles.types.recommender_summary.RecommenderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderSummaryList) -> list:
    import capo_customer_profiles.types.recommender_summary

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.recommender_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommenderSummaryList:
    import capo_customer_profiles.types.recommender_summary

    out: RecommenderSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.recommender_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RecommenderSummaryList) -> list[Any]:
    import capo_customer_profiles.types.recommender_summary

    return [
        capo_customer_profiles.types.recommender_summary.redact_sensitive(item)
        for item in value
    ]
