"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListRecommendersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_summary_list
    import capo_customer_profiles.types.token


class ListRecommendersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>A token to retrieve the next page of results. Null if there are no more results to retrieve.</p>"""
    recommenders: NotRequired[
        "capo_customer_profiles.types.recommender_summary_list.RecommenderSummaryList"
    ]
    """<p>A list of recommenders and their properties in the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recommenders" in value:
        import capo_customer_profiles.types.recommender_summary_list

        out["Recommenders"] = (
            capo_customer_profiles.types.recommender_summary_list.serialize_json(
                value["recommenders"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecommendersResponse:
    out: ListRecommendersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Recommenders") is not None:
        import capo_customer_profiles.types.recommender_summary_list

        out["recommenders"] = (
            capo_customer_profiles.types.recommender_summary_list.deserialize_json(
                data["Recommenders"]
            )
        )
    return out


def redact_sensitive(value: ListRecommendersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommenders" in value:
        import capo_customer_profiles.types.recommender_summary_list

        out["recommenders"] = (
            capo_customer_profiles.types.recommender_summary_list.redact_sensitive(
                value["recommenders"]
            )
        )
    return out
