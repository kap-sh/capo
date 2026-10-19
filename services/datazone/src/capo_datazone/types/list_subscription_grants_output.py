"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptionGrantsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.pagination_token
    import capo_datazone.types.subscription_grants


class ListSubscriptionGrantsOutput(TypedDict, closed=True):
    items: "capo_datazone.types.subscription_grants.SubscriptionGrants"
    """<p>The results of the <code>ListSubscriptionGrants</code> action. </p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of subscription grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionGrants</code> to list the next set of subscription grants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionGrantsOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.subscription_grants

    out["items"] = capo_datazone.types.subscription_grants.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscriptionGrantsOutput:
    out: ListSubscriptionGrantsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.subscription_grants

        out["items"] = capo_datazone.types.subscription_grants.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
