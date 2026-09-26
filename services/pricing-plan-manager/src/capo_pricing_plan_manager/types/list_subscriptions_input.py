"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ListSubscriptionsInput``."""

from typing_extensions import NotRequired, TypedDict


class ListSubscriptionsInput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token from a previous <code>ListSubscriptions</code> response. If the response included a <code>nextToken</code>, there are more results available. Pass this value to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscriptionsInput:
    out: ListSubscriptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
