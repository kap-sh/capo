"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderPromotionalFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.percent_promoted_items
    import capo_customer_profiles.types.recommender_filter_values


class RecommenderPromotionalFilter(TypedDict, closed=True):
    name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender filter to use for the promotion.</p>"""
    values: NotRequired[
        "capo_customer_profiles.types.recommender_filter_values.RecommenderFilterValues"
    ]
    """<p>The values to use when promoting items. For each placeholder parameter in your promotion's filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.</p>"""
    promotion_name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the promotion.</p>"""
    percent_promoted_items: NotRequired[
        "capo_customer_profiles.types.percent_promoted_items.PercentPromotedItems"
    ]
    """<p>The percentage of recommended items to apply the promotion to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderPromotionalFilter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import capo_customer_profiles.types.recommender_filter_values

        out["Values"] = (
            capo_customer_profiles.types.recommender_filter_values.serialize_json(
                value["values"]
            )
        )
    if "promotion_name" in value:
        out["PromotionName"] = value["promotion_name"]
    if "percent_promoted_items" in value:
        out["PercentPromotedItems"] = value["percent_promoted_items"]
    return out


def deserialize_json(data: dict) -> RecommenderPromotionalFilter:
    out: RecommenderPromotionalFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Values") is not None:
        import capo_customer_profiles.types.recommender_filter_values

        out["values"] = (
            capo_customer_profiles.types.recommender_filter_values.deserialize_json(
                data["Values"]
            )
        )
    if data.get("PromotionName") is not None:
        out["promotion_name"] = data["PromotionName"]
    if data.get("PercentPromotedItems") is not None:
        out["percent_promoted_items"] = data["PercentPromotedItems"]
    return out


def redact_sensitive(value: RecommenderPromotionalFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_customer_profiles.types.recommender_filter_values

        out["values"] = (
            capo_customer_profiles.types.recommender_filter_values.redact_sensitive(
                value["values"]
            )
        )
    return out
