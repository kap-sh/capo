"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListAccessLogSubscriptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_subscription_list
    import capo_vpc_lattice.types.next_token


class ListAccessLogSubscriptionsResponse(TypedDict, closed=True):
    items: (
        "capo_vpc_lattice.types.access_log_subscription_list.AccessLogSubscriptionList"
    )
    """<p>Information about the access log subscriptions.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessLogSubscriptionsResponse) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.access_log_subscription_list

    out["items"] = capo_vpc_lattice.types.access_log_subscription_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccessLogSubscriptionsResponse:
    out: ListAccessLogSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_vpc_lattice.types.access_log_subscription_list

        out["items"] = (
            capo_vpc_lattice.types.access_log_subscription_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
