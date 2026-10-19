"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchMessageTemplatesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_search_results_list
    import capo_qconnect.types.next_token


class SearchMessageTemplatesResponse(TypedDict, closed=True):
    results: "capo_qconnect.types.message_template_search_results_list.MessageTemplateSearchResultsList"
    """<p>The results of the message template search.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchMessageTemplatesResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.message_template_search_results_list

    out["results"] = (
        capo_qconnect.types.message_template_search_results_list.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchMessageTemplatesResponse:
    out: SearchMessageTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_qconnect.types.message_template_search_results_list

        out["results"] = (
            capo_qconnect.types.message_template_search_results_list.deserialize_json(
                data["results"]
            )
        )
    else:
        out["results"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchMessageTemplatesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_qconnect.types.message_template_search_results_list

        out["results"] = (
            capo_qconnect.types.message_template_search_results_list.redact_sensitive(
                value["results"]
            )
        )
    return out
