"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommenderFiltersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_filter_summary_list
    import capo_customer_profiles.types.token


class ListRecommenderFiltersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>A token to retrieve the next page of results. Null if there are no more results to retrieve.</p>"""
    recommender_filters: NotRequired[
        "capo_customer_profiles.types.recommender_filter_summary_list.RecommenderFilterSummaryList"
    ]
    """<p>A list of recommender filters and their properties in the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommenderFiltersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommender_filters" in value:
        import capo_customer_profiles.types.recommender_filter_summary_list

        out["RecommenderFilters"] = (
            capo_customer_profiles.types.recommender_filter_summary_list.serialize_json(
                value["recommender_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommenderFiltersResponse:
    out: ListRecommenderFiltersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RecommenderFilters") is not None:
        import capo_customer_profiles.types.recommender_filter_summary_list

        out["recommender_filters"] = (
            capo_customer_profiles.types.recommender_filter_summary_list.deserialize_json(
                data["RecommenderFilters"]
            )
        )
    return out


def redact_sensitive(value: ListRecommenderFiltersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommender_filters" in value:
        import capo_customer_profiles.types.recommender_filter_summary_list

        out["recommender_filters"] = (
            capo_customer_profiles.types.recommender_filter_summary_list.redact_sensitive(
                value["recommender_filters"]
            )
        )
    return out
