"""Generated from Smithy shape ``com.amazonaws.wisdom#ListQuickResponsesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.quick_response_summary_list


class ListQuickResponsesResponse(TypedDict, closed=True):
    quick_response_summaries: (
        "capo_wisdom.types.quick_response_summary_list.QuickResponseSummaryList"
    )
    """<p>Summary information about the quick responses.</p>"""
    next_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuickResponsesResponse) -> dict:
    out: dict = {}
    import capo_wisdom.types.quick_response_summary_list

    out["quickResponseSummaries"] = (
        capo_wisdom.types.quick_response_summary_list.serialize_json(
            value["quick_response_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuickResponsesResponse:
    out: ListQuickResponsesResponse = {}  # type: ignore[typeddict-item]
    if data.get("quickResponseSummaries") is not None:
        import capo_wisdom.types.quick_response_summary_list

        out["quick_response_summaries"] = (
            capo_wisdom.types.quick_response_summary_list.deserialize_json(
                data["quickResponseSummaries"]
            )
        )
    else:
        out["quick_response_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListQuickResponsesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "quick_response_summaries" in value:
        import capo_wisdom.types.quick_response_summary_list

        out["quick_response_summaries"] = (
            capo_wisdom.types.quick_response_summary_list.redact_sensitive(
                value["quick_response_summaries"]
            )
        )
    return out
