"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#AccountRecommendationLifecycleSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary

AccountRecommendationLifecycleSummaryList: TypeAlias = list[
    "capo_trustedadvisor.types.account_recommendation_lifecycle_summary.AccountRecommendationLifecycleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountRecommendationLifecycleSummaryList) -> list:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary

    out: list = []
    for item in value:
        out.append(
            capo_trustedadvisor.types.account_recommendation_lifecycle_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccountRecommendationLifecycleSummaryList:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary

    out: AccountRecommendationLifecycleSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_trustedadvisor.types.account_recommendation_lifecycle_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AccountRecommendationLifecycleSummaryList) -> list[Any]:
    import capo_trustedadvisor.types.account_recommendation_lifecycle_summary

    return [
        capo_trustedadvisor.types.account_recommendation_lifecycle_summary.redact_sensitive(
            item
        )
        for item in value
    ]
