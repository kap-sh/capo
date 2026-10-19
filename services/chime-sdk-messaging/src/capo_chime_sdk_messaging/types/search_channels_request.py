"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchChannelsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.max_results
    import capo_chime_sdk_messaging.types.next_token
    import capo_chime_sdk_messaging.types.search_fields


class SearchChannelsRequest(TypedDict, closed=True):
    chime_bearer: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>"""
    fields: "capo_chime_sdk_messaging.types.search_fields.SearchFields"
    """<p>A list of the <code>Field</code> objects in the channel being searched.</p>"""
    max_results: NotRequired["capo_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of channels that you want returned.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token returned from previous API requests until the number of channels is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchChannelsRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.search_fields

    out["Fields"] = capo_chime_sdk_messaging.types.search_fields.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> SearchChannelsRequest:
    out: SearchChannelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Fields") is not None:
        import capo_chime_sdk_messaging.types.search_fields

        out["fields"] = capo_chime_sdk_messaging.types.search_fields.deserialize_json(
            data["Fields"]
        )
    else:
        out["fields"] = []
    return out


def redact_sensitive(value: SearchChannelsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
