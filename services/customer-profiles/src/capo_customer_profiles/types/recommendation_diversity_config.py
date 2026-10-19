"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommendationDiversityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.diversity_values_map
    import capo_customer_profiles.types.optional_boolean


class RecommendationDiversityConfig(TypedDict, closed=True):
    enabled: "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    """<p>Whether diversity-aware recommendations are enabled for this request.</p>"""
    values: NotRequired[
        "capo_customer_profiles.types.diversity_values_map.DiversityValuesMap"
    ]
    """<p>An optional map of placeholder name to integer cap value used to resolve <code>$name</code> placeholders defined in the recommender's <code>DiversityConfig</code> at inference time. Up to 2 entries are supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationDiversityConfig) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "values" in value:
        import capo_customer_profiles.types.diversity_values_map

        out["Values"] = (
            capo_customer_profiles.types.diversity_values_map.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommendationDiversityConfig:
    out: RecommendationDiversityConfig = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("Values") is not None:
        import capo_customer_profiles.types.diversity_values_map

        out["values"] = (
            capo_customer_profiles.types.diversity_values_map.deserialize_json(
                data["Values"]
            )
        )
    return out
