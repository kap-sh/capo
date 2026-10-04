"""Generated from Smithy shape ``com.amazonaws.billing#ListBusinessSupportSubscriptionHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.business_support_subscription_contract_list
    import capo_billing.types.page_token


class ListBusinessSupportSubscriptionHistoryResponse(TypedDict, closed=True):
    subscription_contracts: "capo_billing.types.business_support_subscription_contract_list.BusinessSupportSubscriptionContractList"
    """<p>The list of Business Support subscription contracts.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token for the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListBusinessSupportSubscriptionHistoryResponse,
) -> dict:
    out: dict = {}
    import capo_billing.types.business_support_subscription_contract_list

    out["subscriptionContracts"] = (
        capo_billing.types.business_support_subscription_contract_list.serialize_aws_json_1_0(
            value["subscription_contracts"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListBusinessSupportSubscriptionHistoryResponse:
    out: ListBusinessSupportSubscriptionHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("subscriptionContracts") is not None:
        import capo_billing.types.business_support_subscription_contract_list

        out["subscription_contracts"] = (
            capo_billing.types.business_support_subscription_contract_list.deserialize_aws_json_1_0(
                data["subscriptionContracts"]
            )
        )
    else:
        raise DeserializationError(
            "ListBusinessSupportSubscriptionHistoryResponse.subscription_contracts required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
