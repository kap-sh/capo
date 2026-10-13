"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.recommender_filter_values


class RecommenderFilter(TypedDict, closed=True):
    name: NotRequired["capo_customer_profiles.types.name.name"]
    """<p>The name of the recommender filter to apply.</p>"""
    values: NotRequired[
        "capo_customer_profiles.types.recommender_filter_values.RecommenderFilterValues"
    ]
    """<p>The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderFilter) -> dict:
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
    return out


def deserialize_json(data: dict) -> RecommenderFilter:
    out: RecommenderFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Values") is not None:
        import capo_customer_profiles.types.recommender_filter_values

        out["values"] = (
            capo_customer_profiles.types.recommender_filter_values.deserialize_json(
                data["Values"]
            )
        )
    return out


def redact_sensitive(value: RecommenderFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "values" in value:
        import capo_customer_profiles.types.recommender_filter_values

        out["values"] = (
            capo_customer_profiles.types.recommender_filter_values.redact_sensitive(
                value["values"]
            )
        )
    return out
