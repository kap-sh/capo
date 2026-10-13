"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListOrganizationRecommendationAccountsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list


class ListOrganizationRecommendationAccountsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    account_recommendation_lifecycle_summaries: "capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list.AccountRecommendationLifecycleSummaryList"
    """<p>The account recommendations lifecycles that are applicable to the Recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationRecommendationAccountsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list

    out["accountRecommendationLifecycleSummaries"] = (
        capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list.serialize_json(
            value["account_recommendation_lifecycle_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListOrganizationRecommendationAccountsResponse:
    out: ListOrganizationRecommendationAccountsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("accountRecommendationLifecycleSummaries") is not None:
        import capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list

        out["account_recommendation_lifecycle_summaries"] = (
            capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list.deserialize_json(
                data["accountRecommendationLifecycleSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListOrganizationRecommendationAccountsResponse.account_recommendation_lifecycle_summaries required"
        )
    return out


def redact_sensitive(
    value: ListOrganizationRecommendationAccountsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "account_recommendation_lifecycle_summaries" in value:
        import capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list

        out["account_recommendation_lifecycle_summaries"] = (
            capo_trustedadvisor.types.account_recommendation_lifecycle_summary_list.redact_sensitive(
                value["account_recommendation_lifecycle_summaries"]
            )
        )
    return out
