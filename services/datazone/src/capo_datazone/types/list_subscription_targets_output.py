"""Generated from Smithy shape ``com.amazonaws.datazone#ListSubscriptionTargetsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.pagination_token
    import capo_datazone.types.subscription_targets


class ListSubscriptionTargetsOutput(TypedDict, closed=True):
    items: "capo_datazone.types.subscription_targets.SubscriptionTargets"
    """<p>The results of the <code>ListSubscriptionTargets</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of subscription targets is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription targets, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionTargets</code> to list the next set of subscription targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionTargetsOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.subscription_targets

    out["items"] = capo_datazone.types.subscription_targets.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscriptionTargetsOutput:
    out: ListSubscriptionTargetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.subscription_targets

        out["items"] = capo_datazone.types.subscription_targets.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListSubscriptionTargetsOutput.items required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSubscriptionTargetsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.subscription_targets

        out["items"] = capo_datazone.types.subscription_targets.redact_sensitive(
            value["items"]
        )
    return out
