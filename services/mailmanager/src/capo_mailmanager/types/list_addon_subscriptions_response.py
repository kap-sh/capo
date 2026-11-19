"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListAddonSubscriptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_subscriptions
    import capo_mailmanager.types.pagination_token


class ListAddonSubscriptionsResponse(TypedDict, closed=True):
    addon_subscriptions: NotRequired[
        "capo_mailmanager.types.addon_subscriptions.AddonSubscriptions"
    ]
    """<p>The list of ingress endpoints.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAddonSubscriptionsResponse) -> dict:
    out: dict = {}
    if "addon_subscriptions" in value:
        import capo_mailmanager.types.addon_subscriptions

        out["AddonSubscriptions"] = (
            capo_mailmanager.types.addon_subscriptions.serialize_aws_json_1_0(
                value["addon_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAddonSubscriptionsResponse:
    out: ListAddonSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonSubscriptions") is not None:
        import capo_mailmanager.types.addon_subscriptions

        out["addon_subscriptions"] = (
            capo_mailmanager.types.addon_subscriptions.deserialize_aws_json_1_0(
                data["AddonSubscriptions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAddonSubscriptionsResponse) -> dict:
    out: dict = {}
    if "addon_subscriptions" in value:
        import capo_mailmanager.types.addon_subscriptions

        out["AddonSubscriptions"] = (
            capo_mailmanager.types.addon_subscriptions.serialize_cbor(
                value["addon_subscriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAddonSubscriptionsResponse:
    out: ListAddonSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AddonSubscriptions") is not None:
        import capo_mailmanager.types.addon_subscriptions

        out["addon_subscriptions"] = (
            capo_mailmanager.types.addon_subscriptions.deserialize_cbor(
                data["AddonSubscriptions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
