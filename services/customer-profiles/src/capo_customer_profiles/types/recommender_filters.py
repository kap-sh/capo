"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_filter

RecommenderFilters: TypeAlias = list[
    "capo_customer_profiles.types.recommender_filter.RecommenderFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderFilters) -> list:
    import capo_customer_profiles.types.recommender_filter

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.recommender_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommenderFilters:
    import capo_customer_profiles.types.recommender_filter

    out: RecommenderFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.recommender_filter.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RecommenderFilters) -> list[Any]:
    import capo_customer_profiles.types.recommender_filter

    return [
        capo_customer_profiles.types.recommender_filter.redact_sensitive(item)
        for item in value
    ]
