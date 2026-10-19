"""Generated from Smithy shape ``com.amazonaws.amplify#ListWebhooksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.max_results
    import capo_amplify.types.next_token


class ListWebhooksRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p>The unique ID for an Amplify app. </p>"""
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p>A pagination token. Set to null to start listing webhooks from the start. If non-null,the pagination token is returned in a result. Pass its value in here to list more webhooks. </p>"""
    max_results: NotRequired["capo_amplify.types.max_results.MaxResults"]
    """<p>The maximum number of records to list in a single response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebhooksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWebhooksRequest:
    out: ListWebhooksRequest = {}  # type: ignore[typeddict-item]
    return out
