"""Generated from Smithy shape ``com.amazonaws.qconnect#ListContentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.content_summary_list
    import capo_qconnect.types.next_token


class ListContentsResponse(TypedDict, closed=True):
    content_summaries: "capo_qconnect.types.content_summary_list.ContentSummaryList"
    """<p>Information about the content.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContentsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.content_summary_list

    out["contentSummaries"] = capo_qconnect.types.content_summary_list.serialize_json(
        value["content_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContentsResponse:
    out: ListContentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("contentSummaries") is not None:
        import capo_qconnect.types.content_summary_list

        out["content_summaries"] = (
            capo_qconnect.types.content_summary_list.deserialize_json(
                data["contentSummaries"]
            )
        )
    else:
        out["content_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
