"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ListSubscriptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pricing_plan_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pricing_plan_manager.types.subscription_summary_list


class ListSubscriptionsOutput(TypedDict, closed=True):
    subscription_summaries: "capo_pricing_plan_manager.types.subscription_summary_list.SubscriptionSummaryList"
    """<p>The list of subscription summaries for the calling account.</p>"""
    next_token: NotRequired["str"]
    """<p>A token that indicates there are more results available. Pass this value in a subsequent <code>ListSubscriptions</code> request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsOutput) -> dict:
    out: dict = {}
    import capo_pricing_plan_manager.types.subscription_summary_list

    out["subscriptionSummaries"] = (
        capo_pricing_plan_manager.types.subscription_summary_list.serialize_json(
            value["subscription_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscriptionsOutput:
    out: ListSubscriptionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("subscriptionSummaries") is not None:
        import capo_pricing_plan_manager.types.subscription_summary_list

        out["subscription_summaries"] = (
            capo_pricing_plan_manager.types.subscription_summary_list.deserialize_json(
                data["subscriptionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListSubscriptionsOutput.subscription_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
