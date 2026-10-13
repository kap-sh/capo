"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderPromotionalFilters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_promotional_filter

RecommenderPromotionalFilters: TypeAlias = list[
    "capo_customer_profiles.types.recommender_promotional_filter.RecommenderPromotionalFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderPromotionalFilters) -> list:
    import capo_customer_profiles.types.recommender_promotional_filter

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.recommender_promotional_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommenderPromotionalFilters:
    import capo_customer_profiles.types.recommender_promotional_filter

    out: RecommenderPromotionalFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.recommender_promotional_filter.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RecommenderPromotionalFilters) -> list[Any]:
    import capo_customer_profiles.types.recommender_promotional_filter

    return [
        capo_customer_profiles.types.recommender_promotional_filter.redact_sensitive(
            item
        )
        for item in value
    ]
