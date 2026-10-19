"""Generated from Smithy shape ``com.amazonaws.amplify#ListWebhooksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.next_token
    import capo_amplify.types.webhooks


class ListWebhooksResult(TypedDict, closed=True):
    webhooks: "capo_amplify.types.webhooks.Webhooks"
    """<p>A list of webhooks. </p>"""
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If non-null, the pagination token is returned in a result. Pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebhooksResult) -> dict:
    out: dict = {}
    import capo_amplify.types.webhooks

    out["webhooks"] = capo_amplify.types.webhooks.serialize_json(value["webhooks"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWebhooksResult:
    out: ListWebhooksResult = {}  # type: ignore[typeddict-item]
    if data.get("webhooks") is not None:
        import capo_amplify.types.webhooks

        out["webhooks"] = capo_amplify.types.webhooks.deserialize_json(data["webhooks"])
    else:
        out["webhooks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
