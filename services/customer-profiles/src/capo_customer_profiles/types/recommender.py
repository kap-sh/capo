"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Recommender``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_filters
    import capo_customer_profiles.types.recommender_promotional_filters


class Recommender(TypedDict, closed=True):
    name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the recommender.</p>"""
    filters: NotRequired[
        "capo_customer_profiles.types.recommender_filters.RecommenderFilters"
    ]
    """<p>A list of filters to apply to the returned recommendations. Filters define criteria for including or excluding items from the recommendation results.</p>"""
    promotional_filters: NotRequired[
        "capo_customer_profiles.types.recommender_promotional_filters.RecommenderPromotionalFilters"
    ]
    """<p>A list of promotional filters to apply to the recommendations. Promotional filters allow you to promote specific items within a configurable subset of recommendation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommender) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "filters" in value:
        import capo_customer_profiles.types.recommender_filters

        out["Filters"] = (
            capo_customer_profiles.types.recommender_filters.serialize_json(
                value["filters"]
            )
        )
    if "promotional_filters" in value:
        import capo_customer_profiles.types.recommender_promotional_filters

        out["PromotionalFilters"] = (
            capo_customer_profiles.types.recommender_promotional_filters.serialize_json(
                value["promotional_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Recommender:
    out: Recommender = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Recommender.name required")
    if data.get("Filters") is not None:
        import capo_customer_profiles.types.recommender_filters

        out["filters"] = (
            capo_customer_profiles.types.recommender_filters.deserialize_json(
                data["Filters"]
            )
        )
    if data.get("PromotionalFilters") is not None:
        import capo_customer_profiles.types.recommender_promotional_filters

        out["promotional_filters"] = (
            capo_customer_profiles.types.recommender_promotional_filters.deserialize_json(
                data["PromotionalFilters"]
            )
        )
    return out


def redact_sensitive(value: Recommender) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_customer_profiles.types.recommender_filters

        out["filters"] = (
            capo_customer_profiles.types.recommender_filters.redact_sensitive(
                value["filters"]
            )
        )
    if "promotional_filters" in value:
        import capo_customer_profiles.types.recommender_promotional_filters

        out["promotional_filters"] = (
            capo_customer_profiles.types.recommender_promotional_filters.redact_sensitive(
                value["promotional_filters"]
            )
        )
    return out
