"""Generated from Smithy shape ``com.amazonaws.inspector#ListEventSubscriptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.pagination_token
    import capo_inspector.types.subscription_list


class ListEventSubscriptionsResponse(TypedDict, closed=True):
    subscriptions: "capo_inspector.types.subscription_list.SubscriptionList"
    """<p>Details of the returned event subscriptions.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p> When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the <b>nextToken</b> parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventSubscriptionsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.subscription_list

    out["subscriptions"] = (
        capo_inspector.types.subscription_list.serialize_aws_json_1_1(
            value["subscriptions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventSubscriptionsResponse:
    out: ListEventSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("subscriptions") is not None:
        import capo_inspector.types.subscription_list

        out["subscriptions"] = (
            capo_inspector.types.subscription_list.deserialize_aws_json_1_1(
                data["subscriptions"]
            )
        )
    else:
        out["subscriptions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
