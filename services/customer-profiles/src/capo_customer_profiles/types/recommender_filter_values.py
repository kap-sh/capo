"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilterValues``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_filter_attribute_name
    import capo_customer_profiles.types.recommender_filter_attribute_value

RecommenderFilterValues: TypeAlias = dict[
    "capo_customer_profiles.types.recommender_filter_attribute_name.RecommenderFilterAttributeName",
    "capo_customer_profiles.types.recommender_filter_attribute_value.RecommenderFilterAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RecommenderFilterValues) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RecommenderFilterValues:
    out: RecommenderFilterValues = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: RecommenderFilterValues) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
